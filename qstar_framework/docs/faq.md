# ❓ FAQ – Foire aux questions sur Q-STAR

Bienvenue dans la FAQ du projet **Q-STAR**.
Cette section est destinée à répondre aux questions les plus fréquentes posées par les utilisateurs, chercheurs et développeurs intéressés par ce framework.

---

### 🧠 En quoi Q-STAR est-il innovant ?
Q-STAR combine un traitement séquentiel avec une vérification asynchrone, un recalibrage automatique, une corrélation croisée et une synthèse finale. Il intègre ces étapes dans un pipeline modulaire visant à fiabiliser les modèles IA, limiter les hallucinations et optimiser l’apprentissage.

---

### ⚙️ Quels types de modèles sont compatibles avec Q-STAR ?
- Hugging Face Transformers (texte)
- Modèles ONNX (edge et embedded)
- JAX / TensorFlow (expérimental)
- Multimodalité (image, audio, texte)

---

### 📦 Comment installer Q-STAR ?
```
git clone https://github.com/guillaume-piron-dev/qstar.git
cd qstar
make install
```

---

### 🚀 Comment exécuter un exemple ?
```
make run MODULE=gradio
# ou
python examples/example_multimodal.py
```

---

### 🔍 Puis-je l’utiliser sans GPU ?
Oui ! Q-STAR détecte automatiquement le matériel. En l’absence de GPU, il s’adapte à un usage CPU ou ONNX sur Raspberry Pi ou serveur léger.

---

### 🌐 Peut-on l’utiliser via API ou en démo ?
Oui. Deux interfaces sont disponibles :
- Gradio (rapide, démo locale)
- FastAPI (API REST pour production)

---

### 🔐 Est-il sécurisé ?
Oui. Des modules de détection d’anomalie, de contrôle de cohérence, d’export de logs et de validation asynchrone sont intégrés.

---

### 🧪 Peut-on intégrer Q-STAR dans un pipeline DevOps ?
Oui, le framework est conçu pour être :
- Conteneurisable (Docker)
- Scriptable (Makefile, scripts)
- Testable (`make test`)
- CI-friendly (GitHub Actions à venir)

---

### 📚 Où trouver la documentation scientifique ?
Dans `docs/qstar_llm.md`, avec explications mathématiques, cas d’usage, citations et méthodes d’optimisation.

---

### 👨‍🔬 Comment contribuer au projet ?
Lisez `CONTRIBUTING.md`, ouvrez une issue ou une pull request, et testez les modules localement avec `run.py`.

---

### 🧠 Citation académique ?
```
@software{piron2025qstar,
  title = {Q-STAR: Séquentialisation intelligente pour IA fiable},
  author = {Piron, Guillaume},
  year = {2025},
  url = {https://github.com/guillaume-piron-dev/qstar},
  version = {1.0},
  license = {MIT}
}
```

---

> Une autre question ? Ouvre une issue sur [GitHub](https://github.com/guillaume-piron-dev/qstar/issues) ou contacte-nous directement.
