import time
import os
import threading
import board
import adafruit_ahtx0
import sqlite3
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

# Flask App
app = Flask(__name__)
CORS(app)

# Sensor Setup
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

# Database Path
db_path = "/home/paul393875/AHT21/sensor_data.db"

# Storage Threshold (in MB)
THRESHOLD_MB = 500

db_lock = threading.Lock()  # Ensuring database thread safety

def enable_wal_mode():
	"""Enable Write-Ahead Logging (WAL) mode to allow multiple readers while writing."""
	try:
    	with db_lock:
        	conn = sqlite3.connect(db_path, check_same_thread=False)
        	conn.execute("PRAGMA journal_mode=WAL;")
        	conn.execute("PRAGMA synchronous=NORMAL;")
        	conn.close()
        	print("WAL mode enabled for SQLite.")
	except Exception as e:
    	print(f"Error enabling WAL mode: {e}")

enable_wal_mode()  # Run this once at startup

def get_free_space_mb():
	"""Check available storage on the SD card in MB."""
	statvfs = os.statvfs("/")
	free_space = (statvfs.f_bavail * statvfs.f_frsize) / (1024 * 1024)  # Convert to MB
	return free_space

def delete_oldest_data():
	"""Delete the oldest day's data from the database if storage is low."""
	try:
    	conn = sqlite3.connect(db_path)
    	cursor = conn.cursor()

    	# Find the oldest date in the database
    	cursor.execute("SELECT MIN(DATE(timestamp)) FROM sensor_data")
    	oldest_date = cursor.fetchone()[0]

    	if oldest_date:
        	print(f"Deleting data from {oldest_date} to free up space...")
        	cursor.execute("DELETE FROM sensor_data WHERE DATE(timestamp) = ?", (oldest_date,))
        	conn.commit()
        	print(f"Data from {oldest_date} deleted successfully.")
    	else:
        	print("No data found to delete.")

    	conn.close()
	except Exception as e:
    	print(f"Error deleting old data: {e}")

def monitor_storage():
	"""Continuously check storage and delete old data when needed."""
	while True:
    	free_space = get_free_space_mb()
    	print(f"Available storage: {free_space:.2f} MB")

    	if free_space < THRESHOLD_MB:
        	print("Low storage detected! Deleting oldest data...")
        	delete_oldest_data()
    	else:
        	print("Storage is sufficient, no need to delete data.")

    	time.sleep(600)  # Check every 10 minutes

# Run storage cleanup in a background thread
storage_thread = threading.Thread(target=monitor_storage, daemon=True)
storage_thread.start()

def log_data():
	"""Log sensor data into the database."""
	try:
    	conn = sqlite3.connect(db_path)
    	c = conn.cursor()

    	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    	temperature = sensor.temperature
    	humidity = sensor.relative_humidity

    	c.execute('INSERT INTO sensor_data (timestamp, temperature, humidity) VALUES (?, ?, ?)',
              	(current_time, temperature, humidity))
    	conn.commit()
    	conn.close()
	except Exception as e:
    	print(f"Error logging data: {e}")

def periodic_logging():
	"""Continuously log data every 2 seconds."""
	while True:
    	start_time = time.time()
    	log_data()
    	elapsed_time = time.time() - start_time
    	time_to_wait = max(0, 2 - elapsed_time)
    	time.sleep(time_to_wait)

# Start the data logging in a separate thread
threading.Thread(target=periodic_logging, daemon=True).start()

@app.route('/data', methods=['GET'])
def get_data():
	"""API endpoint to get live sensor data."""	try:
    	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    	data = {
        	"time": current_time,
        	"temperature": round(sensor.temperature, 2),
        	"humidity": round(sensor.relative_humidity, 2)
    	}
    	return jsonify(data)
	except Exception as e:
    	return jsonify({"error": f"Failed to fetch live data: {e}"}), 500

@app.route('/history', methods=['GET'])
def get_history():
	"""API endpoint to get historical sensor data sorted by day."""
	try:
    	conn = sqlite3.connect(db_path)
    	c = conn.cursor()
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

if __name__ == '__main__':
	try:
    	app.run(host='0.0.0.0', port=5000)
	except Exception as e:
    	print(f"Error starting the server: {e}")
