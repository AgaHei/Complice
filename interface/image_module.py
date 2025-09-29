# image_module.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔐 Charger la clé API depuis .env
# Spécifier le chemin vers le fichier .env dans le dossier parent
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
load_dotenv(env_path)
openai_api_key = os.getenv("OPENAI_API_KEY")

# 📸 Fonction de génération d'image avec DALL-E
def generate_emotion_image(prompt: str, model="dall-e-3"):
    """
    Envoie un prompt à OpenAI DALL-E pour générer une image.
    Retourne l'URL de l'image générée.
    """
    try:
        client = OpenAI(api_key=openai_api_key)
        
        # Améliorer le prompt pour DALL-E
        enhanced_prompt = f"Digital art, high quality, detailed: {prompt}"
        
        response = client.images.generate(
            model=model,
            prompt=enhanced_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        return response.data[0].url
    except Exception as e:
        print(f"❌ Erreur lors de la génération d'image : {e}")
        return None

# 📸 Version économique avec DALL-E 2 (optionnelle)
def generate_emotion_image_budget(prompt: str):
    """
    Version plus économique avec DALL-E 2
    """
    return generate_emotion_image(prompt, model="dall-e-2")