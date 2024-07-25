#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage : $0 <path/to/environment.yml> <path/to/requirements.txt>"
    exit 1
fi

ENV_YML=$1
OUTPUT_DIR=$2

if [ ! -f $ENV_YML ]; then
    echo "$ENV_YML does not exist"
    exit 1
fi

if [ ! -d $OUTPUT_DIR ]; then
    echo "$OUTPUT_DIR does not exist"
    exit 1
fi

REQUIREMENTS_TXT="$OUTPUT_DIR/requirements.txt"

awk '/^  - pip:/,/^  - /{if($0 !~ /^  - pip:/ && $0 !~ /^  - /) print $2}' "$ENV_YML" > "$REQUIREMENTS_TXT"

awk '/^  - pip:/,/^prefix:|dependencies:|^channels:/ {if($0 !~ /^  - pip:/ && $0 !~ /^prefix:|dependencies:|^channels:/ && $0 ~ /^    - /) print $2}' "$ENV_YML" >> "$REQUIREMENTS_TXT"

sed -i '/^$/d' "$REQUIREMENTS_TXT"

echo "requirements.txt created at $REQUIREMENTS_TXT"
exit 0

