#!/usr/bin/env bash

# This is the setup script for the project. It will install all the necessary
# dependencies and set up the project for development.

# update the system.
sudo apt-get update
sudo apt-get -y upgrade

# install python3 and pip3.
sudo apt-get install -y python3 python3-pip

# install the required python packages.
pip3 install -r requirements.txt

# install sql-server.
sudo apt-get install -y mysql-server

# start the sql-server.
sudo systemctl start mysql

# setup the database.
cat api.sql | sudo mysql

# insert data in the db
./script.py

