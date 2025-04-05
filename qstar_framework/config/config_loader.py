# qstar/config/config_loader.py
import yaml
from pathlib import Path

class QStarConfig:
    def __init__(self, config_path="config/qstar_config.yaml"):
        self.config_path = Path(config_path)
        self.config = self.load_config()

    def load_config(self):
        if not self.config_path.exists():
            raise FileNotFoundError(f"Fichier de configuration introuvable : {self.config_path}")
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def get(self, key_path, default=None):
        keys = key_path.split(".")
        val = self.config
        try:
            for key in keys:
                val = val[key]
            return val
        except (KeyError, TypeError):
            return default

if __name__ == "__main__":
    conf = QStarConfig()
    print("🔧 Backend utilisé :", conf.get("model.backend"))
    print("📦 Profil matériel auto :", conf.get("hardware.detect_on_startup"))
