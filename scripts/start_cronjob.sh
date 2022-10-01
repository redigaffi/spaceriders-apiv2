#!/bin/bash

cd src
$(poetry env info -p)/bin/python3 -m apps.cronjobs.__init__
