# ✅ Image de base PyTorch optimisée pour CPU (ou CUDA si GPU)
FROM pytorch/pytorch:2.2.2-cpu

# 🌐 Mise à jour des outils système
RUN apt-get update && apt-get install -y git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*

# 📁 Créer le dossier de travail
WORKDIR /app

# 🔄 Copier les fichiers
COPY . .

# 🔍 Dépendances (CPU-compatible avec fix TensorFlow)
RUN pip install --upgrade pip
RUN pip install ml_dtypes==0.2.0
RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# ⚙️ (Optionnel) Ajout support HF datasets cache
ENV HF_HOME=/app/.cache/huggingface

# ✅ Commande par défaut
CMD ["python", "qstar/reinforcement/train_rlhf.py"]
