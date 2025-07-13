#!/bin/bash

# Start backend in background
cd backend && python app.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
cd frontend && streamlit run app.py --server.port 10000 --server.address 0.0.0.0

# If frontend exits, kill backend
kill $BACKEND_PID 