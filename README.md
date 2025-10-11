# 🤗 COMPLICE : Assistant Multimodal Bienveillant pour Jeunes Autistes

## Complice — Un compagnon pour comprendre, ressentir et prendre confiance


Ce projet vise à créer un assistant conversationnel intelligent en combinant les modules suivants:

- 💬 **Chat bienveillant** : Dialogue rassurant, adapté au niveau de compréhension; l'utilisateur peut poser des questions sur l'autisme, les émotions, les relations sociales…
- 🌈 **Exploration émotionnelle** : Exploration des émotions avec génération d'images de visages exprimant des émotions (joie, colère, tristesse, etc.)
- 🧩 **Quiz interactifs sur les  habiletés sociales** : 30 scénarios d'apprentissage pour développer les habiletés sociales
- 🛡️ **Sécurité & éthique** : Filtrage des réponses, personnalisation du ton et du niveau de difficulté intelligent, combinant :

## 🧠 Objectif du projet

L’objectif est de proposer un outil accessible, rassurant et éducatif pour les jeunes autistes en quête de compréhension et d’autonomie.

🧑‍🏫 Ce projet est réalisé dans le cadre de la formation Data Science Full Stack chez JEDHA comme le projet final pour la certification de "Concepteur Développeur en Science de Données".

## ✅ **Fonctionnalités réalisées et opérationnelles**

- 🔍 **Recherche intelligente** : RAG basé sur une bibliothèque documentaire sur l'autisme, émotions et habiletés sociales avec chat empathique avec prompts contextualisés et accueil chaleureux
- 🌈 **Module exploration émotionnelle** : 
  - 30 émotions avec descriptions pédagogiques
  - Génération d'images DALL-E personnalisées (âge, lieu, moment de la journée)
  - Sélecteur de personnage inclusif ("personne à visualiser")
  - Discussion empathique sur les émotions ressenties
  - Génération DALL-E 3 avec paramètres personnalisables
- 🧩 **Module Quiz interactifs** : 
  - 30 scénarios d'apprentissage pour développer les habiletés sociales
  - Discussion empathique sur les choix des réponses
- 🛡️ **Sécurité & éthique** : Prompts bienveillants, ton adapté aux adolescents autistes

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
        ├── data/                   # Textes extraits, chunks, embeddings, index FAISS
        │   ├── pdf_books/          # (non versionné) PDF sources originaux
        │   ├── extracted_texts/    # (non versionné) textes extraits
        │   ├── ready_for_embedding/  # chunks, chunks avec metadonnées    
        │   └── embeddings/           # fichiers .npy, .pkl, .idx, vectorstore FAISS
        ├── notebooks/              # Notebooks 01 à 05 (pipeline RAG)
        │   ├── 01_extraction.ipynb         # extraction des textes
        │   ├── 02_chunking_metadata.ipynb  # découpage + annotation
        │   ├── 03_embeddings.ipynb         # génération des vecteurs
        │   ├── 04_indexation_faiss.ipynb   # création du vectorstore (.faiss + .pkl)   
        │   ├── 05_rag_pipeline.ipynb       # requêtes RAG avec GPT-4o
        │   ├── 06_validation_rag.ipynb     # boucle de questions test et évaluation RAGAS
        │   ├── 07_generate_quiz.ipynb      # génération automatisée de quiz avec GPT-4o
        │   └── generated_quizzes/           # Données des quiz (scénarios sociaux)
        ├── interface/                      # Interface Streamlit complète et fonctionnelle
        │   ├── app.py                      # Interface principale avec 4 modules complets
        │   ├── rag_module.py               # Pipeline RAG avec prompts bienveillants
        │   ├── image_module.py             # Génération d'images DALL-E personnalisées
        │   ├── quiz_module.py              # Système de quiz interactifs pour habiletés sociales
        │   ├── data/                       # Données des quiz (30 scenarios d'apprentissage)
        │   └── └── quiz_complets_melanges_corriges.json
        │
        ├── .gitignore                   # Fichiers à exclure du suivi Git
        ├── .dockerignore               # Fichiers à exclure du conteneur Docker
        ├── Dockerfile                  # Image Docker pour environnement Jupyter
        ├── docker-compose.yml          # Orchestrateur Docker (JupyterLab + Streamlit + volumes)
        ├── requirements.txt            # Dépendances Python du projet
        ├── GUIDE_COEQUIPIERS.md        # Explication concernant le démarrage du conteneur
        └── README.md                   # Présentation et documentation du projet


---

### 🔧 Technologies utilisées

#### 📚 Extraction & préparation des données
- PyMuPDF, pdfminer.six : extraction de texte depuis PDF
- pandas, numpy, tqdm : manipulation et nettoyage des données

