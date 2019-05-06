#!/usr/bin/env bash

set -e

# Enter the application's directory
cd /home/ubuntu/neargreen-v2

# Tear down the server
docker-compose -f docker-compose.prod.yml down

# Rebuild the server
docker-compose -f docker-compose.prod.yml build

# Restart the server
docker-compose -f docker-compose.prod.yml up -d