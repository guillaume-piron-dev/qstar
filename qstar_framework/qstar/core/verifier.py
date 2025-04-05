# qstar/core/verifier.py


class QStarVerifier:
    def __init__(self):
        # Initialisation simple ou avec des paramètres de vérification
        pass

    def score(self, prompt: str, response: str) -> float:
        """
        Évalue la cohérence du prompt et de la réponse.
        """
        # Exemple : on retourne un score fictif
        return 0.95

    def detect_hallucination(self, response: str) -> bool:
        """
        Détecte si la réponse contient des hallucinations.
        """
        # Exemple : réponse trop courte = suspicion
        return len(response.strip()) < 5
