#!/bin/bash

cd src
$(poetry env info -p)/bin/python3 -m uvicorn apps.websockets:app --reload --port 8011
