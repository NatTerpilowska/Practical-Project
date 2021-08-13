#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:


ssh swarm-manager <<EOF
  export DATABASE=$DATABASE_URI
  docker stack deploy --compose-file docker-compose.yaml character
EOF