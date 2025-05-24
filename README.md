# Server Monitor Web App

A simple web-based server monitor that displays real-time CPU and memory usage of your Linux server.

---

## Overview

This project uses a Python Flask backend to gather system stats with `psutil` and serves a minimal HTML page that fetches and displays this data every 2 seconds.

---

## Files

- `server.py` — Flask backend serving system data at `/api/system` and the frontend page.
- `static/index.html` — Frontend HTML page that shows CPU and memory usage.

---

## Requirements

- Python 3.x
- Flask
- psutil
    ```bash
    pip install flask psutil

---

## Setup & Run

1. Clone or download this project.

2. (Optional) Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Run the server:
    ```bash
    python3 server.py

4. Open your browser and visit:
    ```bash
    http://127.0.0.1:5000