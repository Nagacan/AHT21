#!/bin/bash
set -e

# === Basic Variables ===
USERNAME=$(whoami)
REPO_DIR=$(pwd)
PROJECT_DIR="/home/$USERNAME/AHT21"
PYTHON_ENV="$PROJECT_DIR/environment"
SERVICE_TEMPLATE="$REPO_DIR/SystemD/backend.service"
SERVICE_DEST="/etc/systemd/system/backend.service"

# Pick a Python that has GPIO wheels
if command -v python3.11 >/dev/null 2>&1; then
  PYTHON_BIN="python3.11"
else
  PYTHON_BIN="python3"
fi

echo "[1/10] Updating system packages..."
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

# Ensure venv package for the chosen Python
if [ "$PYTHON_BIN" = "python3.11" ]; then
  sudo apt-get install -y python3.11-venv || sudo apt-get install -y python3-venv
else
  sudo apt-get install -y python3-venv
fi

echo "[2/10] Enabling I2C..."
sudo raspi-config nonint do_i2c 0
sudo usermod -aG i2c "$USERNAME"

echo "[3/10] Setting timezone to America/Los_Angeles..."
sudo timedatectl set-timezone America/Los_Angeles

echo "[4/10] Setting up project directory at $PROJECT_DIR"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

echo "[5/10] Copying backend code..."
cp "$REPO_DIR/Backend_Code/backend.py" "$PROJECT_DIR/backend.py"

echo "[6/10] Creating virtual environment with $PYTHON_BIN..."
$PYTHON_BIN -m venv "$PYTHON_ENV"
# shellcheck disable=SC1090
source "$PYTHON_ENV/bin/activate"

echo "[7/10] Installing Python packages into the venv..."
"$PYTHON_ENV/bin/pip" install --upgrade pip wheel setuptools
# Hardware access layers
"$PYTHON_ENV/bin/pip" install RPi.GPIO adafruit-blinka
# Sensor driver
"$PYTHON_ENV/bin/pip" install adafruit-circuitpython-ahtx0
# Web backend
"$PYTHON_ENV/bin/pip" install flask flask-cors

echo "[8/10] Configuring NGINX..."
sudo cp "$REPO_DIR/NGINX_Setup/default" /etc/nginx/sites-available/default
sudo systemctl restart nginx

echo "[9/10] Deploying frontend files..."
sudo cp "$REPO_DIR/Frontend_Code/index.html" /var/www/html/index.html
sudo cp "$REPO_DIR/Frontend_Code/history.html" /var/www/html/history.html

echo "[10/10] Configuring backend service..."
# Replace %u with the current username in your template
sed "s|%u|$USERNAME|g" "$SERVICE_TEMPLATE" | sudo tee "$SERVICE_DEST" > /dev/null

sudo systemctl daemon-reload
sudo systemctl enable backend.service
sudo systemctl restart backend.service

echo "✅ Installation complete."
echo "Visit your Pi at: http://<your_pi_ip>  (use 'hostname -I' to see the IP)"
echo "If the service cannot import RPi.GPIO or board, confirm the venv Python is $PYTHON_BIN and rerun this script."
