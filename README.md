# 🤖 COMPLICE Assistant Multimodal Bienveillant pour Jeunes Autistes

Complice — Un compagnon pour comprendre, ressentir et prendre confiance

## 🧠 Objectif du projet

Ce projet vise à créer un assistant conversationnel intelligent, combinant :
- 🔍 Recherche sémantique dans une base documentaire sur l’autisme
- 💬 Dialogue bienveillant pour s’exercer aux habiletés sociales
- 🖼️ Génération d’images de visages exprimant des émotions pour l’apprentissage émotionnel

L’objectif est de proposer un outil accessible, rassurant et éducatif pour les jeunes autistes en quête de compréhension et d’autonomie.

🧑‍🏫 Ce projet est réalisé dans le cadre de la formation Data Science Full Stack chez JEDHA comme le projet final pour la certification de "Concepteur Développeur en Science de Données".

---

## 👥 Équipe

    | Prénom    | Rôle principal                     |Contributions                                            |
    |--------   |----------------                    |----------------                                         |
    | Léa       | Extraction & annotation des données| PDF → texte, chunking, métadonnées, prompts émotionnels |
    | Alisson   | Embeddings & base vectorielle      | Choix du modèle, FAISS, intégration LangChain           |
    | Agnès     | LLM & génération de réponses       | API LLM, prompts bienveillants, validation UX           |
    | Ludo      | Interface & sécurité               | Streamlit, intégration image, filtres de contenu        |

---

## 🗂️ Structure du projet

    complice/
        ├── data/                  # Textes extraits, chunks, embeddings, index FAISS
        │   ├── pdf_books/          # (non versionné) PDF sources originaux
        │   ├── extracted_texts/   # (non versionné) textes extraits
        │   ├── ready_for_embedding/  # chunks, chunks avec metadonnées    
        │   └── embeddings/         # fichiers .npy, .pkl, .idx
        ├── notebooks/             # Notebooks 01 à 05 (pipeline RAG)
        │   ├── 01_extraction.ipynb # extraction des textes
        │   ├── 02_chunking_metadata.ipynb # découpage + annotation
        │   ├── 03_embeddings.ipynb # génération des vecteurs
        │   ├── 04_indexation_faiss.ipynb # création du vectorstore (.faiss + .pkl)   
        │   ├── 05_rag_pipeline.ipynb # requêtes RAG avec GPT-4o
        │   └── 06_validation_rag.ipynb # boucle de questions test et évaluation RAGAS
        │
        ├── .gitignore                   # Fichiers à exclure du suivi Git
        ├── .dockerignore               # Fichiers à exclure du conteneur Docker
        ├── Dockerfile                  # Image Docker pour environnement Jupyter
        ├── requirements.txt            # Dépendances Python du projet
        └── README.md                   # Présentation et documentation du projet


---

### 🔧 Technologies utilisées

#### 📚 Extraction & préparation des données
- PyMuPDF, pdfminer.six : extraction de texte depuis PDF
- pandas, numpy, tqdm : manipulation et nettoyage des données

#### 🧠 Recherche sémantique & génération
- LangChain : orchestration du pipeline RAG
- FAISS : base vectorielle pour la recherche
- sentence-transformers : embeddings multilingues
- OpenAI API : génération de réponses bienveillantes

#### 🧪 Validation & évaluation
- RAGAS : évaluation de la pertinence, fidélité et bienveillance des réponses

#### 💻 Interface & expérience utilisateur
- Jupyter Notebook : environnement de développement
- Streamlit / Gradio (*à suivre) : interface utilisateur interactive

#### 🐳 Déploiement & portabilité
- Docker : conteneurisation pour faciliter l’installation
- python-dotenv : gestion sécurisée des clés API

#### 🤝 Collaboration & versioning
- Git / GitHub : gestion du code en équipe


---

## 📚 Sources documentaires

Les textes utilisés sont des ouvrages éducatifs sur l’autisme, l’adolescence et les habiletés sociales. Tous les documents sont légalement accessibles et utilisés dans un cadre non-commercial et pédagogique.

