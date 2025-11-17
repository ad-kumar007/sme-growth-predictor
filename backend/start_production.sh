#!/bin/bash
# Production start script for backend

echo "Starting SME Growth Predictor Backend (Production)"
echo "=================================================="

# Load environment variables if .env exists
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Start uvicorn with production settings
uvicorn main:app \
    --host ${API_HOST:-0.0.0.0} \
    --port ${API_PORT:-8000} \
    --workers 4 \
    --log-level info \
    --no-access-log
