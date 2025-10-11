# rag_module.py

import os
import pickle
import faiss
import numpy as np
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

# 🔧 Chargement du vectordb avec les nouveaux fichiers OpenAI
def load_vector_db():
    """Charge la base vectorielle FAISS créée par les notebooks corrigés"""
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
        
        # Charger l'index FAISS
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
        
        # Créer le modèle d'embedding OpenAI
        embeddings_model = OpenAIEmbeddings(
            api_key=openai_api_key,
            model="text-embedding-3-small"
        )
        
        # Version production : utiliser tous les documents
        # Note : Cette ligne va générer les embeddings à la première utilisation
        # mais ils seront mis en cache par LangChain pour les utilisations suivantes
        # Création du vectorstore (peut prendre quelques secondes au premier lancement)
        vectorstore = FAISS.from_documents(
            documents=langchain_docs,
            embedding=embeddings_model
        )
        return vectorstore
        
    except Exception as e:
        print(f"❌ Erreur lors du chargement de FAISS: {e}")
        raise

# 🧠 Création du pipeline RAG
def create_rag_chain():
    """Crée la chaîne RAG complète"""
    try:
        db = load_vector_db()
        retriever = db.as_retriever(search_kwargs={"k": 3})

        llm = ChatOpenAI(
            api_key=openai_api_key,
            model="gpt-4o",
            temperature=0.7
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=False
        )

        return qa_chain
    except Exception as e:
        print(f"❌ Erreur lors de la création du RAG: {e}")
        raise

# 💬 Fonction d'interrogation avec prompts bienveillants et debug
def query_rag(question: str, mode: str = "dialogue") -> str:
    """Interroge le système RAG avec une question et un prompt système bienveillant"""
    try:
        # Charger le vectorstore directement pour debug
        db = load_vector_db()
        
        # Récupérer les documents pertinents
        docs = db.similarity_search(question, k=3)
        
        # Créer le retriever et le LLM
        retriever = db.as_retriever(search_kwargs={"k": 3})
        llm = ChatOpenAI(
            api_key=openai_api_key,
            model="gpt-4o",
            temperature=0.7
        )

        # 🎯 Prompt système bienveillant avec contexte explicite
        if mode == "emotion":
            system_prompt = (
                "Tu es Complice, un guide émotionnel doux et rassurant spécialisé dans l'autisme. "
                "Tu t'adresses à des adolescents autistes avec empathie et clarté. "
                "IMPORTANT: Base ta réponse sur les documents fournis qui contiennent des informations sur l'autisme. "
                "Utilise un ton chaleureux, encourageant, et ajoute des emojis doux pour rythmer la réponse."
            )
        else:
            system_prompt = (
                "Tu es Complice, un compagnon bienveillant spécialisé dans l'accompagnement des adolescents autistes. "
                "IMPORTANT: Base ta réponse principalement sur les extraits de documents fournis qui parlent d'autisme et de neurodiversité. "
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

Réponds en te basant sur les informations du contexte documentaire ci-dessus."""

        # Utiliser directement le LLM au lieu de RetrievalQA pour plus de contrôle
        response = llm.invoke([{"role": "user", "content": full_prompt}])
        
        return response.content

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"❌ Erreur détaillée: {error_details}")
        return f"❌ Erreur: {type(e).__name__}: {str(e)}. Détails: {error_details}. Vérifie que FAISS est bien chargé et que ta clé OpenAI est configurée."