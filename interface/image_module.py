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
def generate_emotion_image(emotion_name: str, emotion_description: str = "", personnage: str = "👦 Garçon / Homme", age: int = 15, lieu: str = "🏫 École", moment: str = "☀️ Midi", model="dall-e-3"):
    """
    Envoie un prompt à OpenAI DALL-E pour générer une image d'émotion personnalisée.
    Retourne l'URL de l'image générée.
    
    Args:
        emotion_name: Nom de l'émotion (ex: "Joie", "Tristesse")
        emotion_description: Description personnalisée de l'émotion
        personnage: Type de personnage à visualiser
        age: Âge du personnage (5-80 ans)
        lieu: Lieu où se déroule la scène
        moment: Moment de la journée
        model: Modèle DALL-E à utiliser
    """
    try:
        client = OpenAI(api_key=openai_api_key)
        
        # Adapter le prompt selon le personnage choisi
        gender_prompt = "boy" if "Garçon" in personnage else "girl"
        
        # Adapter l'âge dans le prompt
        if age <= 12:
            age_prompt = f"young {gender_prompt}"
        elif age <= 17:
            age_prompt = f"teenage {gender_prompt}"
        elif age <= 30:
            age_prompt = f"young adult {gender_prompt if gender_prompt == 'boy' else 'woman' if gender_prompt == 'girl' else gender_prompt}"
        else:
            age_prompt = f"adult {gender_prompt if gender_prompt == 'boy' else 'woman' if gender_prompt == 'girl' else gender_prompt}"
        
        # Nettoyer les emojis des paramètres pour le prompt
        lieu_clean = lieu.split(' ', 1)[1] if ' ' in lieu else lieu
        moment_clean = moment.split(' ', 1)[1] if ' ' in moment else moment
        
        # Adapter le lieu en anglais
        lieu_mapping = {
            "École": "school", "Maison": "home", "Parc": "park", "Plage": "beach",
            "Restaurant": "restaurant", "Magasin": "store", "Rue": "street",
            "Forêt": "forest", "Hôpital": "hospital", "Bibliothèque": "library"
        }
        lieu_en = lieu_mapping.get(lieu_clean, "park")
        
        # Adapter le moment en anglais
        moment_mapping = {
            "Matin": "morning", "Midi": "midday", "Soir": "evening", "Nuit": "night"
        }
        moment_en = moment_mapping.get(moment_clean, "midday")
        
        # Construire le prompt complet
        base_prompt = f"Digital art, high quality, detailed illustration of a {age_prompt} expressing {emotion_name.lower()}"
        base_prompt += f" in a {lieu_en} during {moment_en}"
        
        if emotion_description:
            base_prompt += f", {emotion_description}"
        
        # Style artistique adapté pour un public adolescent
        enhanced_prompt = f"{base_prompt}, warm and empathetic art style, soft colors, expressive face, safe and comforting atmosphere"
        
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