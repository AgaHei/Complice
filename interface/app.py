import streamlit as st
from rag_module import query_rag
from image_module import generate_emotion_image

# Configuration de la page
st.set_page_config(
    page_title="Complice",
    page_icon="🤗",
    layout="wide"
)

# 🌸 Palette pastel (via CSS)
st.markdown("""
    <style>
    body { background-color: #f7f5f2; }
    .stApp { font-family: 'Quicksand', sans-serif; }
    h1, h2, h3 { color: #4b4b4b; }
    .block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# 🤗 Barre latérale
st.sidebar.title("🤗 Complice")
st.sidebar.markdown("Un compagnon bienveillant pour explorer les émotions et les situations sociales.")
module = st.sidebar.radio("Choisis une activité :", ["💬 Dialogue", "🎭 Coaching émotionnel", "🤝 Analyse sociale"])

# 💬 Module 1 : Dialogue RAG
if module == "💬 Dialogue":
    st.header("🤗 Discuter avec Complice")
    st.write("Pose tes questions sur l'autisme, les émotions ou les habiletés sociales.")
    user_input = st.text_input("Ta question ici")
    if user_input:
        with st.spinner("Complice réfléchit..."):
            response = query_rag(user_input)
        st.success(response)

# 🎭 Module 2 : Coaching émotionnel
elif module == "🎭 Coaching émotionnel":
    st.header("🎭 Explorer une émotion")
    st.write("Choisis une émotion et les paramètres de l'image à générer. Complice t'aidera à mieux comprendre cette émotion.")

    # 🌿 Liste enrichie d'émotions
    emotions_dict = {
        "joie": "Un état de plaisir, de satisfaction ou de bonheur.",
        "tristesse": "Une émotion liée à la perte, au manque ou à la solitude.",
        "colère": "Une réaction à une injustice ou une frustration.",
        "peur": "Une émotion face à un danger ou une incertitude.",
        "calme": "Un état de sérénité et de détente.",
        "surprise": "Une réaction à un événement inattendu.",
        "ironie": "Une manière de dire le contraire de ce qu'on pense, souvent avec humour.",
        "sarcasme": "Une forme d'ironie plus mordante, parfois moqueuse.",
        "jalousie": "Une inquiétude liée à la peur de perdre l'attention ou l'amour de quelqu'un.",
        "cynisme": "Une attitude de méfiance ou de désillusion face aux intentions des autres.",
        "embarras": "Un malaise ressenti dans une situation sociale délicate.",
        "condescendance": "Une attitude de supériorité déguisée en bienveillance.",
        "nostalgie": "Un mélange doux-amer de souvenirs heureux et de regret du passé.",
        "perplexité": "Un état de confusion ou d'hésitation face à une situation complexe.",
        "fierté": "Une satisfaction liée à une réussite ou à une valeur personnelle.",
        "honte": "Un malaise lié à une faute ou à une transgression perçue.",
        "remords": "Une tristesse liée à une action que l'on regrette.",
        "gratitude": "Une reconnaissance sincère envers quelqu'un ou quelque chose.",
        "méfiance": "Une prudence face à une personne ou une situation incertaine.",
        "frustration": "Une tension liée à un obstacle ou un besoin non satisfait.",
        "solitude": "Un sentiment d'isolement, choisi ou subi.",
        "soulagement": "Une détente après une période de stress ou d'inquiétude."
    }

    with st.form("emotion_form"):
        emotion = st.selectbox("Émotion à explorer", list(emotions_dict.keys()))
        sexe = st.radio("Sexe du personnage", ["masculin", "féminin"])
        age = st.slider("Âge", min_value=5, max_value=80, value=25)  # ✅ Syntaxe corrigée
        nombre = st.selectbox("Nombre de personnes", [1, 2])
        environnement = st.selectbox("Environnement", ["maison", "école", "parc", "chambre", "extérieur", "restaurant"])
        moment = st.selectbox("Moment", ["jour", "nuit", "matin", "coucher de soleil", "lumière tamisée"])
        submitted = st.form_submit_button("Générer l'image et lancer la discussion")

    if submitted:
        # 🧠 Affichage de la définition
        st.subheader(f"🧠 Définition de '{emotion}'")
        st.write(emotions_dict[emotion])

        # 🖼️ Construction du prompt image
        prompt = f"Photorealistic portrait of {nombre} person(s), {sexe} gender, age {age}, expressing the emotion '{emotion}' in a {environnement} environment, {moment} lighting, natural facial expression, high quality"
        st.markdown(f"**Prompt généré :** _{prompt}_")

        # 📸 Génération de l'image avec Replicate
        with st.spinner("🎨 Génération de l'image en cours..."):
            try:
                image_url = generate_emotion_image(prompt)
                if image_url:
                    st.image(image_url, caption=f"Expression de l'émotion : {emotion}")
                else:
                    st.warning("⚠️ Impossible de générer l'image. Utilisation d'une image de remplacement.")
                    st.image("https://via.placeholder.com/400x300.png?text=Image+émotionnelle")
            except Exception as e:
                st.error(f"❌ Erreur lors de la génération : {str(e)}")
                st.image("https://via.placeholder.com/400x300.png?text=Erreur+génération")

        # 💬 Commentaire bienveillant
        st.markdown("**Complice dit :**")
        st.info(f"Cette scène semble illustrer l'émotion **{emotion}**. Que ressens-tu en la regardant ? Veux-tu en parler ?")

        # 🧩 Option de discussion
        user_reflection = st.text_input("Exprime ce que cette image t'évoque")
        if user_reflection:
            st.success("Merci pour ton partage. Complice est là pour t'écouter et t'accompagner.")

# 🤝 Module 3 : Analyse sociale
elif module == "🤝 Analyse sociale":
    st.header("🤝 Comprendre une situation sociale")
    st.write("Crée une scène sociale et discute avec Complice.")

    with st.form("social_form"):
        interaction = st.selectbox("Type d'interaction", ["discussion", "conflit", "entraide", "demande", "refus", "invitation", "excuse", "compliment", "présentation", "remerciement", "adieu", "salutation"])
        lieu = st.selectbox("Lieu", ["école", "maison", "rue", "salle de classe", "parc", "restaurant"])
        moment = st.selectbox("Moment", ["jour", "nuit", "pause", "repas"])
        nombre = st.selectbox("Nombre de personnes", [2, 3])
        submitted_social = st.form_submit_button("Générer la scène")

    if submitted_social:
        # Construction du prompt pour Replicate
        social_prompt = f"Photorealistic scene showing {nombre} people having a {interaction} interaction in a {lieu}, {moment} time, natural body language, realistic social setting"
        
        with st.spinner("🎨 Génération de la scène sociale..."):
            try:
                image_url = generate_emotion_image(social_prompt)
                if image_url:
                    st.image(image_url, caption=f"Scène : {interaction} au {lieu}")
                else:
                    st.image("https://via.placeholder.com/400x300.png?text=Scene+sociale")
            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")
                st.image("https://via.placeholder.com/400x300.png?text=Erreur")
        
        # Analyse par le RAG
        analysis_question = f"Comment gérer une situation de {interaction} dans un contexte de {lieu} ?"
        with st.spinner("Complice analyse la situation..."):
            analysis = query_rag(analysis_question)
        st.info(f"**Analyse de Complice :** {analysis}")