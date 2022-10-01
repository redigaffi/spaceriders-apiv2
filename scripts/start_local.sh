#!/bin/bash

cd src
$(poetry env info -p)/bin/python3 -m uvicorn apps.http:app --reload --port 8010
