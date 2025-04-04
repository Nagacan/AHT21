# AHT21
Tutorial to create a temperature and humidity sensor using AHT21 and Raspberry Pi Zero W. 

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

Breadboard and Jumper Wires (female-male wires; need 4 wires to connect the sensors to the breadboard and RPi; any breadboard is fine)

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
  <img src="https://images.theengineeringprojects.com/image/webp/2021/03/raspberry-pi-zero-5.png.webp?ssl=1" height="400" />
  <img src="https://m.media-amazon.com/images/I/61+RVpqV5AL._AC_UF1000,1000_QL80_.jpg" height="400" />
</p>

#### Use Male to Female Pins (Connect Male to Sensor/Breadboard, and Females to GPIO Pins on RPi)
1. VCC (or VIN) on the Sensor to 3.3V on the Pi
2. GND (Ground) on the Sensor to Ground on the Pi
3. SDA (Data) on the Sensor to GPIO2 (SDA1) on the Pi
4. SCL (Clock) on the sensor to GPIO3 (SCL1) on the Pi

## Setting Up the Raspberry Pi (headless)
### 1. Flash Raspberry Pi OS
1. Use Raspberry Pi Imager to flash Raspberry Pi OS onto your SD card.
2. In the imager settings:
      1. Enable SSH (Password Auth)
      2. 

Set your hostname (or leave default raspberrypi)

Set username/password (e.g., admin/admin)

Configure Wireless LAN (SSID and password)

Set country: US, timezone: America/Los_Angeles, keyboard: US

    1. enable SSH
    2.  and use Password Auth, you can set that hostname to anything I will uncheck it. set your username and password to anything - mine is admin, admin, and configuer wireless LAN (used to connect to your own hotspot or wifi)
I will use eduroam, and password, as the SSID and password. WIreless LAN country as US. America los angelos as local settings, and keyboard as US. Telemetry can be enabled (mine is checked). Apply the change (this will wipe eveyrthing previously on it). Should take a few minutes to finish. Take a picture or something of these settings. You will need them.
Once it's finished. Go into the file bootfs folder, and then make two text files. One name it as "ssh", and nothing else , and the other "wpa_supplicant.txt" (or download and import the supplicant file I'm using)- you want to have everything in there the same and adjusted to your own settings. Once you're done, or whenever u want you can change it to "wpa_supplicant.conf", however you migth need an application to access it.
 1. First item
2. Second item
3. Third item
1. Indented item
    2. Indented item
. Then eject the Sd card from your computter and put it in the RPI, and then plug your RPI in using a micro usb cable. It might take a while to connect. And sometimes, since it's an intial start up, it won't connect. I would reccomend you to plug it in, leave it in with the hotspot on (automatically connects) for about 5 minutes. Then if nothing shows up connected, unplug it, and replug. After waiting about 5 mins, I unplug and replugged it in and it connected to my hotspot after about 2 minutes. 

to ssh (secure shell (protocol); remotely connect; the raspberry pi is a microcomputer) into the PI go to the command terminal and type "ssh raspberrypi.local"; this is because I unchcked the host name as a result it's the default name, if you have a personal name for it use "ssh username@hostname.local", "ssh username@<IP_ADDRESS>" if you have the IP address of the PI. The username is the username you previously set (with it's password)

