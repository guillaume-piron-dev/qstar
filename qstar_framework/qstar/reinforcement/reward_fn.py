# qstar/reinforcement/reward_fn.py

from qstar.core.verifier import QStarVerifier

# Initialisation du vérificateur de cohérence
verifier = QStarVerifier()


def score_response(prompt: str, response: str) -> float:
    """
    Évalue la cohérence du couple prompt-réponse à l'aide du vérificateur Q-STAR.

    Args:
        prompt (str): Le texte d'entrée à traiter.
        response (str): La réponse générée par un LLM ou pipeline.

    Returns:
        float: Score de cohérence, entre 0.0 et 1.0
    """
    return verifier.score(prompt, response)


def detect_hallucination(response: str) -> bool:
    """
    Détecte la présence d'hallucinations potentielles dans une réponse.

    Args:
        response (str): La réponse générée.

    Returns:
        bool: True si une hallucination est détectée, False sinon.
    """
    return verifier.detect_hallucination(response)


def composite_reward(prompt: str, response: str) -> float:
    """
    Combine le score de cohérence et une pénalité si une hallucination est détectée.

    Args:
        prompt (str): Le prompt utilisé en entrée.
        response (str): La réponse générée.

    Returns:
        float: Score final de récompense pour un apprentissage par renforcement.
    """
    penalty = 0.2 if detect_hallucination(response) else 0.0
    return score_response(prompt, response) - penalty
