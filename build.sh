#!/bin/bash

rm -rf bin
mkdir bin
cp src/dbmigrate.py bin/dbmigrate
chmod +x bin/dbmigrate
