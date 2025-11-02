#!/bin/bash

# Colors
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}============================================================"
echo "   🚀 Droidify Redirector - Starting Server..."
echo -e "============================================================${NC}"
echo

python3 server.py

if [ $? -ne 0 ]; then
    echo
    echo "❌ Error: Python not found or server failed to start!"
    echo "💡 Make sure Python 3 is installed"
    echo
    exit 1
fi

