# 📝 Changelog - Complice

## 🚀 Version 2.0 - Optimisations Performance (Janvier 2026)

### ⚡ **Améliorations de Performance**
- **Cache Streamlit** : Implémentation de `@st.cache_resource` pour tous les composants lourds
- **Vectorstore optimisé** : Chargement unique au lieu de rechargement à chaque requête
- **Modèles LLM cachés** : ChatGPT et embeddings OpenAI mis en cache
- **Gain de vitesse** : 80-90% plus rapide après l'initialisation
- **Temps de réponse** : Passage de 5-8s à 1-2s pour les requêtes chat

### 🎯 **Améliorations Qualité RAG**
- **Prompts optimisés** : Instructions pour éviter les références personnelles indésirables
- **Généralisation** : Les réponses évitent de citer des prénoms/situations spécifiques des documents
- **Contextualisation** : Réponses plus adaptées et bienveillantes
- **Cohérence** : Ton uniforme et empathique maintenu

### 📦 **Environnement**
- **Docker** : Image mise à jour avec les optimisations
- **Architecture** : Structure modulaire préservée
- **Compatibilité** : Toutes les fonctionnalités maintenues

### 🔧 **Modules optimisés**
- `rag_module.py` : Cache des vectorstores et modèles LLM
- `app.py` : Initialisation intelligente des ressources
- `quiz_module.py` : Gestionnaire de quiz mis en cache
- `image_module.py` : Inchangé (performance dépendante d'OpenAI)

### ✅ **Fonctionnalités testées**
- [x] Module Dialogue : Ultra-rapide
- [x] Module Émotions : Interface rapide + génération normale
- [x] Module Quiz : Instantané
- [x] Navigation : Fluide
- [x] Qualité des réponses : Améliorée

---

## 📋 Version 1.0 - Version initiale
- Système RAG complet avec FAISS
- Interface Streamlit multi-modules
- Génération d'images émotionnelles
- Quiz interactifs d'habiletés sociales
- Base documentaire spécialisée autisme