# Educational Keylogger (Python)

> Un projet open-source **à but purement éducatif**, illustrant le fonctionnement d'un keylogger basique sous Linux et Windows.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Educational](https://img.shields.io/badge/Purpose-Educational-yellow.svg)]()

---

## Avertissement légal et éthique

> **ATTENTION** : Ce projet est conçu **uniquement à des fins pédagogiques et de recherche en cybersécurité**.

### Interdictions strictes :
- **Ne jamais exécuter** ce programme sur un système qui n'est pas le vôtre
- **Ne jamais utiliser** sans autorisation explicite écrite du propriétaire
- **Ne jamais déployer** à des fins malveillantes ou illégales

### Usages autorisés :
- Tests dans un **environnement virtualisé** (VM, sandbox)
- Recherche académique en cybersécurité
- Formation et éducation en sécurité informatique
- Démonstrations contrôlées

**L'auteur décline toute responsabilité** en cas d'usage inapproprié ou malveillant de ce code.

---


## Fonctionnement technique

Le keylogger utilise la bibliothèque [`pynput`](https://pynput.readthedocs.io/) pour :
- Écouter les événements clavier en arrière-plan
- Intercepter les frappes en temps réel
- Enregistrer les données dans un fichier texte local

---

## Structure du projet

```
educational-keylogger/
│
├── keylogger/
│   ├── logger.py           # Logique d'écoute clavier
│   ├── config.py           # Configuration et chemins
│
├── dist/                   # Exécutables compilés
│   └── main.exe           # (généré par PyInstaller)
│
│
├── main.py                 # Point d'entrée principal
├── requirements.txt        # Dépendances Python
├── .gitignore
├── LICENSE
└── README.md
```

---

## Installation et utilisation

### 1. Prérequis
- Python 3.8 ou supérieur
- Système d'exploitation : Linux, Windows, macOS
- Machine virtuelle recommandée pour les tests

### 2. Cloner le dépôt
```bash
git clone https://github.com/dadal560/educational-keylogger.git
cd educational-keylogger
```

### 3. Créer un environnement virtuel
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 5. Lancer le keylogger (dans une VM uniquement !)
```bash
python main.py
```

### 6. Arrêter le programme
- Appuyez sur `Ctrl+C` dans le terminal
- Ou utilisez la combinaison de touches configurée (par défaut : `Ctrl+Alt+Q`)

---

## Création d'un exécutable

### Windows (.exe)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### Linux (binaire)
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

L'exécutable sera généré dans le dossier `dist/`.

---

## Fonctionnalités

### Fonctionnalités actuelles :
- Capture des frappes clavier
- Enregistrement avec timestamp
- Support multi-plateforme
- Arrêt propre via combinaison de touches
- Gestion des touches spéciales

### Fonctionnalités prévues :
- Interface graphique simple
- Chiffrement des logs
- Analyse des patterns de frappe
- Rapport de sécurité automatique

---

## Aspects sécuritaires

### Détection et protection :
- **Antivirus** : Ce programme peut être détecté comme malveillant
- **Pare-feu** : Aucune connexion réseau n'est établie
- **Permissions** : Nécessite des privilèges d'écoute clavier

### Mesures de protection contre les keyloggers :
1. **Antivirus à jour** avec protection temps réel
2. **Clavier virtuel** pour les mots de passe sensibles
3. **Authentification à deux facteurs** (2FA)
4. **Surveillance des processus** système
5. **Chiffrement des données** sensibles

---

## Licence

Ce projet est distribué sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

---

## Auteur

**@dadal560** 

### Contact :
- Email : [gwen.henry56@gmail.com]
- GitHub : [@dadal560](https://github.com/dadal560)

---

## Liens utiles

- [Documentation Python](https://docs.python.org/)
- [Pynput Documentation](https://pynput.readthedocs.io/)
- [Cybersecurity Education](https://www.cybrary.it/)
- [Ethical Hacking Course](https://www.coursera.org/learn/ethical-hacking)

---

## Changelog

### Version 1.0.0 (2025-07-15)
- Première version fonctionnelle
- Support Linux/Windows
- Documentation complète
- Mesures de sécurité de base

---

**Rappel important** : Ce projet est uniquement à des fins éducatives. Utilisez-le de manière responsable et éthique dans le respect des lois en vigueur et avec l'autorisation appropriée.

## ⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !

