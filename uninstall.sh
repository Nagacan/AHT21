#!/bin/bash

set -e

USERNAME=$(whoami)
PROJECT_DIR="/home/$USERNAME/AHT21"
SERVICE_NAME="backend.service"

echo "⚠️  This will stop the backend service, remove it, delete project files, and restore NGINX config."
echo "Press Ctrl+C to cancel or wait 5 seconds to continue..."
sleep 5

# === Stop and Disable backend.service ===
echo "[1/4] Stopping and disabling systemd service..."
sudo systemctl stop $SERVICE_NAME || true
sudo systemctl disable $SERVICE_NAME || true
sudo rm -f "/etc/systemd/system/$SERVICE_NAME"
sudo systemctl daemon-reload

# === Remove Project Directory ===
echo "[2/4] Removing project directory at $PROJECT_DIR..."
rm -rf "$PROJECT_DIR"

# === Remove frontend HTML files ===
echo "[3/4] Deleting frontend files from /var/www/html..."
sudo rm -f /var/www/html/index.html
sudo rm -f /var/www/html/history.html

# === Restore NGINX default config (optional, backup first if needed) ===
echo "[4/4] Restoring default NGINX config..."
sudo apt-get install --reinstall nginx -y
sudo systemctl restart nginx

# === Done ===
echo "✅ Uninstall complete. You can remove the repo folder if desired."
