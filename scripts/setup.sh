#!/bin/bash

set -e

sudo apt-get update
sudo apt-get install curl jq -y

if [ -z "$(docker --version 2> /dev/null)" ]; then
   curl https://get.docker.com | sudo bash
   sudo usermod -aG docker $USER
fi

if [ -z "$(docker-compose --version 2> /dev/null)" ]; then
   version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | /latest | jq -r '.tag_name')
      sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi
