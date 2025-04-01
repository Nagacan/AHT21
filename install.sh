#!/bin/bash

# === Basic Variables ===
USERNAME=$(whoami)
REPO_DIR=$(pwd)
PROJECT_DIR="/home/$USERNAME/AHT21"
PYTHON_ENV="$PROJECT_DIR/environment"
SERVICE_TEMPLATE="SystemD/backend.service"
SERVICE_DEST="/etc/systemd/system/backend.service"

# === Update & Install System Packages ===
echo "[1/9] Updating system packages..."
sudo apt-get update
sudo apt-get install -y \
  build-essential \
  git \
  libi2c-dev \
  i2c-tools \
  sqlite3 \
  curl \
  gnupg2 \
  ca-certificates \
  lsb-release \
  debian-archive-keyring \
  nginx

# === Enable I2C ===
echo "[2/9] Enabling I2C..."
sudo raspi-config nonint do_i2c 0

# === Set Timezone ===
echo "[3/9] Setting timezone to America/Los_Angeles..."
sudo timedatectl set-timezone America/Los_Angeles

# === Create Project Directory ===
echo "[4/9] Setting up project directory at $PROJECT_DIR"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# === Copy Backend Code ===
echo "[5/9] Copying backend code..."
cp "$REPO_DIR/Backend_Code/backend.py" "$PROJECT_DIR/backend.py"

# === Create Virtual Environment and Install Python Dependencies ===
echo "[6/9] Creating virtual environment..."
python3 -m venv environment
source "$PYTHON_ENV/bin/activate"
echo "[6/8] Installing Python packages..."
pip3 install --upgrade pip
pip3 install adafruit-circuitpython-ahtx0 flask flask-cors

# === Setup NGINX ===
echo "[7/9] Configuring NGINX..."
sudo cp "$REPO_DIR/NGINX_Setup/default" /etc/nginx/sites-available/default
sudo systemctl restart nginx

# === Deploy HTML Frontend Files ===
echo "[8/9] Deploying frontend files..."
sudo cp "$REPO_DIR/Frontend_Code/index.html" /var/www/html/index.html
sudo cp "$REPO_DIR/Frontend_Code/history.html" /var/www/html/history.html

# === Setup systemd Service ===
echo "[9/9] Configuring backend service..."
sed "s|%u|$USERNAME|g" "$REPO_DIR/SystemD/backend.service" | sudo tee "$SERVICE_DEST" > /dev/null
sudo systemctl daemon-reload
sudo systemctl enable backend.service
sudo systemctl start backend.service

# === Done ===
echo "✅ Installation complete. Visit your Pi at http://<your_pi_ip>"
echo "Use 'hostname -I' to find your Pi's IP address."
