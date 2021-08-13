#!/bin/bash

# Unit Testing
python3 -m pytest --ignore-glob=service_1/tests/test-se-1.py --cov --cov-config=.coveragerc

# Integration Testing
docker-compose up -d --build > /dev/null 2>&1 # silent
docker exec service_1 python3 -m pytest tests/test-se-1.py --color=yes