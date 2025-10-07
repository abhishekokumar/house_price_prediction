#!/bin/bash
# Start Flask in background
python Server/server.py &

# give Flask a few seconds to start
sleep 2

# Start nginx in foreground
nginx -g "daemon off;"
