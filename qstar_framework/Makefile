# 🛠️ Makefile – Q-STAR Framework complet

init-pyproject:
	python scripts/init_pyproject.py


PYTHON=python
SCRIPT_DIR=scripts
TEST_DIR=tests
SRC=qstar

.PHONY: install train run run-pipeline run-multimodal export-onnx benchmark security clean test format docker-build help

# 📦 Installation des dépendances
install:
	pip install -r requirements.txt

# 🔁 Entraînement LLM
train:
	$(PYTHON) train/train_llm.py

# ▶️ Exemple pipeline
run-pipeline:
	$(PYTHON) examples/example_pipeline.py

# ▶️ Exemple multimodal
run-multimodal:
	$(PYTHON) examples/example_multimodal.py

# 🔄 Export ONNX
export-onnx:
	$(PYTHON) tools/export_onnx.py

# 📊 Benchmark
benchmark:
	$(PYTHON) tools/benchmark.py

# 🛡️ Analyse sécurité
security:
	$(PYTHON) tools/security_scan.py

# 🧹 Nettoyage des outputs/logs
clean:
	$(PYTHON) $(SCRIPT_DIR)/clean_outputs.py

# ✅ Tests unitaires
test:
	pytest $(TEST_DIR)

test-full:
	@echo "🧪 Lancement complet des tests + couverture"
	coverage run -m pytest
	coverage report -m
	flake8 qstar
	black --check qstar
	bandit -r qstar

# 🎨 Formatage
format:
	black $(SRC) $(SCRIPT_DIR) $(TEST_DIR)

# 🐳 Docker build
docker-build:
	docker build -t qstar:latest .

# 📘 Aide
help:
	@echo "\nCommandes disponibles :"
	@echo "  make install           📦 Installer les dépendances"
	@echo "  make train             🔁 Entraînement du modèle"
	@echo "  make run-pipeline      ▶️  Pipeline Q-STAR (exemple)"
	@echo "  make run-multimodal    ▶️  Pipeline multimodal"
	@echo "  make export-onnx       🔄 Export ONNX"
	@echo "  make benchmark         📊 Mesures de performance"
	@echo "  make security          🛡️  Analyse sécurité"
	@echo "  make test              ✅ Tests unitaires"
	@echo "  make clean             🧹 Nettoyage outputs/logs"
	@echo "  make format            🎨 Formatage du code"
	@echo "  make docker-build      🐳 Build image Docker"
	@echo "  make help              📘 Ce menu"