---

## 🧪 Fonctionnalités principales

- 🔍 **Recherche intelligente** : L’utilisateur peut poser des questions sur l’autisme, les émotions, les relations sociales…
- 💬 **Chat bienveillant** : Dialogue rassurant, adapté au niveau de compréhension
- 🖼️ **Images émotionnelles** : Génération de visages exprimant des émotions (joie, colère, tristesse, etc.)
- 🛡️ **Sécurité & éthique** : Filtrage des réponses, personnalisation du ton et du niveau de difficulté

---

## 📅 Planning de réalisation

| Semaine | Objectifs |
|--------|-----------|
| Semaine 1 | Extraction des données + cadrage technique |
| Semaine 2 | Construction du pipeline RAG |
| Semaine 3 | Génération d’images + interface |
| Semaine 4 | Finalisation + documentation + soutenance |

---
## 🐳 Lancer le projet avec Docker

Prérequis:

- Docker installé sur votre machine
- Docker Compose (inclus avec Docker Desktop)

# Installation et lancement

1. Clonez le dépôt :

    bash   git clone https://github.com/AgaHei/Complice.git
        cd Complice

2. Configurez l'environnement :

    Créez un fichier .env à la racine avec vos clés API :

    env     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            REPLICATE_API_TOKEN=your_replicate_token (optionnel, pour la génération d'images)

3. Lancez l'environnement de développement :

bash   docker-compose up --build

4. Accédez à JupyterLab :

Ouvrez votre navigateur sur : http://localhost:8888

🎉 Pas de token requis en mode développement !


5. Arrêter l'environnement :

bash   # Appuyez sur Ctrl+C dans le terminal, puis :
        docker-compose down

# 📘 Notebooks principaux

Une fois JupyterLab ouvert, explorez les notebooks dans l'ordre :

    - 03_embeddings.ipynb🔤 Génération des vecteurs d'embedding
    - 04_indexation_faiss.ipynb🗃️ Création du vectorstore FAISS
    - 05_rag_pipeline.ipynb🤖 Pipeline RAG

📚 Enrichissement de la base documentaire (optionnel)

Pour ajouter de nouveaux documents PDF à la base de connaissances :
    - 01_extraction.ipynb📄 Extraction de texte depuis les PDF
    - 02_chunking_metadata.ipynb✂️ Découpage et annotation des documents

🛠️ Commandes utiles
bash# Reconstruire après modification du Dockerfile/requirements

docker-compose up --build --force-recreate

# Lancer en arrière-plan
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Accéder au shell du conteneur (debug)
docker-compose exec jupyter-dev bash

# Installer un nouveau package temporairement
docker-compose exec jupyter-dev pip install nom-du-package

# 🚀 Interface Streamlit (à venir)
L'interface utilisateur sera accessible sur http://localhost:8501 une fois développée.

🐛 Problèmes courants
Docker n'arrive pas à se connecter ?

Vérifiez que Docker Desktop est lancé
Sur Windows : redémarrez Docker Desktop

Erreur de permissions ?

bash# Sur Linux/Mac, ajoutez votre utilisateur au groupe docker :
sudo usermod -aG docker $USER
Puis redémarrez votre session

Port 8888 déjà utilisé ?
bash# Modifiez le port dans docker-compose.yml :
ports:
  - "8889:8888"  # Utilisez 8889 à la place

---
## 🤝 Contribuer

Les coéquipiers peuvent :

- Ajouter de nouveaux textes sources (PDF éducatifs, guides, etc.)
- Proposer des améliorations aux prompts pour plus de nuance
- Tester des variantes de modèles (GPT-3.5, GPT-4o, Mistral…)
- Créer une interface utilisateur (Streamlit, Gradio)
- Ajouter des filtres thématiques ou des scores de pertinence

### 🧪 Bonnes pratiques

- Documenter chaque étape dans les notebooks
- Utiliser des noms de fichiers explicites et versionnés
- Respecter la philosophie de *Complice* : bienveillance, clarté, inclusion
- Ne jamais exposer de clé API dans le code ou les notebooks


