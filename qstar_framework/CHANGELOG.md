#Changelog – Q-STAR Framework

Toutes les modifications notables du projet seront consignées ici.

## [1.0.0] - 2025-04-07
### Ajouté ✅
- Pipeline séquentiel Q-STAR complet (5 étapes)
- Multimodalité (texte, image, audio)
- RLHF + TRL intégration de base
- Dockerfiles de prod et dev
- Support ONNX / TensorFlow / JAX / PyTorch
- Scripts CI/CD (`Makefile`, test, clean)
- Intégration hardware-aware (profil CPU/GPU/NPU)
- Export Hugging Face Space et API
- README, FAQ, Industrialisation, LLM doc, citation

### Changé ♻️
- Arborescence centralisée (framework-qstar/)
- Normalisation modules internes /scripts

### Corrigé 🛠️
- Support ARM / Raspberry avec fallback CPU