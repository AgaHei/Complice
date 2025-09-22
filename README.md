# 🤖 COMPLICE Assistant Multimodal Bienveillant pour Jeunes Autistes

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

    📁 complice-assistant-autisme/ 
    ├── data/ # Textes extraits et annotés 
    ├── notebooks/ # Exploration, chunking, embeddings 
    ├── app/ # Backend FastAPI + frontend Streamlit 
    ├── prompts/ # Prompts LLM et image (Replicate) 
    ├── utils/ # Fonctions d’extraction, nettoyage, sécurité 
    ├── README.md # Ce fichier 
    └── requirements.txt # Dépendances Python


---

## 🔧 Technologies utilisées

- **LangChain / LlamaIndex** : Orchestration du pipeline RAG
- **FAISS / Qdrant** : Base vectorielle pour la recherche sémantique
- **OpenAI / Mistral API** : Génération de réponses bienveillantes
- **Replicate API** : Génération d’images émotionnelles
- **Streamlit / Gradio** : Interface utilisateur
- **PyMuPDF / pdfminer.six** : Extraction de texte depuis PDF
- **sentence-transformers** : Embeddings multilingues

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

## 🚀 Lancer le projet

```bash
# Cloner le repo
git clone https://github.com/AgaHei/Complice.git
cd complice

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app/main.py

---

##💬 Contact

