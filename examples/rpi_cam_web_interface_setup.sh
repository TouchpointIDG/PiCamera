#!/bin/bash

sudo apt update
sudo apt install -y git

git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
cd RPi_Cam_Web_Interface
sudo ./install.sh
