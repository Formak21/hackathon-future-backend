#!/bin/bash

waitress-serve --host 127.0.0.1 --port 8080 --call app:create_app
