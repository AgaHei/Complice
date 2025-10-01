import streamlit as st
from rag_module import query_rag
from image_module import generate_emotion_image
from quiz_module import get_quiz_manager

st.set_page_config(page_title="Complice", page_icon="", layout="wide")

def render_dialogue_module():
    st.header("💬 Discuter avec Complice")
    
    # Message d'accueil chaleureux - texte ajusté
    st.markdown("""
    ### 👋 **Bonjour, je suis Complice - ton compagnon bienveillant !**
    
    Je suis là pour répondre à tes questions et t'aider à prendre confiance en toi. 
    N'hésite pas à me parler de tout ce qui te préoccupe ou t'intéresse ! 🤗
    """)
    
    # Saut de ligne avant le champ de prompt
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Question avec texte plus grand
    st.markdown("### 🌟 Quelle question voudrais-tu me poser aujourd'hui ?")
    
    user_input = st.text_input("", placeholder="Tape ta question ici...")
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

def render_about_page():
    """Page d'accueil et présentation de Complice"""
    
    # En-tête principal
    st.title("🤗 Bienvenue chez Complice")
    
    # Saut de ligne après le titre
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Message d'accueil personnalisé - taille intermédiaire
    st.markdown("""
    ### 👋 **Salut ! Je suis ravi de te retrouver ici !**
    
    ### Tu es dans un espace qui t'appartient, conçu spécialement pour t'accompagner avec bienveillance. 
    ### Prends le temps de découvrir ce que je peux t'offrir ! ✨
    """)
    
    # Séparateur simple
    st.markdown("---")
    
    # Section À propos
    st.markdown("""
    ## 🤗 À propos de Complice

    Complice est un assistant bienveillant conçu pour accompagner les adolescents autistes dans l'exploration de leurs émotions et le développement de leurs habiletés sociales.

    🌈 **Pourquoi Complice ?**  
    Parce que chacun mérite un espace doux, rassurant et respectueux pour mieux se comprendre et interagir avec les autres.

    💬 **Ce que tu peux faire ici :**
    - Discuter avec Complice pour explorer tes ressentis
    - Découvrir des émotions à travers des images et des mots simples
    - T'entraîner à réagir dans des situations sociales grâce à des quiz adaptés

    🧠 **Un ton chaleureux et sans jugement**  
    Complice ne donne pas de leçons. Il propose des pistes, pose des questions, et t'encourage à réfléchir à ton rythme.

    🐣 **Pour qui ?**  
    Pour tous les jeunes qui veulent mieux comprendre leurs émotions et leurs relations, en particulier ceux qui ont besoin d'un cadre rassurant et clair.
    """)
    
    # Section navigation
    st.markdown("---")
    st.subheader("🧭 Comment naviguer ?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 💬 Discuter
        Pour poser tes questions et explorer tes ressentis avec Complice
        """)
    
    with col2:
        st.markdown("""
        ### 🌈 Émotions
        Pour créer des images qui représentent ce que tu ressens
        """)
    
    with col3:
        st.markdown("""
        ### 🧩 Quiz
        Pour t'entraîner sur des situations sociales du quotidien
        """)
    
    # Call-to-action
    st.markdown("---")
    st.markdown("""
    ### 🚀 Prêt à commencer ?
    
    Utilise le menu dans la barre latérale pour choisir l'activité qui te fait envie ! 
    
    N'hésite pas à explorer, il n'y a pas de mauvaise façon de faire. 😊
    """)
    
    # Petite note encourageante
    st.info("💡 **Astuce :** Tu peux revenir à cette page à tout moment en sélectionnant 'À propos' dans le menu !")

def render_quiz_module():
    st.header("🧩 Quiz habiletés sociales avec Complice")
    
    # Message d'introduction
    st.markdown("""
    🎯 **Teste tes habiletés sociales avec Complice !**
    
    Ces quiz t'aideront à réfléchir sur différentes situations sociales 
    et à développer tes compétences relationnelles. 🤗
    """)
    
    # Initialiser le gestionnaire de quiz
    if 'quiz_manager' not in st.session_state:
        st.session_state.quiz_manager = get_quiz_manager()
    
    if 'current_quiz' not in st.session_state:
        st.session_state.current_quiz = None
    
    if 'quiz_answered' not in st.session_state:
        st.session_state.quiz_answered = False
    
    if 'user_answer' not in st.session_state:
        st.session_state.user_answer = None
    
    quiz_manager = st.session_state.quiz_manager
    
    # Statistiques des quiz
    stats = quiz_manager.get_quiz_statistics()
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"📊 **{stats['total']} quiz disponibles**")
    with col2:
        if st.button("🎲 Nouveau quiz aléatoire", type="primary"):
            st.session_state.current_quiz = quiz_manager.get_random_quiz()
            st.session_state.quiz_answered = False
            st.session_state.user_answer = None
            st.rerun()
    
    # Affichage du quiz
    if st.session_state.current_quiz:
        quiz = quiz_manager.format_quiz_for_display(st.session_state.current_quiz)
        
        # Contexte
        st.subheader("📖 Situation")
        st.write(quiz["contexte"])
        
        # Question
        st.subheader("❓ Question")
        st.write(quiz["question"])
        
        # Options de réponse
        st.subheader("🤔 Choix de réponse")
        
        if not st.session_state.quiz_answered:
            # Mode réponse
            option_texts = []
            for option in quiz["options"]:
                option_texts.append(f"{option['letter']} - {option['text']}")
            
            user_choice = st.radio(
                "Sélectionne ta réponse :",
                option_texts,
                key="quiz_choice"
            )
            
            if st.button("✅ Valider ma réponse"):
                # Extraire la lettre de la réponse
                selected_letter = user_choice[0]  # Premier caractère = lettre
                st.session_state.user_answer = selected_letter
                st.session_state.quiz_answered = True
                st.rerun()
        
        else:
            # Mode correction
            user_answer = st.session_state.user_answer
            correct_answer = quiz["correct_answer"]
            is_correct = quiz_manager.check_answer(st.session_state.current_quiz, user_answer)
            
            # Afficher toutes les options avec coloration
            for option in quiz["options"]:
                letter = option["letter"]
                text = option["text"]
                
                if letter == user_answer and is_correct:
                    st.success(f"✅ {letter} - {text} (Ta réponse - CORRECTE !)")
                elif letter == user_answer and not is_correct:
                    st.error(f"❌ {letter} - {text} (Ta réponse - Incorrecte)")
                elif letter == correct_answer:
                    st.info(f"💡 {letter} - {text} (Bonne réponse)")
                else:
                    st.write(f"⚪ {letter} - {text}")
            
            # Résultat et explication
            if is_correct:
                st.balloons()
                st.success("🎉 Bravo ! Tu as trouvé la bonne réponse !")
            else:
                st.warning(f"🤔 La bonne réponse était : **{correct_answer}**")
            
            # Explication
            st.subheader("💭 Explication")
            st.info(quiz["explanation"])
            
            # Discussion avec Complice sur la situation
            st.subheader("💬 Discuter avec Complice")
            
            discussion_context = f"Je viens de répondre à un quiz sur cette situation : {quiz['contexte']}. {quiz['explanation']}"
            discussion_response = query_rag(discussion_context, mode="dialogue")
            st.write(discussion_response)
            
            # Zone pour poser des questions sur le quiz
            follow_up_question = st.text_input(
                "As-tu des questions sur cette situation ?",
                placeholder="Demande des conseils à Complice..."
            )
            
            if follow_up_question:
                context_with_question = f"À propos de cette situation sociale : {quiz['contexte']}. {follow_up_question}"
                follow_response = query_rag(context_with_question, mode="dialogue")
                st.success(follow_response)
    
    else:
        st.write("👆 Clique sur 'Nouveau quiz aléatoire' pour commencer !")
        
        # Aperçu des statistiques
        if stats['total'] > 0:
            st.subheader("📈 Aperçu des quiz")
            col1, col2, col3, col4 = st.columns(4)
            
            distribution = stats['answer_distribution']
            with col1:
                st.metric("Réponses A", distribution.get('A', 0))
            with col2:
                st.metric("Réponses B", distribution.get('B', 0))
            with col3:
                st.metric("Réponses C", distribution.get('C', 0))
            with col4:
                st.metric("Réponses D", distribution.get('D', 0))

st.sidebar.title("🤗 Complice")
# Ajouter un espace pour aligner avec le message d'accueil
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# CSS pour espacer les options du radio
st.sidebar.markdown("""
<style>
.stRadio > div {
    margin-bottom: 15px;
}
.stRadio > div > label {
    margin-bottom: 10px !important;
    padding: 8px 0 !important;
}
</style>
""", unsafe_allow_html=True)

module = st.sidebar.radio("Choisis une activite :", [
    "🏠 À propos",
    "💬 Discuter avec Complice", 
    "🌈 Explorer les émotions avec Complice",
    "🧩 Quiz habiletés sociales"
])

# Ajouter des espaces visuels dans la sidebar
st.sidebar.markdown("---")

if module == "🏠 À propos":
    render_about_page()
elif module == "💬 Discuter avec Complice":
    render_dialogue_module()
elif module == "🌈 Explorer les émotions avec Complice":
    render_emotion_module()
elif module == "🧩 Quiz habiletés sociales":
    render_quiz_module()
