#! /bin/bash
sudo apt-get update
sudo apt-get remove postgresql
sudo apt-get install -y postgresql
# To set the password for postgres, type 
sudo passwd postgres

# To conntect to postgres, type 
sudo -u postgres psql
######## OR
# You should get a prompt asking for your password. If this doesn’t work, then you can try the second option listed below.
# Switch users to postgres by typing 
su - postgres
# Type 
psql

CREATE DATABASE myproject;

CREATE USER <db_username> WITH PASSWORD '(password)';
