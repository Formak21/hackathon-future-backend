#!/bin/bash

cd ./src
waitress-serve --host 127.0.0.1 --port 8080 --call main:create_app
