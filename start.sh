#!/bin/bash
chmod +x start.sh
echo "Starting FastAPI on port $PORT"
gunicorn app.main:app \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:${PORT:-8000}