#### 🧠 Recherche sémantique & génération
- LangChain : orchestration du pipeline RAG avec langchain-openai
- FAISS : base vectorielle pour la recherche (6,346 documents indexés)
- OpenAI text-embedding-3-small : embeddings haute qualité multilingues (1536 dimensions)
- OpenAI GPT-4o : génération de réponses bienveillantes avec prompts contextualisés
- OpenAI DALL-E 3 : génération d'images émotionnelles personnalisées

#### 🧪 Validation & évaluation
- RAGAS : évaluation de la pertinence, fidélité et bienveillance des réponses

#### 💻 Interface & expérience utilisateur 
- Jupyter Notebook : environnement de développement
- Streamlit : interface utilisateur interactive **opérationnelle en local**
- Interface modulaire avec une page d'accueil, un dialogue bienveillant, une exploration émotionnelle et des quiz pour s'entraîner en habiletés sociales

#### 🐳 Déploiement & portabilité
- Docker : conteneurisation pour faciliter l’installation
- python-dotenv : gestion sécurisée des clés API

#### 🤝 Collaboration & versioning
- Git / GitHub : gestion du code en équipe

---

## 📚 Sources documentaires

Les textes utilisés sont des ouvrages éducatifs sur l’autisme, l’adolescence et les habiletés sociales. Tous les documents sont légalement accessibles et utilisés dans un cadre non-commercial et pédagogique.

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

    Créez un fichier .env à la racine avec votre clé API OpenAI :

    env     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            # Utilisé pour GPT-4o, DALL-E 3 et les embeddings

3. Lancez l'environnement de développement :

bash   docker-compose up --build

4. Accédez à JupyterLab :

Ouvrez votre navigateur sur : http://localhost:8888

🎉 Pas de token requis en mode développement !


5. Arrêter l'environnement :

bash   # Appuyez sur Ctrl+C dans le terminal, puis :
        docker-compose down



# 🚀 Interface Streamlit (opérationnelle en local)

## Lancer l'interface Complice en local

1. **Navigation vers le dossier interface** :
```bash
cd interface
```

2. **Activation de l'environnement virtuel** :
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac  
source venv/bin/activate
```

3. **Lancement de Streamlit** :
```bash
streamlit run app.py
```

4. **Accès à l'interface** :
- **Local** : http://localhost:8501
- **Réseau** : http://[votre-ip]:8501

> ⚠️ **Important** : Assurez-vous d'avoir configuré votre clé OpenAI dans le fichier `.env` à la racine du projet

## 🎉 Fonctionnalités disponibles

### � Module "À propos"
- Présentation de Complice et de sa mission
- Informations sur l'équipe et les objectifs pédagogiques
- Guide d'utilisation des différents modules

### �💬 Module "Discuter avec Complice"
- Message d'accueil bienveillant
- Chat empathique avec RAG contextuel
- Prompts adaptés aux adolescents autistes

### 🌈 Module "Explorer les émotions avec Complice"  
- Sélection parmi 30 émotions avec descriptions
- Paramétrage personnalisé :
  - 🎂 Âge (5-80 ans)
  - 📍 Lieu (école, parc, plage, etc.)
  - 🕐 Moment (matin, midi, soir, nuit)
  - 👦👧 Personnage inclusif
- Génération d'images DALL-E 3 contextualisées
- Discussion empathique sur l'émotion explorée

### 🎯 Module "Quiz habiletés sociales avec Complice"
- **30 scénarios d'apprentissage** couvrant diverses situations sociales :
  - 🏫 Situations scolaires (interactions en classe, récréation, cantine)
  - 👨‍👩‍👧‍👦 Contextes familiaux (repas, sorties, discussions)
  - 🎭 Interactions sociales (amitié, conflits, événements)
  - 🌍 Situations publiques (transports, commerces, loisirs)
- **Questions à choix multiples** avec 3 options par scénario
- **Feedback constructif** : explications bienveillantes pour chaque réponse
- **Apprentissage progressif** : découverte de nouvelles stratégies sociales
- **Interface intuitive** : navigation simple et encourageante

---
## 🤝 Contribuer

Les coéquipiers peuvent :

- Ajouter de nouveaux textes sources (PDF éducatifs, guides, etc.)
- Proposer des améliorations aux prompts pour plus de nuance
- Tester des variantes de modèles (GPT-3.5, GPT-4o, Mistral…)
- Enrichir l'interface utilisateur Streamlit (nouvelles fonctionnalités, design)
- Ajouter des filtres thématiques ou des scores de pertinence
- Améliorer le pipeline RAG et l'évaluation RAGAS

### 🧪 Bonnes pratiques

- Documenter chaque étape dans les notebooks
- Utiliser des noms de fichiers explicites et versionnés
- Respecter la philosophie de *Complice* : bienveillance, clarté, inclusion
- Ne jamais exposer de clé API dans le code ou les notebooks


