#!/usr/bin/env bash

set -e

# Enter the application's directory
cd /home/ubuntu/neargreen-v2

# Rebuild and restart the server
sudo docker-compose -f docker-compose.prod.yml up -d --build