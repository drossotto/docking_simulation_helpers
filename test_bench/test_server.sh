#!/bin/sh

PORT=8000

while true; do
    nc -l -p $PORT -e /bin/cat
    sleep 4
    echo "Connection persisting..."
done