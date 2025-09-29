import streamlit as st
from rag_module import query_rag
from image_module import generate_emotion_image

st.set_page_config(page_title="Complice", page_icon="", layout="wide")

def render_dialogue_module():
    st.header("💬 Discuter avec Complice")
    
    # Message d'accueil chaleureux
    st.markdown("""
    👋 **Bonjour, je suis Complice - ton compagnon bienveillant !**
    
    Je suis là pour répondre à tes questions et t'aider à prendre confiance en toi. 
    N'hésite pas à me parler de tout ce qui te préoccupe ou t'intéresse ! 🤗
    """)
    
    user_input = st.text_input("🌟 Quelle question voudrais-tu me poser aujourd'hui ?")
    if user_input:
        response = query_rag(user_input, mode="dialogue")
        st.success(response)

def render_emotion_module():
    st.header("🌈 Explorer les émotions avec Complice")
    
    # Dictionnaire des émotions
    emotions = {
        "😊 Joie": "Un sentiment de bonheur et de satisfaction",
        "😢 Tristesse": "Un sentiment de peine ou de mélancolie",
        "😠 Colère": "Un sentiment d'irritation ou de frustration",
        "😨 Peur": "Un sentiment d'inquiétude ou d'anxiété",
        "😤 Frustration": "Un sentiment d'agacement face à un obstacle",
        "😴 Fatigue": "Un sentiment d'épuisement ou de lassitude",
        "🤗 Affection": "Un sentiment de tendresse ou d'amour",
        "😔 Solitude": "Un sentiment d'isolement ou de vide",
        "😰 Stress": "Un sentiment de tension ou de pression",
        "🤔 Confusion": "Un sentiment d'incertitude ou de perplexité",
        "😌 Sérénité": "Un sentiment de calme et de paix",
        "😖 Overwhelm": "Un sentiment d'être dépassé par les événements"
    }
    
    # Sélection de l'émotion
    selected_emotion = st.selectbox(
        "Quelle émotion ressens-tu en ce moment ?",
        list(emotions.keys()),
        index=0
    )
    
    # Affichage de la description
    if selected_emotion:
        st.write(f"**{selected_emotion}** : {emotions[selected_emotion]}")
    
    # Zone de texte pour décrire l'émotion
    emotion_description = st.text_area(
        "Peux-tu me décrire ce que tu ressens ? (optionnel)",
        placeholder="Décris ton émotion avec tes propres mots...",
        height=100
    )
    
    # Sélecteur de personnage avec formulation inclusive
    personnage = st.radio(
        "Définis la personne que tu aimerais visualiser :",
        ["👦 Garçon / Homme", "👧 Fille / Femme"],
        help="Cela permet à Complice de mieux adapter l'image et le ton de la réponse."
    )
    
    # Paramètres supplémentaires pour personnaliser l'image
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider(
            "🎂 Âge de la personne :",
            min_value=5,
            max_value=80,
            value=15,
            help="Choisis l'âge qui te correspond ou te ressemble"
        )
    
    with col2:
        lieu = st.selectbox(
            "📍 Lieu :",
            ["🏫 École", "🏠 Maison", "🌳 Parc", "🏖️ Plage", "🍽️ Restaurant", 
             "🛍️ Magasin", "🚶 Rue", "🌲 Forêt", "🏥 Hôpital", "📚 Bibliothèque"],
            help="Où se déroule la scène ?"
        )
    
    with col3:
        moment = st.selectbox(
            "🕐 Moment :",
            ["🌅 Matin", "☀️ Midi", "🌇 Soir", "🌙 Nuit"],
            help="À quel moment de la journée ?"
        )
    
    # Bouton pour générer l'image
    if st.button("🎨 Créer une image de mon émotion", type="primary"):
        if selected_emotion:
            with st.spinner("Création de ton image en cours..."):
                try:
                    # Préparation du prompt pour l'image
                    emotion_name = selected_emotion.split(' ', 1)[1]  # Enlever l'emoji
                    
                    # Génération de l'image
                    image_url = generate_emotion_image(emotion_name, emotion_description, personnage, age, lieu, moment)
                    
                    if image_url:
                        st.success("🎉 Ton image est prête !")
                        
                        # Affichage de l'image avec taille réduite
                        col1, col2, col3 = st.columns([1, 1, 1])
                        with col2:
                            st.image(image_url, caption=f"Ton émotion : {emotion_name}", width=300)
                        
                        # Discussion sur l'émotion avec RAG
                        st.subheader("💬 Parlons de ton émotion")
                        
                        # Construction du contexte pour la discussion
                        context_text = f"Je ressens {emotion_name}"
                        if emotion_description:
                            context_text += f" : {emotion_description}"
                        
                        # Génération de la réponse empathique
                        emotion_response = query_rag(context_text, mode="emotion")
                        st.info(emotion_response)
                        
                        # Zone pour continuer la discussion
                        follow_up = st.text_input(
                            "Veux-tu en parler davantage ?",
                            placeholder="Partage tes pensées..."
                        )
                        
                        if follow_up:
                            follow_response = query_rag(follow_up, mode="emotion")
                            st.success(follow_response)
                    
                    else:
                        st.error("❌ Impossible de générer l'image. Réessaye plus tard.")
                        
                except Exception as e:
                    st.error(f"❌ Erreur lors de la génération : {str(e)}")
        else:
            st.warning("⚠️ Sélectionne d'abord une émotion !")

st.sidebar.title("🤗 Complice")
module = st.sidebar.radio("Choisis une activite :", ["💬 Discuter avec Complice", "🌈 Explorer les émotions avec Complice"])

if module == "💬 Discuter avec Complice":
    render_dialogue_module()
elif module == "🌈 Explorer les émotions avec Complice":
    render_emotion_module()
