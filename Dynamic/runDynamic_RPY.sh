#!/bin/bash
cd /home/pi/OHSU_ANKLE/Dynamic
git pull
lxterminal --command "sudo nice -n -20 /home/pi/.pyenv/versions/3.6.6/bin/python /home/pi/OHSU_ANKLE/Dynamic/main1force.py" &
lxterminal --command "sudo nice -n -20 /home/pi/.pyenv/versions/3.6.6/bin/python /home/pi/OHSU_ANKLE/Dynamic/readforcecallable.py"
