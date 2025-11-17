#!/bin/bash
# Production start script for frontend

echo "Building and serving SME Growth Predictor Frontend (Production)"
echo "==============================================================="

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm ci
fi

# Build the application
echo "Building application..."
npm run build

# Serve the built application
echo "Starting production server..."
npx serve -s dist -l ${PORT:-3000}
