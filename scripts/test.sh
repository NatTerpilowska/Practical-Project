#!/bin/bash

# Unit Testing
python3 -m pytest --ignore-glob=service_1/tests/test_1.py --cov --cov-config=.coveragerc
python3 -m pytest --ignore-glob=service_2/tests/test_2.py --cov --cov-config=.coveragerc
python3 -m pytest --ignore-glob=service_3/tests/test_3.py --cov --cov-config=.coveragerc
python3 -m pytest --ignore-glob=service_4/tests/test_4.py --cov --cov-config=.coveragerc