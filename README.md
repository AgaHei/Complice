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
        ├── start.sh                    # Script de lancement du conteneur Docker
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

1. Installez Docker sur votre machine.
2. Clonez le dépôt :
      ```bash
   git clone https://github.com/AgaHei/Complice.git
   cd Complice
3. Créez un fichier .env à la racine (OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)
4. Lancez le conteneur :
    bash start.sh
5. Ouvrez JupyterLab dans votre navigateur : http://localhost:8888 Utilisez le token affiché dans le terminal pour vous connecter.

📘 Les notebooks principaux :

03_embeddings.ipynb → génération des vecteurs

04_indexation_faiss.ipynb → création du vectorstore

05_rag_pipeline.ipynb → requêtes RAG + validation

📚 Extraction optionnelle : Si vous souhaitez enrichir la base documentaire avec de nouveaux PDF :

01_extraction.ipynb → extraction des textes

02_chunking_metadata.ipynb → découpage + annotation


# Lancer l'application (*à suivre)
streamlit run app/main.py

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


