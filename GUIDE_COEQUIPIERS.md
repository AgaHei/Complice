# 🚀 Guide de démarrage Docker pour les coéquipiers

## Prérequis
- Docker Desktop installé et démarré
- Git installé
- Clé API OpenAI personnelle

## Étapes de lancement

### 1. Cloner le projet
```bash
git clone https://github.com/AgaHei/Complice.git
cd Complice
```

### 2. Configuration de la clé API OpenAI
Créer un fichier `.env` à la racine du projet avec votre clé API :
```env
OPENAI_API_KEY=sk-votre-clé-openai-ici
```

### 3. Lancement de l'environnement Docker

#### Option A : Commandes séparées (recommandé pour débuter)
```bash
# 1. Arrêter tout conteneur existant
docker-compose down

# 2. Construire l'image avec toutes les dépendances
docker-compose build

# 3. Démarrer l'environnement
docker-compose up
```

#### Option B : Commande unique (plus rapide)
```bash
docker-compose up --build
```

### 4. Accès aux services

#### JupyterLab (environnement de développement)
- **URL** : http://localhost:8888
- **Token** : Aucun requis (configuré sans mot de passe)

#### Interface Streamlit (dans Docker)
```bash
# Dans un nouveau terminal, pendant que Docker tourne :
docker exec -it complice-dev streamlit run /home/jovyan/work/interface/app.py --server.port 8501 --server.address 0.0.0.0
```
- **URL** : http://localhost:8501

⚠️ **IMPORTANT** : Si vous voyez "Port 8501 is already in use", arrêtez d'abord les processus :
```bash
docker exec -it complice-dev pkill -f streamlit
```

## 🔧 Commandes utiles

### Gestion des conteneurs
```bash
# Voir les conteneurs en cours
docker ps

# Arrêter l'environnement
docker-compose down

# Démarrer en arrière-plan (recommandé)
docker-compose up -d

# Reconstruire complètement (si problème)
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Accéder au terminal du conteneur
docker exec -it complice-dev bash

# Vérifier les logs du conteneur
docker logs complice-dev
```

### Installation de nouveaux packages (temporaire)
```bash
# Se connecter au conteneur
docker exec -it complice-dev bash

# Installer un package
pip install nom-du-package

# Pour une installation permanente, ajouter le package dans requirements.txt et reconstruire
```

## 🐛 Résolution de problèmes

### L'application ne s'affiche pas dans le navigateur
**Solution complète étape par étape :**
```bash
# 1. Vérifier que le conteneur tourne
docker ps

# 2. Si pas de conteneur, le démarrer
docker-compose up -d

# 3. Arrêter d'éventuels processus Streamlit en conflit
docker exec -it complice-dev pkill -f streamlit

# 4. Lancer l'application Streamlit
docker exec -it complice-dev streamlit run /home/jovyan/work/interface/app.py --server.port 8501 --server.address 0.0.0.0

# 5. Ouvrir http://localhost:8501 dans votre navigateur
```

### Port déjà utilisé
Si le port 8888 ou 8501 est occupé :
```bash
# Modifier dans docker-compose.yml :
ports:
  - "8889:8888"  # Utiliser 8889 au lieu de 8888
  - "8502:8501"  # Utiliser 8502 au lieu de 8501
```

### Problème de permissions (Linux/Mac)
```bash
sudo usermod -aG docker $USER
# Puis redémarrer la session
```

### Docker Desktop ne démarre pas
- Vérifier que la virtualisation est activée dans le BIOS
- Redémarrer Docker Desktop
- Sur Windows : vérifier que WSL2 est installé

### Timeout lors du build
```bash
# Réessayer avec une meilleure connexion ou :
docker-compose build --no-cache
```

## 📁 Structure du projet

```
Complice/
├── docker-compose.yml      # Configuration Docker
├── Dockerfile             # Image Jupyter avec toutes les dépendances
├── requirements.txt       # Packages Python du projet
├── .env                   # Clés API (À CRÉER)
├── notebooks/             # Notebooks 01 à 07
├── interface/             # Application Streamlit complète
│   ├── app.py            # Interface principale
│   ├── rag_module.py     # Pipeline RAG
│   ├── image_module.py   # Génération d'images
│   ├── quiz_module.py    # Système de quiz
│   └── data/             # 23 quiz interactifs
├── data/                 # Données RAG (embeddings, vectorstore)
└── README.md            # Documentation principale
```

## 🎯 Développement

### Pour contribuer au projet
1. Créer une branche : `git checkout -b ma-nouvelle-fonctionnalité`
2. Développer dans l'environnement Docker
3. Tester les modifications
4. Commit et push : `git add . && git commit -m "Description" && git push`
5. Créer une Pull Request sur GitHub

### Interface Streamlit locale (alternative à Docker)
```bash
cd interface
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r ../requirements.txt
streamlit run app.py
```

## ✅ Vérification du setup

### Test rapide
```bash
# Dans le conteneur Docker :
docker exec -it complice-dev python -c "
import openai
import streamlit as st
from sentence_transformers import SentenceTransformer
print('✅ Toutes les dépendances sont installées !')
"
```

### Test des quiz
```bash
# Test complet de tous les modules :
docker exec -it complice-dev python -c "
import sys
sys.path.append('/home/jovyan/work/interface')
from quiz_module import get_quiz_manager
from rag_module import load_vector_db
from image_module import generate_emotion_image
qm = get_quiz_manager()
print(f'✅ {qm.get_total_quizzes()} quiz chargés avec succès !')
print('✅ Tous les modules fonctionnent !')
"
```

### Commande de lancement rapide (tout-en-un)
```bash
# Commande complète pour démarrer l'application :
docker-compose up -d && docker exec -it complice-dev streamlit run /home/jovyan/work/interface/app.py --server.port 8501 --server.address 0.0.0.0
```

---

💡 **Conseil** : Gardez Docker Desktop ouvert pendant le développement et utilisez `docker-compose down` quand vous avez terminé pour libérer les ressources.