#!/bin/bash

# Detect package manager
if command -v pnpm &> /dev/null; then
    PACKAGE_MANAGER="pnpm"
elif command -v yarn &> /dev/null; then
    PACKAGE_MANAGER="yarn"
else
    PACKAGE_MANAGER="npm"
fi

echo "Using package manager: $PACKAGE_MANAGER"

# Start FastAPI backend
echo "Starting FastAPI backend..."
cd api
python main.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start Next.js frontend
echo "Starting Next.js frontend..."
cd ..
$PACKAGE_MANAGER run dev &
FRONTEND_PID=$!

echo "Both services are starting..."
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo ""
echo "Backend will be available at: http://localhost:8000"
echo "Frontend will be available at: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both services"

# Wait for user to stop
wait 