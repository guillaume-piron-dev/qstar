![Build](https://img.shields.io/github/actions/workflow/status/guillaume-piron-dev/qstar/test_full.yml?label=CI%20Build&style=flat-square)
![CI Full Build](https://github.com/guillaume-piron-dev/qstar/actions/workflows/test_full.yml/badge.svg)
![CI Status](https://github.com/F4S1R/qstar/actions/workflows/test.yml/badge.svg)
![Build Status](https://github.com/guillaume-piron-dev/qstar/actions/workflows/test_full.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![PyPI version](https://img.shields.io/pypi/v/qstar?label=PyPI&color=brightgreen)
![Docker Pulls](https://img.shields.io/docker/pulls/guillaume-piron/qstar)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
[![HF Space](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-orange)](https://huggingface.co/spaces/guillaume-piron/qstar)
![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Lint: Flake8](https://img.shields.io/badge/lint-flake8-yellow)
![PyPI - Downloads](https://img.shields.io/pypi/dm/qstar?label=PyPI%20Downloads&color=blue)
![No Candy, Only Code](https://img.shields.io/badge/friandise-non--requise-blueviolet?style=for-the-badge&logo=python)


# Q-STAR 🚀 – Framework IA Séquentielle Asynchrone Multimodale

**Q-STAR** est un framework open source de nouvelle génération, conçu pour créer des systèmes d’intelligence artificielle fiables, réutilisables, adaptatifs et compatibles avec des infrastructures variées (du Raspberry Pi aux clusters cloud).

> 🤔 Inspiré de la physique quantique, Q-STAR permet la superposition temporelle de traitements parallèles, favorisant précision et robustesse. Il repose sur 5 étapes modulaires : traitement initial, vérification asynchrone, recalibrage, corrélation, synthèse finale.

---

## 📂 Arborescence principale (framework-qstar)

```bash
framework-qstar/
├── qstar/
│   ├── qstar_core.py          # Pipeline principal
│   ├── async_core.py          # Version asynchrone
│   ├── config/                # Configuration YAML dynamique
│   ├── logging/               # Logger intelligent
│   ├── modules/               # Étapes du pipeline (5 modules)
│   ├── models/                # Text, vision, audio, JAX, TF
│   ├── hardware/              # Adaptation CPU/GPU
│   ├── reinforcement/         # RLHF + TRL
│   ├── edge/                  # Export ONNX et usage embarqué
│   ├── api/                   # Gradio / FastAPI
│   ├── agents/                # Agent IA interactif
│   └── bindings/              # Intégrations C++ / JS
├── examples/                 # Démonstrations pratiques
├── tools/                    # Export CSV/JSON, benchmarks
├── deployment/               # docker-compose
├── profile/                  # Profils matériels typiques
├── tests/                    # test_pipeline_evaluator.py
├── docs/                     # Documentation scientifique
├── run_all.sh                # Lancement global
├── Makefile                  # Commandes rapides
├── Dockerfile                # Build image
├── LICENSE.md                # Licence MIT
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
└── CITATION.cff
```

---

## 🛠️ Installation complète

### Avec Make :
```bash
git clone https://github.com/guillaume-piron-dev/qstar.git
cd qstar
make install
```

### Ou manuellement :
```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install ml_dtypes==0.2.0
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

> ❓ Si vous utilisez **JAX** et **TensorFlow**, assurez-vous que `ml_dtypes==0.2.0` est explicitement installé **avant** `tensorflow==2.15.0`

---

## 🚀 Lancement rapide de modules

### Interface API (FastAPI)
```bash
make run MODULE=api
```

### Interface Gradio
```bash
make run MODULE=gradio
```

### RLHF / Entraînement via TRL
```bash
make run MODULE=rlhf
make test_rlhf
```

### Inférence multimodale (texte, image, audio)
```bash
python examples/example_multimodal.py
```

### Ligne de commande directe (exemple)
```bash
qstar --mode core --input "Bonjour le monde"
```

---

## 🫖 Tests & couverture

### Lancer les tests :
```bash
make test
# ou manuellement
pytest tests/
```

### Couverture de code :
```bash
pytest --cov=qstar tests/
```

---

## 🧬 Fonctionnalités majeures

- ✅ Traitement **séquentiel et asynchrone**
- 🌟 Vérification + recalibrage des sorties LLM
- 🧬 **Multimodalité** : texte, image, audio
- 📈 Benchmarks, visualisation, export
- 🔀 Backend modulaire : Torch, ONNX, TF, JAX
- 📦 Support complet Docker + YAML + Makefile
- 🔒 Sécurité, sandboxing, auditabilité
- 🧠 Compatible avec CPU, GPU, edge, cloud

---

## 📙 Documentation

| Lien                         | Description                              |
|------------------------------|------------------------------------------|
| [`docs/index.md`](docs/index.md)            | Vue d’ensemble                           |
| [`docs/qstar_llm.md`](docs/qstar_llm.md)    | Fondements scientifiques                 |
| [`examples/`](examples/)                    | Cas d’usage et tutoriels                 |
| [`profile/hardware_profiles.yaml`](profile/hardware_profiles.yaml) | Profils matériels types             |
| [`config/qstar_config.yaml`](config/qstar_config.yaml)   | Paramètres dynamiques                    |

---

## 💬 Cas d’usage concrets

- 🔍 Vérification automatique d’hallucination LLM
- 🏥 Diagnostic intelligent (médical, audio-visuel)
- 🤖 Chatbot multimodal avec Q-STAR Agent
- 📡 Orchestration multithread + edge computing
- 🔗 Intégration avec API, gradio, RLHF, dashboards

---

## 🧠 Contribuer à l’évolution

```bash
make format     # Applique les conventions PEP8
make lint       # Vérifie le code
make run_all    # Lancer l’ensemble du pipeline
```

👥 Contributions bienvenues via `CONTRIBUTING.md`

---

## 📜 Citation académique

```bibtex
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

## ✨ Framework modulaire d’avenir

Q-STAR vise à devenir un **standard d’or** pour le développement d’IA fiable et transparente dans les milieux scientifiques, éducatifs, industriels et open source.

> 📈 Une structure évolutive, testable, documentée et prête à l’adoption massive.

📨 Rejoins le mouvement sur [GitHub](https://github.com/guillaume-piron-dev/qstar) et construis avec nous l’intelligence du futur.

## 🦠 Liens utiles

- 🌍 Démo Hugging Face : [Q-STAR sur HF Spaces](https://huggingface.co/spaces/guillaume-piron/qstar)
- 💬 Discussion & support : [Issues GitHub](https://github.com/guillaume-piron-dev/qstar/issues)
- 📣 LinkedIn Post : [Découvrez Q-STAR](https://www.linkedin.com/...)

> ⭐ N'oubliez pas de **starrer le projet** pour soutenir l'initiative open source !
  ✨ Version stable déployée avec pipelines CI complets, installation CPU-friendly et compatibilité TF/JAX assurée.

