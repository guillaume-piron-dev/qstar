# clean_outputs.py – Purge des dossiers sans supprimer les fichiers .gitkeep

import os
import shutil

# Dossiers à nettoyer (hors .gitkeep)
TARGET_DIRS = ["logs", "outputs"]

for folder in TARGET_DIRS:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if filename != ".gitkeep":
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print(f"✅ Supprimé : {file_path}")
                except Exception as e:
                    print(f"❌ Erreur lors de la suppression de {file_path} : {e}")

print("✨ Nettoyage terminé. Les fichiers .gitkeep sont préservés.")
