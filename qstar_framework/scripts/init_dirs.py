# scripts/init_dirs.py
import os

# Liste des chemins relatifs à la racine du projet (framework-qstar)
directories = [
    "qstar",
    "qstar/core",
    "qstar/core/cloud",
    "qstar/core/execution",
    "qstar/core/interop",
    "qstar/core/security",
    "qstar/models",
    "qstar/models/audio",
    "qstar/models/text",
    "qstar/models/vision",
    "qstar/modules",
    "qstar/reinforcement",
    "qstar/edge",
    "qstar/api",
    "qstar/agents",
    "qstar/logging",
    "tools",
    "tests",
    "examples",
    "modules",
    "reinforcement",
    "security",
    "hardware"
]

def create_init_files():
    for directory in directories:
        init_path = os.path.join(directory, "__init__.py")
        os.makedirs(directory, exist_ok=True)
        if not os.path.exists(init_path):
            with open(init_path, "w", encoding="utf-8") as f:
                f.write("# Initialisation de package\n")
            print(f"✅ Créé : {init_path}")
        else:
            print(f"✔️ Déjà présent : {init_path}")

if __name__ == "__main__":
    create_init_files()
