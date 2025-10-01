import json
import random
from pathlib import Path

class QuizManager:
    """Gestionnaire des quiz pour l'application Complice"""
    
    def __init__(self, quiz_file_path=None):
        """Initialise le gestionnaire de quiz"""
        if quiz_file_path is None:
            # Chemin par défaut vers les 23 quiz complets avec réponses mélangées
            self.quiz_file_path = Path("data/quiz_complets_melanges_corriges.json")
        else:
            self.quiz_file_path = Path(quiz_file_path)
        
        self.quizzes = []
        self.current_quiz_index = 0
        self.load_quizzes()
    
    def load_quizzes(self):
        """Charge les quiz depuis le fichier JSON"""
        try:
            if self.quiz_file_path.exists():
                with open(self.quiz_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.quizzes = data.get("quiz", [])
                print(f"✅ {len(self.quizzes)} quiz chargés avec succès !")
            else:
                print(f"⚠️ Fichier de quiz non trouvé : {self.quiz_file_path}")
                # Quiz d'exemple en cas de problème
                self.quizzes = self._get_example_quiz()
        except Exception as e:
            print(f"❌ Erreur lors du chargement des quiz : {e}")
            self.quizzes = self._get_example_quiz()
    
    def _get_example_quiz(self):
        """Retourne un quiz d'exemple si le fichier n'est pas trouvé"""
        return [{
            "contexte": "Tu es dans une situation sociale nouvelle.",
            "question": "Quelle est la meilleure approche ?",
            "options": {
                "A": "Rester dans ton coin et observer",
                "B": "Te présenter calmement aux autres",
                "C": "Faire du bruit pour attirer l'attention",
                "D": "Partir immédiatement"
            },
            "bonne_reponse": "B",
            "commentaire": "Se présenter calmement est souvent la meilleure approche pour faire connaissance."
        }]
    
    def get_random_quiz(self):
        """Retourne un quiz aléatoire"""
        if self.quizzes:
            return random.choice(self.quizzes)
        return None
    
    def get_quiz_by_index(self, index):
        """Retourne un quiz spécifique par son index"""
        if 0 <= index < len(self.quizzes):
            return self.quizzes[index]
        return None
    
    def get_total_quizzes(self):
        """Retourne le nombre total de quiz disponibles"""
        return len(self.quizzes)
    
    def format_quiz_for_display(self, quiz):
        """Formate un quiz pour l'affichage dans Streamlit"""
        if not quiz:
            return None
        
        formatted = {
            "contexte": quiz.get("contexte", ""),
            "question": quiz.get("question", ""),
            "options": [],
            "correct_answer": quiz.get("bonne_reponse", ""),
            "explanation": quiz.get("commentaire", "")
        }
        
        # Formater les options pour Streamlit
        options = quiz.get("options", {})
        for letter in ["A", "B", "C", "D"]:
            if letter in options:
                formatted["options"].append({
                    "letter": letter,
                    "text": options[letter]
                })
        
        return formatted
    
    def check_answer(self, quiz, user_answer):
        """Vérifie si la réponse de l'utilisateur est correcte"""
        if not quiz or not user_answer:
            return False
        
        correct_answer = quiz.get("bonne_reponse", "")
        return user_answer.upper() == correct_answer.upper()
    
    def get_quiz_statistics(self):
        """Retourne des statistiques sur les quiz"""
        if not self.quizzes:
            return {"total": 0, "categories": {}}
        
        stats = {
            "total": len(self.quizzes),
            "answer_distribution": {"A": 0, "B": 0, "C": 0, "D": 0}
        }
        
        # Analyser la distribution des bonnes réponses
        for quiz in self.quizzes:
            correct = quiz.get("bonne_reponse", "")
            if correct in stats["answer_distribution"]:
                stats["answer_distribution"][correct] += 1
        
        return stats

# Fonction utilitaire pour initialiser le gestionnaire
def get_quiz_manager():
    """Fonction helper pour obtenir une instance du gestionnaire de quiz"""
    return QuizManager()