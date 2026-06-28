#!/bin/bash

echo "Downloading assets..."
python download_assets.py

echo "Listing assets..."
find assets -maxdepth 4

echo "Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT