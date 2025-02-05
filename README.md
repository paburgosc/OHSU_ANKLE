# OHSU_ANKLE
kinematics and Dynamics

Prerequisites
Make sure you have the following installed before running the application:

Python (Python version 3.6.6)

pygame raspbian
   ```bash
sudo apt-get install  libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev  subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
   ```
metawear raspbian
   ```bash
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev

sudo apt-get install bluetooth bluez libbluetooth-dev libudev-dev libboost-all-dev build-essential
   ```
Installation
Clone the repository or download the source code:

   ```bash


  git clone https://github.com/paburgosc/OHSU_ANKLE.git
   ```
   ```bash
  cd OHSU_ANKLE
   ```
Install dependencies:
   ```bash
  pip install -r requirements.txt
   ```

Run the api:
   ```bash
  python readeurlercallable.py
   ```
Running the Application

Ensure the virtual environment is activated.

Run the application:
   ```bash
  python main.py
   ```
