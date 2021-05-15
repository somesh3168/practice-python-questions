#! /bin/bash
#source:= https://www.scaleway.com/en/docs/install-and-secure-mongodb-on-ubuntu/
sudo apt-get update
sudo apt-get upgrade
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install mongodb-org
sudo systemctl start mongod
or
sudo service mongod status/start

# 4 . Ensure that it restarts automatically at each boot

sudo systemctl enable mongod

# then 
mongo
#check ports
nmap -p- localhost
#  add documents
# https://zellwk.com/blog/local-mongodb/

