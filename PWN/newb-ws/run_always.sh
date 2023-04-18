#!/usr/bin/env sh

# If the application crashes, this script will restart it.
while true; do
    ./build/httpd 80
    sleep 1
done
