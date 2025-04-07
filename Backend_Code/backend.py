# Copy and paste this into your backend file, or just import the file
import os
import time
import threading
import sqlite3
import board
import adafruit_ahtx0
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

# Flask App and setup
app = Flask(__name__)
CORS(app)

# Get the directory where backend.py is located (dynamic path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sensor_data.db")  # Dynamic database path

# Sensor Setup
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# Storage Threshold (in MB)
THRESHOLD_MB = 500
db_lock = threading.Lock()  # Only one thread can interact with the database at a time

# Creates the table for sqlite 
def initialize_database():
    """Ensure the sensor_data table exists."""
    try: # Try blocks : if get error go instantly to exception
        conn = sqlite3.connect(db_path) # Opens a connection to your SQLite database.
        c = conn.cursor() # Prepares a cursor to execute SQL commands and creates table ->
        c.execute("""
            CREATE TABLE IF NOT EXISTS sensor_data (
                timestamp TEXT,
                temperature REAL,
                humidity REAL
            );
        """)
        conn.commit() # Commits changes
        conn.close() # Closes the connection
        print("Database initialized successfully.")
    except Exception as e: # Instead of crashing entire program prints this
        print(f"Error initializing database: {e}")

# Call this function at startup so that it creates the table
initialize_database()

#allows multiple readers with 1 writer
def enable_wal_mode():
    """Enable Write-Ahead Logging (WAL) mode to allow multiple readers while writing."""
    try:
        with db_lock:
            conn = sqlite3.connect(db_path, check_same_thread=False) # Allows this connection to be used in threads other than the one that created it 
            conn.execute("PRAGMA journal_mode=WAL;") # PRAGMA command to switch the journaling mode to WAL
            conn.execute("PRAGMA synchronous=NORMAL;") # Controls how carefully SQLite waits for data to be fully written to disk during a COMMIT
            conn.close() # Closes the database connection 
            print("WAL mode enabled for SQLite.")
    except Exception as e:
        print(f"Error enabling WAL mode: {e}")

enable_wal_mode()  # Run this once at startup

# Checks how much free storage is available and returns in mgbs
def get_free_space_mb():
    """Check available storage on the SD card in MB."""
    statvfs = os.statvfs("/") # Gets filesystem statistics for the given path in root directory
    free_space = (statvfs.f_bavail * statvfs.f_frsize) / (1024 * 1024)  # Calculates total space then converts to MB (total space /(1024 * 1024))
    return free_space

