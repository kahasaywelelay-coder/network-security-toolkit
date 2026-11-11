#!/bin/bash

# Check for correct argument count
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <Target-IP> <NSE-Script-Name>"
    echo "Example: $0 192.168.1.1 http-title"
    exit 1
fi

TARGET=$1
SCRIPT=$2

echo "[*] Running Nmap NSE script '$SCRIPT' against $TARGET..."
nmap --script "$SCRIPT" "$TARGET"