#!/bin/bash
cd /home/pi/OHSU_ANKLE
sudo fetch origin
sudo git reset --hard origin/main
sudo git pull
cd /home/pi/OHSU_ANKLE/Dynamic
lxterminal --command "sudo nice -n -20 /home/pi/.pyenv/versions/3.6.6/bin/python /home/pi/OHSU_ANKLE/Dynamic/main1force.py" &
lxterminal --command "sudo nice -n -20 /home/pi/.pyenv/versions/3.6.6/bin/python /home/pi/OHSU_ANKLE/Dynamic/readforcecallable.py"
