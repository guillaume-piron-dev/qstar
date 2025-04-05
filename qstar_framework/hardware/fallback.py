# qstar/hardware/fallback.py
import torch
import logging

def is_fallback_required():
    fallback = {
        "no_gpu": not torch.cuda.is_available(),
        "low_memory": torch.cuda.is_available() and torch.cuda.get_device_properties(0).total_memory < 4 * 1024 ** 3
    }
    return fallback

def fallback_message():
    status = is_fallback_required()
    if status["no_gpu"]:
        logging.warning("GPU non détecté : passage en mode CPU optimisé")
    elif status["low_memory"]:
        logging.warning("GPU mémoire trop faible : réduction des paramètres modèle")
    else:
        logging.info("Pas de fallback nécessaire. Ressources suffisantes.")

if __name__ == "__main__":
    fallback_message()
