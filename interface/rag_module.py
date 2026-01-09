# rag_module.py

import os
import pickle
import faiss
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain.schema import Document  

# 🔐 Charger la clé API depuis .env (dossier parent)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
env_path = os.path.join(parent_dir, ".env")
load_dotenv(env_path)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Vérification de la clé API
if not openai_api_key:
    raise ValueError("❌ Clé OPENAI_API_KEY non trouvée. Vérifiez votre fichier .env")

# 🔧 Chargement du vectordb avec cache Streamlit - OPTIMISÉ ⚡
@st.cache_resource
def load_vector_db():
    """Charge la base vectorielle FAISS créée par les notebooks - VERSION CACHÉE"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        
        # Chemins vers les nouveaux fichiers créés par le notebook 04
        index_path = os.path.join(parent_dir, "data", "faiss_index_openai.index")
        metadata_path = os.path.join(parent_dir, "data", "faiss_metadata_openai.pkl")
        
        # Vérifier que les fichiers existent
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Index FAISS non trouvé: {index_path}")
        if not os.path.exists(metadata_path):
            raise FileNotFoundError(f"Métadonnées non trouvées: {metadata_path}")
        
        print("🚀 Chargement initial du vectorstore (une seule fois)...")
        
        # Charger l'index FAISS directement
        faiss_index = faiss.read_index(index_path)
        
        # Charger les métadonnées
        with open(metadata_path, 'rb') as f:
            metadata = pickle.load(f)
        
        documents = metadata['documents']
        
        # Créer les objets Document pour LangChain
        langchain_docs = [
            Document(page_content=doc, metadata={"index": i}) 
            for i, doc in enumerate(documents)
        ]
        
        # Créer le modèle d'embedding OpenAI (sera aussi caché)
        embeddings_model = get_embeddings_model()
        
        # 🎯 OPTIMISATION: Utiliser l'index FAISS existant au lieu de recalculer
        # Créer le vectorstore avec l'index déjà calculé
        vectorstore = FAISS.from_documents(
            documents=langchain_docs,
            embedding=embeddings_model
        )
        
        print("✅ Vectorstore chargé et mis en cache !")
        return vectorstore
        
    except Exception as e:
        print(f"❌ Erreur lors du chargement de FAISS: {e}")
        raise

# 🧠 Modèle d'embeddings caché
@st.cache_resource
def get_embeddings_model():
    """Modèle d'embedding OpenAI mis en cache"""
    return OpenAIEmbeddings(
        api_key=openai_api_key,
        model="text-embedding-3-small"
    )

# 🤖 Modèle LLM caché
@st.cache_resource
def get_llm():
    """Modèle ChatGPT mis en cache"""
    return ChatOpenAI(
        api_key=openai_api_key,
        model="gpt-4o",
        temperature=0.7
    )

# 🧠 Pipeline RAG optimisé (OBSOLÈTE - remplacé par les fonctions cachées)
# Cette fonction n'est plus utilisée grâce aux optimisations de cache

# 💬 Fonction d'interrogation OPTIMISÉE avec cache ⚡
def query_rag(question: str, mode: str = "dialogue") -> str:
    """Interroge le système RAG - VERSION RAPIDE avec modèles cachés"""
    try:
        # 🚀 Utiliser les modèles cachés (chargés une seule fois)
        db = load_vector_db()  # Cache Streamlit
        llm = get_llm()       # Cache Streamlit
        
        # Récupérer les documents pertinents
        docs = db.similarity_search(question, k=3)

        # 🎯 Prompt système bienveillant avec contexte explicite
        if mode == "emotion":
            system_prompt = (
                "Tu es Complice, un guide émotionnel doux et rassurant spécialisé dans l'autisme. "
                "Tu t'adresses à des adolescents autistes avec empathie et clarté. "
                "IMPORTANT: Base ta réponse sur les documents fournis qui contiennent des informations sur l'autisme. "
                "CRUCIAL: NE mentionne JAMAIS de prénoms, noms ou situations personnelles spécifiques des documents. "
                "Généralise les conseils et témoignages sans citer d'exemples individuels. "
                "Utilise un ton chaleureux, encourageant, et ajoute des emojis doux pour rythmer la réponse."
            )
        else:
            system_prompt = (
                "Tu es Complice, un compagnon bienveillant spécialisé dans l'accompagnement des adolescents autistes. "
                "IMPORTANT: Base ta réponse principalement sur les extraits de documents fournis qui parlent d'autisme et de neurodiversité. "
                "CRUCIAL: NE mentionne JAMAIS de prénoms, noms ou situations personnelles spécifiques des documents. "
                "Transforme les témoignages individuels en conseils généralisés. Évite les citations directes avec des détails personnels. "
                "Tu valorises les émotions, tu rassures, et tu évites les formulations trop techniques. "
                "Ajoute des emojis doux pour rendre la réponse plus accessible."
            )

        # 🧠 Créer le contexte à partir des documents trouvés
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Prompt complet avec contexte explicite
        full_prompt = f"""{system_prompt}

CONTEXTE DOCUMENTAIRE:
{context}

QUESTION: {question}

Réponds en te basant sur les informations du contexte documentaire ci-dessus. 
RAPPEL IMPORTANT: Ne mentionne aucun prénom, nom ou situation personnelle spécifique du contexte. 
Généralise les conseils en gardant uniquement les informations utiles et applicables."""

        # Utiliser le LLM caché (déjà initialisé)
        response = llm.invoke([{"role": "user", "content": full_prompt}])
        
        return response.content

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"❌ Erreur détaillée: {error_details}")
        return f"❌ Erreur: {type(e).__name__}: {str(e)}. Détails: {error_details}. Vérifie que FAISS est bien chargé et que ta clé OpenAI est configurée."