type y then enter to continue connecting. It will give you a fingerprint, type yes, you don't need this and there are ways to find the Pi's fingerprint. Type in your password (note here when you type the password it won't show anything, or indicate that you are typing). Once done with password type enter. 

Update software to the latest version using “sudo apt-get update”
Using “sudo raspi-config” changed the password to make sure it was “paul393875” and you can configure it in system configure and then change password.
before you do anything as well.
do the sudo raspi config
Go to:Interfacing Options → I2C → Enable
then reboot the pi, usingn sudo reboot

 “sudo apt install -y build-essential git libi2c-dev i2c-tools” which is basically just downloading the libraries. (-y automatically confirms the installation, so you don’t have to manually type Y when prompted.)
- build-essential – Installs essential development tools, including:

    gcc (GNU C Compiler)
    g++ (GNU C++ Compiler)
    make (build automation tool)
    Other development utilities

git – Installs Git, a version control system used for cloning and managing repositories.

libi2c-dev – Installs development libraries for working with the I²C (Inter-Integrated Circuit) protocol, allowing your Raspberry Pi to communicate with I²C devices.

i2c-tools – Installs utilities to interact with I²C devices from the command line, such as:
    i2cdetect (scan for I²C devices)
    i2cget (read from an I²C device)
    i2cset (write to an I²C device)
    i2cdump (dump contents of an I²C device)

Now you need to install the senesor library, for this you need to make a virtual environment. because Debian-based systems (including Raspberry Pi OS)  use a stricter package management system to prevent conflicts between system-installed and user-installed Python packages
Type this into the terminal
mkdir ~/AHT21 #(this makes a folder in the directory called AHT21; to keep everything organized)
then go into tthe folder with cd AHT21/ ## important, always remember to go into this folder, to get access to the folders etc, or clarify your directory/file location.

python3 -m venv environment (this makes a vietual eniroment called environemnt) (this one might take a minute about 2-3 ), then type into the terminal 
source environment/bin/activate (activate and uses the environemnt, download the external libraries and installations here)

then "pip3 install adafruit-circuitpython-ahtx0" - will take a while, about 2-3 or maybe 5 mins. if it says warning retrying after connection broken don't worry, just leave it and let it finish. Be sure not to press any buttons or disturb it (cntrl c kills the command)
Every time you want to use this environment, activate it with:

source environment/bin/activate
"deactivate" if you want to get out

isntall flask 
pip3 install flask (might takke 5 minis)

https://nginx.org/en/linux_packages.html#Debian
follow this website
Do everything it says under Debian in the putty terminal, inside the correct directory and virtual environment 

sudo apt install curl gnupg2 ca-certificates lsb-release debian-archive-keyring

curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor \
    | sudo tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null

gpg --dry-run --quiet --no-keyring --import --import-options import-show /usr/share/keyrings/nginx-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

(apt repository for stable nginx packages) OR (mainline nginx packages) - doesnt matter (i just installed both)
    
echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/mainline/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list

echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx

then to install nginx
sudo apt update
sudo apt install nginx

if you want to find out your hostname or ip address type into the terminal
hostname or hostname -I

After nginx is installed you can access your website on 
http://<<IP_Address_Here>>
or just type your IP address into the brwoser

remmber cd AHT21/
then source environment/bin/activate
to get into the folder/directory and then actiavting the envinroment

http://192.168.137.8/ is my page

Creating the system file, backend, and frontends (make sure  you do all of this in the AHT21/ directory, and in your environment just to be safe). 
backedn:
Configure Nginx as a reverse proxy to point to your Flask app. Edit the Nginx configuration file to forward requests from /data to your Flask backend in your virtual environment 
sudo nano /etc/nginx/sites-available/default
(replace everything in this file with everything in the file i provided in NGINX_setup, or just import the file I provided and replace it with the one already there)

Install a database:
sudo apt install sqlite3
pip install flask-cors


Create the backend 
sudo nano backend.py, and replace everything in here with the file provided or just import the file i provided in that directory (directory and name of the file matters)

Do the same with the two front ends
sudo nano /var/www/html/index.html
sudo nano /var/www/html/history.html

Do the same for the system file (This is important though, you may need to change the directory and address accordingly), so go into the system (backend.service) file that I provided and read the directioins
or in other words, just change all of the hostnames to your hostname. 
sudo nano /etc/systemd/system/backend.service

Once you're done. sudo systemctl daemon-reload to restart the service and do these in order
sudo systemctl enable backend.service       -enables the service
sudo systemctl start backend2.service       -starts the service 
sudo systemctl status backend2.service    -checks status of the service

fixed some of the databases and locations of the addresses in the backend and the system file code. 
Previously my backend also didn't create a table in the sqlite database so I've included that
