# AHT21
Tutorial to create a temperature and humidity sensor using AHT21 and Raspberry Pi Zero W. 
## Capabilties:
- Live temperature and humidity graph every 2 seconds
- Historical graph with the ability to view previous dates
- Downloadable data and sortable historical data table
- Automatic data logging starts as soon as the Raspberry Pi is powered on 
- Local web interface becomes available once the Pi is connected to Wi-Fi
- Smart disk monitoring: Automatically deletes old data when storage is low
- Timezone auto-configuration via systemd
- Fully autonomous: no user interaction needed after power-up

**Note: Names of Files, passwords, IDs, and Directories (location files are in) are important!**
## Quick Install (Terminal/SSH)
Input the Following into the Terminal (after you SSH into the Pi): 
1. git clone https://github.com/Nagacan/AHT21.git
2. cd AHT21/
3. chmod +x install.sh
4. ./install.sh

(Optional if you want to uninstall; skip step 1/2 below if already did above)
1. git clone https://github.com/Nagacan/AHT21.git
2. cd AHT21/
3. chmod +x uninstall.sh
4. ./uninstall.sh



## Materials:
Raspberry Pi Zero WH (W= Wireless, H= Headers (already soldered on))

[RPi](https://www.amazon.com/Raspberry-Bluetooth-Compatible-Connector-headers/dp/B0CG99MR5W?crid=YN19MCMRYEC1&dib=eyJ2IjoiMSJ9.WEtUDQK3vhQkFbdhbEmfjWrj_9w6I2o00tTxnnLh9T8v7-Q9FfEwbd3aPnh53XCOjxdwvMByjlossEZ1C09VjkflufTdu0pRNFIFnekUCu0adQJX5nQh4ElQ9wNNi-DL-Q3xMKTX_HPr8TQzf7RGnhQQHzqC6pTR_GFXXKtxfP4bni95r93Z5g2F3ZNP_zS_KYKdld8jQgPP9FVbt6xnCznnPfGXeV6_T0t7BzsRcXBVR70CE2qHD10Yeg5-Nt3sz7_yWhvVnHepARwkwowbOIVOQ4I5bI_bCrN6n3VY8508R3fVTiV4f8fcn6lRuFHbSOagvTzI8TnONCw8My3Nu-NLqv8f2wCexAISXRFnCko.ZwAyMG__KfboHmyRSViGvPvxUDbDSHWUBs8Pgnxqoiw&dib_tag=se&keywords=raspberry%2Bpi%2Bzero%2Bw%2Bh&qid=1740175076&s=electronics&sprefix=raspberrry%2Bpi%2Bzero%2Bw%2B%2Celectronics%2C213&sr=1-1&th=1)

AHT21 Sensor (Adafruit Humidity Temperature Sensors; brand matters -> code library used "adafruit_ahtx0")

[AHT21 Sensors](https://www.amazon.com/UMLIFE-Precision-Temperature-Measurement-Communication/dp/B0C6DZ8YZG?crid=6KT50QK4051T&dib=eyJ2IjoiMSJ9.--9iZK9wWnKNwOHjRBdEsnOgpCZcL0V3rZdXW3BneKrRRTUKEV-4xwqiwmOQcXmch-4LNY3CXhMJIaRsgw-YE19_9oPCNUY7Ei-HE64CkUylj3EjCKtYh_Ewwpkd2e4PKiR0iXhrnyx00EvZDfkZAt4KUFXIS3cTuvGOo9QetFUDjWsZ94TcpSM2i5d4UV6Em-8UmNdBAdzkmlJiSg_2t3JLrBuIkqaAguwdcGcRhc0.AL-HbH3saLZ-HQf68Wmw1_wA0j5UtVst3vJWOnykzqc&dib_tag=se&keywords=aht21%2Btemperature%2Bsensor&qid=1740175406&sprefix=AHT21%2Caps%2C204&sr=8-5&th=1)

Breadboard and Jumper Wires 

(__**Male to Female / Female to Male**__ wires; need 4 wires to connect the sensors to the breadboard and RPi; any breadboard is fine)

[Breadboard/Wire Set](https://www.amazon.com/HUAREW-Breadboard-Jumper-Include-Points/dp/B09VKYLYN7?crid=2LV4G3OA5VBHV&dib=eyJ2IjoiMSJ9.ozHaOEz11CAJtB_xbZ27F-e75UuFDp5cGrPdMUK1I-X73Vhc0u1U3IKdbRw0Kn2lsugL24L49g8Us7f-gVrIUbJYOTo5f9XcpIZgNX2lYVgBHJNWRCf06lu8CKsz0uNLRE_UrM8SrzQXpSuyLy9J6Ol_aOHhAF9iOsc1MjEKr7ajN_xdOuw9zKelyJrTrpCoaNsXsZwXg1GpweQhkxVlkcce551PlK4-CNnuCrfSnss.UNmPV_krCkfU3wT4rHPr_wS87d90idZtb-0NkZFWOy4&dib_tag=se&keywords=breadboard+and+jumper+wires&qid=1740175667&sprefix=breadboard+and+jumper+wir%2Caps%2C202&sr=8-3)

Micro-USB Cable and USB Power Supply (any is fine)

[Micro-USB Cable](https://www.amazon.com/Charging-Transfer-Android-Trustable-MYFON/dp/B098DW7485?crid=2KGXKFFMHT4LZ&dib=eyJ2IjoiMSJ9.WR63mKTxAJQICRAe9uZ2APmoXscPxGk0W7TyUC7zUOepA-mpjv4JSKc1TkT1jRBtRmhycVZ-cl4f3JYFXJR7O3_LLi8tkEZYT5f7mRLzJFfMCqghjIbRt4eznJGgL9yjrhd1zb7qvKVPF-RDueImDUPlszzwvTUlVjFaRiWpCVwkkyDuAYS4zCI0-1Tmf3UU56BfcM_TKoSWlt88bGwOz5jYuJS3tRJJiZg0mCpGFHg.CrI8OwJtEzEehjiZbrl8bqo9uIz5VVNQopMxnrXjyEE&dib_tag=se&keywords=micro%2Busb&qid=1740176049&sprefix=micro%2Bus%2Caps%2C424&sr=8-4&th=1)
 | [Power Supply with Micro-USB](https://www.amazon.com/Bawofu-Supply-Charger-Adapter-Universal/dp/B0BSF3TB8P?crid=GUN3N529THFG&dib=eyJ2IjoiMSJ9.lYhV7VDm_2PdWXB38EVtA02ZZ7iTnEt0e1GHHrJR7H-A7YUYv8pu5nxWQ7iMlAVJMPfazuqkRkG1BzAlhpBj4AjYpgJcEcc16EPM8PTqiW1PBQR6Drh13yWa1on5Gw0jTePA4rHzNEF3PaHFvhK9I9OuBv8BXpHlIZpUg0alz7NwJFWD_JH4RpYLw4iHFJc9go3ukDCHMC6_hDzy22HaQ24OA6pjEWbc4NFmOJ38OWE.BmYW0u6zvDPYID3bANagd9w2uxxxoVkdTjy3aoZ5TI8&dib_tag=se&keywords=usb+power+supply+micro+usb&qid=1740176249&sprefix=usb+power+supply+micro+us%2Caps%2C195&sr=8-3)

Micro SD-Card (I used 16 and 32gbs)

[Micro SD-Card](https://www.amazon.com/Center-Memory-Adapter-Mobile-Storage/dp/B08HD83TFJ?crid=2BQCKLHXHA5EH&dib=eyJ2IjoiMSJ9.Uwx19gT9ffNa_idEUNhHLJndkVLmxwwGnyqGY6G1drtN2FIqpZ_wLSP502zU4lT5zjOn7B-wRiLJ6fMHJoWHX165Mj-_fy6-B2s90l42A_S-AtgFJkagv_ywZk8Ex1R8fuDYqfwqa3CWecMKt1EXu0eRoirFcVh3iZrlrp6LsC19x1RwCJnKUxmdas0dDScssYJNrI4B4kqLAXwkg6KeI4XM28WHZFKjpsGHCEmv0Ec.xecKIXm0zfVyXNANv6De-CHw-tlmf1NerkyQ6wCURds&dib_tag=se&keywords=micro+sd+card+16gb+microcenter&qid=1740176570&sprefix=micro+sd+card+16gb+microcente%2Caps%2C182&sr=8-1)

Micro SD-Card Reader/Adapter

[Adapter](https://www.amazon.com/Reader-Adapter-Camera-Memory-Wansurs/dp/B0B9QZ4W4Y?crid=1NRJQU9RFIEUX&dib=eyJ2IjoiMSJ9.aZ5CyI1seaCTFVUzT0NlJpD8dyQjzqiqAURiyClSNrH2BGRKFKbUrMzzF59pt43S0IFH3E6I00N6K6GSyrhpmx3imwonNx4xzcFtk9ZzN4DJMNFZl6cg6qMy5rCOA6W2LOXlkYWOTcdxbBAmjkMfaEBSL3PMtZakDS_UNtSwuSrGZeT5n0gP3ZLp572kA636_A4iDL-Rms6Z5qR8qW5fw_pHX3N3wMLKtk3T0xdtz6U.9WVDsjNrwOKz5CJDiLGtSr47cc6gQd7MSiG2myKHeTE&dib_tag=se&keywords=micro+sd+card+adapter&qid=1740176655&sprefix=micro+sd+card+adapt%2Caps%2C207&sr=8-4)

## Connections
[RPi Pinout](https://www.theengineeringprojects.com/2021/03/what-is-raspberry-pi-zero-pinout-specs-projects-datasheet.html)
<p align="center">
  <img src="https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-zero-5.png.webp?ssl=1" height="350" />
  <img src="https://m.media-amazon.com/images/I/61+RVpqV5AL._AC_UF1000,1000_QL80_.jpg" height="350" />
</p>

**_Use Male to Female Pins (Connect Male to Sensor/Breadboard, and Females to GPIO Pins on RPi)_**

1. VCC (or VIN) on the Sensor to 3.3V on the Pi
2. GND (Ground) on the Sensor to Ground on the Pi
3. SDA (Data) on the Sensor to GPIO2 (SDA1) on the Pi
4. SCL (Clock) on the sensor to GPIO3 (SCL1) on the Pi

# Detailed Guide

## Setting Up the Raspberry Pi (headless)
### 1. Flash Raspberry Pi OS
1. Use Raspberry Pi Imager to flash Raspberry Pi OS onto your SD card.
2. In the Configure OS imager settings:
   * Set your hostname (default: raspberrypi)
   * Set Username/Pass (e.g., admin/admin)
   * Configure Wireless LAN (Wifi/Hotspot SSID and Password)
   * Set country: US, timezone: America/Los_Angeles, keyboard: US
   * Enable SSH (Password Auth)
3. Click save and flash the SD card. This will erase all existing content

### 2. Additional Boot Setup
1. After flashing, open the `bootfs` partition on the SD card
2. Add the following files (or download/import from the one's I already provided in the folder: `RaspberryPi_Setup` for this Repository):
   * a blank file named `ssh`
   * a `wpa_supplicant.conf` file (or `.txt`, rename later if needed) with your specific Wi-Fi config
*If you're using the uploaded config file I provided be sure to edit the contents and change accordingly*

### 3. Boot and Connect
1. Insert the SD card into the Pi and power via micro USB
2. Wait ~5-10 mins. If it doesn't connect to Wi-Fi, unplug and retry/wait.
   * If still doesn't work may be issue with your Wi-Fi configuration
3. SSH into the Pi using CMD Terminal, Or Putty (3rd party app)
   * Default `ssh pi@raspberrypi.local`
   * Custom: `ssh <username>@<hostname>.local` or  `<username>@<IP_ADDRESS>`
4. Accept the SSH Key fingerprint and login with your password (It won't show that you're typing anything)
  
## Initial Configuration
1. Run these commands (one after another) into the terminal
```
sudo apt-get update
sudo raspi-config
```
* Change password (`System Options -> Password`)
* Enable I2C (`Interfacing Options -> I2C -> Enable`)
2. Install Dependencies:
```
sudo apt install -y build-essential git libi2c-dev i2c-tools
```
What These Do:
* build-essential: gcc, g++, make, and other dev tools
* git: Clone and manage repositories
* 2c-dev / i2c-tools: I²C support and tools like i2cdetect
3. Adjust the time to your region. LA as an example is below.
```
sudo timedatectl set-timezone America/Los_Angeles 
```
4. Reboot:
```
sudo reboot
```

### 4. Sensor Setup (AHT21)
1. Create Virtual Environment
```
mkdir ~/AHT21
cd ~/AHT21
python3 -m venv environment
source environment/bin/activate
```
2. Install Sensor Library
```
pip3 install adafruit-circuitpython-ahtx0
```
*Note: Ignore warnings like "retrying after connection broken." Just wait.*

### 5. Install Flask and NGINX
1. Install flask
```
pip3 install flask flask-cors
```
2. Install NGINX by following [NGINX](https://nginx.org/en/linux_packages.html#Debian) Debian Instructions or use commands below:
```
sudo apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring

curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
  | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null

gpg --dry-run --quiet --no-keyring --import --import-options import-show \
  /usr/share/keyrings/nginx-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/debian `lsb_release -cs` nginx" \
  | sudo tee /etc/apt/sources.list.d/nginx.list

# Optionally add mainline repo
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/mainline/debian `lsb_release -cs` nginx" \
  | sudo tee /etc/apt/sources.list.d/nginx.list

echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
  | sudo tee /etc/apt/preferences.d/99nginx

# Install NGINX
sudo apt update
sudo apt install nginx
```

### 5. Backend and Frontend Configuration
1. Setup Flask App and SystemD Service
2. Go to the your project folder and create/import (Import the Backend Folder in my repository `Backend_Code`) Flask Backend
```
cd ~/AHT21
source environment/bin/activate
sudo nano backend.py
```
3. Install SQLite
```
sudo apt install sqlite3
```
4. Setup Systemd Service file (or import from `SystemD`)
```
sudo nano /etc/systemd/system/backend.service
```
* Remember to replace with your Username
5. Reload and enable the service
```
sudo systemctl daemon-reload
sudo systemctl enable backend.service
sudo systemctl start backend.service
sudo systemctl status backend.service
```

### 6. Web Frontend Pages
1. Create/Import these HTML Files `Frontend_Code`
```
sudo nano /var/www/html/index.html
sudo nano /var/www/html/history.html
```
2. Configure NGINX config (or import from `NGINX_Setup`) and restart 
```
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
```

### 7. Access your site
1. Find your Pi's IP and Visit `(http://<YOUR_PI_IP>)`:
```
hostname -I
```
**Always activate your virtual environment before running Python code:**
*  ` source environment/bin/activate `
*  use `deactivate` to exit the environment

