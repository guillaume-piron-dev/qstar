# scripts/init_pyproject.py

pyproject_content = """
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
""".strip()

with open("pyproject.toml", "w", encoding="utf-8") as f:
    f.write(pyproject_content)

print("✅ Fichier pyproject.toml généré avec succès.")
