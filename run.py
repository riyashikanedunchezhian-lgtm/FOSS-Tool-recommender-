import os
import webbrowser
import time
import threading

def load_data():
    os.system("python load_data.py")

def start_backend():
    os.system("uvicorn app:app --reload")

def open_browser():
    time.sleep(3)
    webbrowser.open("http://127.0.0.1:8000")

# Run steps
load_data()
threading.Thread(target=start_backend).start()
open_browser()