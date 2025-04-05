# qstar/core/cloud/hf_push.py
from huggingface_hub import HfApi, Repository
import os


class HuggingFacePusher:
    def __init__(self, repo_id, token, local_dir="qstar_model"):
        self.repo_id = repo_id
        self.token = token
        self.local_dir = local_dir
        self.api = HfApi()

    def push_model(self):
        if not os.path.exists(self.local_dir):
            raise ValueError("Répertoire local introuvable pour le push.")

        repo = Repository(
            local_dir=self.local_dir, clone_from=self.repo_id, use_auth_token=self.token
        )
        repo.git_add()
        repo.git_commit("Mise à jour du modèle Q-STAR")
        repo.git_push()
        print("✅ Modèle poussé sur Hugging Face Hub avec succès.")


if __name__ == "__main__":
    # Exemple d'utilisation
    pusher = HuggingFacePusher("guillaume-piron-dev/qstar", "hf_YourTokenHere")
    pusher.push_model()
