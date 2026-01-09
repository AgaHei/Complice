#!/usr/bin/env python3
"""
Script de test des performances pour Complice
Test les fonctions optimisées avec cache Streamlit
"""

import time
import sys
import os

# Ajouter le dossier interface au path pour les imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'interface'))

def test_rag_performance():
    """Test de performance du module RAG optimisé"""
    print("🧪 Test des performances RAG optimisées")
    print("=" * 50)
    
    try:
        from rag_module import load_vector_db, get_llm, query_rag
        
        # Test 1: Chargement initial (devrait être lent la première fois)
        print("\n1️⃣ Premier chargement du vectorstore...")
        start_time = time.time()
        db = load_vector_db()
        first_load_time = time.time() - start_time
        print(f"   ⏱️ Temps: {first_load_time:.2f}s")
        
        # Test 2: Deuxième chargement (devrait être instantané avec le cache)
        print("\n2️⃣ Deuxième chargement (cache)...")
        start_time = time.time()
        db2 = load_vector_db()
        second_load_time = time.time() - start_time
        print(f"   ⏱️ Temps: {second_load_time:.2f}s")
        
        # Test 3: Chargement du LLM
        print("\n3️⃣ Chargement du modèle LLM...")
        start_time = time.time()
        llm = get_llm()
        llm_load_time = time.time() - start_time
        print(f"   ⏱️ Temps: {llm_load_time:.2f}s")
        
        # Test 4: Query RAG
        print("\n4️⃣ Test d'une requête RAG...")
        start_time = time.time()
        response = query_rag("Comment gérer le stress ?", mode="dialogue")
        query_time = time.time() - start_time
        print(f"   ⏱️ Temps: {query_time:.2f}s")
        print(f"   📝 Réponse (extrait): {response[:100]}...")
        
        # Résumé des performances
        print("\n📊 RÉSUMÉ DES PERFORMANCES")
        print("=" * 50)
        print(f"Premier chargement DB: {first_load_time:.2f}s")
        print(f"Cache DB (gain):       {second_load_time:.2f}s (🚀 {((first_load_time-second_load_time)/first_load_time)*100:.1f}% plus rapide)")
        print(f"Chargement LLM:        {llm_load_time:.2f}s")
        print(f"Requête complète:      {query_time:.2f}s")
        
        if second_load_time < 0.1:
            print("\n✅ OPTIMISATION RÉUSSIE ! Le cache fonctionne parfaitement.")
        else:
            print("\n⚠️ Le cache pourrait être amélioré.")
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        import traceback
        traceback.print_exc()

def test_quiz_performance():
    """Test de performance du module Quiz"""
    print("\n🧩 Test des performances Quiz")
    print("=" * 50)
    
    try:
        from quiz_module import get_quiz_manager
        
        start_time = time.time()
        quiz_manager = get_quiz_manager()
        load_time = time.time() - start_time
        
        stats = quiz_manager.get_quiz_statistics()
        print(f"⏱️ Chargement quiz: {load_time:.2f}s")
        print(f"📊 {stats['total']} quiz disponibles")
        
        if load_time < 0.5:
            print("✅ Quiz chargé rapidement !")
        else:
            print("⚠️ Chargement des quiz un peu lent.")
            
    except Exception as e:
        print(f"❌ Erreur quiz: {e}")

if __name__ == "__main__":
    print("🚀 COMPLICE - TEST DE PERFORMANCE")
    print("Version optimisée avec cache Streamlit")
    print("=" * 50)
    
    # Tests des modules
    test_rag_performance()
    test_quiz_performance()
    
    print("\n🎉 Tests terminés !")
    print("💡 Conseil: Lancez l'app avec 'streamlit run interface/app.py'")