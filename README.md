# QBE

# Project Setup Guide

## Prerequisites:

These instructions were prepared on the following environment:
- Debian based Linux OS 8.3.0-6 and higher (64 bit)
- Python 3.10

## Initial Setup:

### Python Virtual Environment

To keep the dependencies for this project isolated from others, I recommend setting up a Python Virtual Environment using the following steps:

1. Run the following command, replacing `<env_name>` with the name you want for your virtual environment:
   ```bash
   python -m venv <env_name>
   ```
2. Run the following command to activate your virtual environment:
   ```bash
   source <env_name>/bin/activate
   ```

Now you can install packages using pip; they will be isolated to the virtual environment.

## Install Required Dependencies:

```bash
pip install fastapi
pip install uvicorn
pip install requests
```

## Running the Unit Tests:

1. Run the following command in the terminal in your Python Virtual Environment to get Uvicorn to start the ASGI server:
   ```bash
   uvicorn project:app --reload
   ```

2. In a separate terminal, navigate to your Python virtual environment. Run the following to execute the unit tests:
   ```bash
   python3 validateunit.py
   python3 getfactorsunit.py
   ```

While the tests are running, you can monitor the server terminal to see what payloads are being sent to the server and what actions are being taken.
```
