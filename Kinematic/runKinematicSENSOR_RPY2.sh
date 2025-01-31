#!/bin/bash

lxterminal --command "sudo nice -n -20 /home/pi/.pyenv/versions/3.6.6/bin/python /home/pi/OHSU_ANKLE/Kinematic/main1.py" &
lxterminal --command "sudo nice -n -20 /home/pi/.pyenv/versions/3.6.6/bin/python /home/pi/OHSU_ANKLE/Kinematic/readeulercallable.py"

read -n 1
