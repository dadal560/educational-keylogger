import os
from datetime import datetime

# 1. Détermine le dossier où seront stockés les logs
LOG_DIR = os.path.join(os.path.expanduser("~"), "keylogs")

# 2. Crée un nom de fichier avec la date/heure actuelle
FILENAME = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# 3. Chemin complet du fichier de log
LOG_FILE = os.path.join(LOG_DIR, FILENAME)
