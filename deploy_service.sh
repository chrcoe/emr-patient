#!/bin/bash

systemctl stop emrapp.service
systemctl disable emrapp.service
cp emrapp.service /etc/systemd/system
systemctl enable emrapp.service
systemctl start emrapp.service
