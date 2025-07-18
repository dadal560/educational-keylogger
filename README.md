# Educational Keylogger (Python)  
> Un projet open-source **à but purement éducatif** illustrant le fonctionnement d’un keylogger basique sous Linux ou Windows.

## Avertissement légal et éthique

> Ce projet est conçu **uniquement à des fins pédagogiques et de recherche**.  
> **N’exécutez jamais ce programme sur un système qui n’est pas le vôtre ou sans autorisation explicite**.  
> Testez-le **uniquement dans un environnement virtualisé (machine virtuelle ou sandbox)**.

L’auteur **décline toute responsabilité** en cas d’usage inapproprié ou malveillant de ce code.

---

## Objectifs pédagogiques

- Comprendre comment intercepter les frappes clavier avec Python.
- Étudier la structure d’un outil de type keylogger.
- Expérimenter l’empaquetage d’un script Python en exécutable.

---

## Fonctionnement

Le keylogger utilise la bibliothèque [`pynput`](https://pynput.readthedocs.io/) pour écouter les frappes clavier en arrière-plan et les enregistrer dans un fichier texte local dans un dossier `keylogs/`.

### Exemple de log :
hello world<space>!<enter>

yaml
Copier
Modifier

---

## Arborescence du projet

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