# Deletes oldest day worth of data
def delete_oldest_data():
    """Delete the oldest day's data from the database if storage is low."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
# 79-80 Checks oldest date; ignores the time part and just compares by day
        cursor.execute("SELECT MIN(DATE(timestamp)) FROM sensor_data")
        oldest_date = cursor.fetchone()[0]
# If a date exists (meaning the table has data), go ahead and delete. If not prints nothing to delete. 
        if oldest_date:
            print(f"Deleting data from {oldest_date} to free up space...")
            cursor.execute("DELETE FROM sensor_data WHERE DATE(timestamp) = ?", (oldest_date,))
            conn.commit()
            print(f"Data from {oldest_date} deleted successfully.")
        else:
            print("No data found to delete.")
# Closes the connection
        conn.close()
    except Exception as e:
        print(f"Error deleting old data: {e}")

# Checks every 10 minutes to see if storage is ok
def monitor_storage():
    """Continuously check storage and delete old data when needed."""
    while True: # Runs continuously
        free_space = get_free_space_mb() # Gets the current free space in MB using the helper function.
        print(f"Available storage: {free_space:.2f} MB") # Prints it with 2 decimal precision so you can see storage dropping or increasing over time.
# If free space is below a threshold (e.g. THRESHOLD_MB = 100), it deletes the oldest day’s data. If there's enough space, it just prints a status update.
        if free_space < THRESHOLD_MB: # Checks free space with threshold we set earlier
            print("Low storage detected! Deleting oldest data...")
            delete_oldest_data() # Runs the function we made above to delete oldest data
        else:
            print("Storage is sufficient, no need to delete data.")
# Sets a 10 minute delay before the function reruns
        time.sleep(600)  # Check every 10 minutes

# Run storage cleanup in a background thread
storage_thread = threading.Thread(target=monitor_storage, daemon=True) # Tells the thread to run the monitor function we made above and run it as daemon thread (automatically exit when the main program exits)
storage_thread.start() # Starts the thread

#logs the live sensor data
def log_data():
    """Log sensor data into the database."""
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Takes current time and formats it into a human-readable string
        temperature = sensor.temperature  # Pull data from your sensor object 
        humidity = sensor.relative_humidity # Pull data from your sensor object 
# SQL command inserts the data using ? placeholders for safety (avoids SQL injection).
        c.execute('INSERT INTO sensor_data (timestamp, temperature, humidity) VALUES (?, ?, ?)',
                  (current_time, temperature, humidity))
        conn.commit() # Commits the change
        conn.close() # Closes connection
    except Exception as e:
        print(f"Error logging data: {e}")
# This will keep logging data to your database at 2-second intervals — indefinitely.
def periodic_logging():
    """Continuously log data every 2 seconds."""
    while True: # Forever Loop 
        start_time = time.time() # Captures the start time before logging.
        log_data() # Calls log_data() (which talks to the sensor + DataBase).
        elapsed_time = time.time() - start_time # Calculates how long that took.
        time_to_wait = max(0, 2 - elapsed_time) # Subtracts elapsed_time from 2 seconds to determine how long to sleep. Max makes sure no negative
        time.sleep(time_to_wait)

# Start the data logging in a separate thread, runs the logging function, daemon thread, and starts
threading.Thread(target=periodic_logging, daemon=True).start()

@app.route('/data', methods=['GET']) # Flask route that listens at /data for GET requests.
def get_data():
    """API endpoint to get live sensor data."""
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Current system time in a readable format. Below gets data to 2 decimal points
        data = {
            "time": current_time,
            "temperature": round(sensor.temperature, 2),
            "humidity": round(sensor.relative_humidity, 2)
        }
        return jsonify(data) # Returns JSON response
    except Exception as e: # Returns a 500 Internal Server Error if something breaks. No crashes
        return jsonify({"error": f"Failed to fetch live data: {e}"}), 500

@app.route('/history', methods=['GET']) # Sets up a Flask GET endpoint at /history.
def get_history():
    """API endpoint to get historical sensor data sorted by day."""
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor() # Below use GROUP_CONCAT to bundle all times, temps, and humidity values as comma-separated strings per day. Return them sorted from newest to oldest.
        c.execute("""
            SELECT DATE(timestamp) AS date,
                   GROUP_CONCAT(TIME(timestamp)) AS times,
                   GROUP_CONCAT(temperature) AS temperatures,
                   GROUP_CONCAT(humidity) AS humidities
            FROM sensor_data
            GROUP BY date
            ORDER BY date DESC
        """)
        rows = c.fetchall()
        conn.close()
# Splits the comma-separated values into actual Python lists. Converts temperature and humidity strings to floats. Creates a list of dicts
        grouped_data = [
            {
                "date": row[0],
                "times": row[1].split(","),
                "temperatures": [float(t) for t in row[2].split(",")],
                "humidities": [float(h) for h in row[3].split(",")]
            }
            for row in rows
        ]
        return jsonify(grouped_data)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch historical data: {e}"}), 500

if __name__ == '__main__': # This checks whether the script is being run directly 
    try:
        app.run(host='0.0.0.0', port=5000) # Makes the server accessible from any IP on the local network (important for Raspberry Pi setups). Uses default Flask Port
    except Exception as e:
        print(f"Error starting the server: {e}")

