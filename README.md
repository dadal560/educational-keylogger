# 🛡️ Educational Keylogger (Python)  
> Un projet open-source **à but purement éducatif**, illustrant le fonctionnement d’un keylogger basique sous Linux ou Windows.

## ⚠️ Avertissement légal et éthique

> Ce projet est conçu **uniquement à des fins pédagogiques et de recherche**.  
> **N’exécutez jamais ce programme sur un système qui n’est pas le vôtre ou sans autorisation explicite**.  
> Testez-le **uniquement dans un environnement virtualisé (machine virtuelle ou sandbox)**.

L’auteur **décline toute responsabilité** en cas d’usage inapproprié ou malveillant de ce code.

---

## 🎯 Objectifs pédagogiques

- Comprendre comment intercepter les frappes clavier avec Python.
- Étudier la structure d’un outil de type keylogger.
- Expérimenter l’empaquetage d’un script Python en exécutable.

---

## 🧠 Fonctionnement

Le keylogger utilise la bibliothèque [`pynput`](https://pynput.readthedocs.io/) pour écouter les frappes clavier en arrière-plan et les enregistrer dans un fichier texte local, dans un dossier `keylogs/`.

### Exemple de log :
hello world<space>!<enter>

yaml
Copier
Modifier

---

## 🗂️ Arborescence du projet

educational-keylogger/
│
├── keylogger/
│ ├── init.py
│ ├── logger.py # Contient la logique d'écoute clavier
│ └── config.py # Définit le chemin des logs
│
├── dist/
│ └── main.exe # (optionnel) version exécutable compilée via PyInstaller
│
├── main.py # Point d’entrée
├── requirements.txt # Dépendances Python
├── .gitignore
└── README.md # Ce fichier

yaml
Copier
Modifier

---

## 🚀 Utilisation

### 1. Cloner le dépôt

```bash
git clone https://github.com/dadal560/educational-keylogger.git
cd educational-keylogger
2. Créer un environnement virtuel
bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
3. Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
4. Lancer le keylogger (⚠️ dans une VM !)
bash
Copier
Modifier
python main.py
Appuie sur Ctrl+C pour l'arrêter. Les logs seront enregistrés dans le dossier keylogs/.

🏗️ Créer un exécutable .exe (Windows)
Si tu veux créer un exécutable portable :

bash
Copier
Modifier
pip install pyinstaller
pyinstaller --onefile main.py
L'exécutable sera généré dans dist/main.exe.

📜 Licence
Ce projet est distribué sous licence MIT.
Voir le fichier LICENSE pour plus d'informations.

🙋‍♂️ Auteur
Projet réalisé par @dadal560 pour expérimenter la cybersécurité offensive de manière contrôlée.

🧪 Pour aller plus loin
Ajout d’une touche secrète pour arrêter l’écoute proprement

Interface graphique minimale avec Tkinter ou PyQt

Envoi automatique des logs (dans un environnement 100% isolé)

Analyse de la charge CPU / RAM via psutil
