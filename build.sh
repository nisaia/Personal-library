#!/bin/bash

GREEN="\e[32m"
END_COLOR="\e[0m"
venv='virtual_enviroment'

#CREATE VIRTUAL ENVIROMENT
echo -e "${GREEN}Creating virtual enviroment...${END_COLOR}"
sleep 3
python3 -m venv $venv
echo -e "${GREEN}$venv created.${END_COLOR}"

echo

#INSTALL DEPENDENCIES

echo -e "${GREEN}Installing dependencies...${END_COLOR}"
sleep 3
. $venv/bin/activate
echo -e "${GREEN}Upgrading pip command...${END_COLOR}"
python -m pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}All dependencies installed.${END_COLOR}"

echo

#CREATE DATABASE ENGINE

echo -e "${GREEN}Creating database engine...${END_COLOR}"
sleep 3
python3 -c "from database.db import create_database; create_database()"
echo -e "${GREEN}Database engine created.${END_COLOR}"