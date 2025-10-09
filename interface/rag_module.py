# rag_module.py
# rag_module.py

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS  
from langchain_huggingface import HuggingFaceEmbeddings  

# 🔐 Charger la clé API depuis .env
# Dans Docker, le fichier .env est dans le même répertoire que les modules Python
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(env_path)
openai_api_key = os.getenv("OPENAI_API_KEY")

# 🔧 Chargement du vectordb
def load_vector_db(index_path=None):
    """Charge la base vectorielle FAISS"""
    # Chemin absolu pour éviter les problèmes
    if index_path is None:
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Dans Docker, nous sommes dans /home/jovyan/work/interface/
        # Donc data/ (embeddings) est dans le parent /home/jovyan/work/data/
        parent_dir = os.path.dirname(current_dir)
        index_path = os.path.join(parent_dir, "data", "embeddings", "faiss_store")
    
    try:
        # Utiliser les embeddings OpenAI (1536 dimensions)
        from langchain_openai import OpenAIEmbeddings
        embeddings = OpenAIEmbeddings(
            api_key=openai_api_key,
            model="text-embedding-3-small"
        )
        db = FAISS.load_local(
            index_path, 
            embeddings,
            allow_dangerous_deserialization=True  # ✅ Nécessaire pour FAISS
        )
        return db
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
            api_key=openai_api_key,  # ✅ Nouveau paramètre
            model="gpt-4o",  # ✅ model au lieu de model_name
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

# 💬 Fonction d'interrogation avec prompts bienveillants
def query_rag(question: str, mode: str = "dialogue") -> str:
    """Interroge le système RAG avec une question et un prompt système bienveillant"""
    try:
        qa_chain = create_rag_chain()

        # 🎯 Prompt système bienveillant
        if mode == "emotion":
            system_prompt = (
                "Tu es Complice, un guide émotionnel doux et rassurant. "
                "Tu t'adresses à des adolescents autistes avec empathie et clarté. "
                "Utilise un ton chaleureux, encourageant, et ajoute des emojis doux pour rythmer la réponse."
            )
        else:
            system_prompt = (
                "Tu es Complice, un compagnon bienveillant pour discuter librement. "
                "Tu valorises les émotions, tu rassures, et tu évites les formulations trop techniques. "
                "Ajoute des emojis doux pour rendre la réponse plus accessible."
            )

        # 🧠 Fusionner le prompt avec la question
        full_prompt = f"{system_prompt}\n\nQuestion : {question}"

        response = qa_chain.invoke({"query": full_prompt})
        return response["result"]

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"❌ Erreur détaillée: {error_details}")
        return f"❌ Erreur: {type(e).__name__}: {str(e)}. Détails: {error_details}. Vérifie que FAISS est bien chargé et que ta clé OpenAI est configurée."