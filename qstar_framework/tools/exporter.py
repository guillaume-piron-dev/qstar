# tools/exporter.py
import json
import csv
from pathlib import Path

class Exporter:
    def __init__(self, save_dir="exports"):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(exist_ok=True, parents=True)

    def to_json(self, data, filename="output.json"):
        path = self.save_dir / filename
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return str(path)

    def to_csv(self, data, filename="output.csv"):
        path = self.save_dir / filename
        if isinstance(data, list) and all(isinstance(d, dict) for d in data):
            with open(path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            return str(path)
        raise ValueError("Les données doivent être une liste de dictionnaires")

if __name__ == "__main__":
    sample_data = [
        {"étape": "init", "résultat": 0.98},
        {"étape": "vérification", "résultat": 0.95},
    ]
    exp = Exporter()
    print("✅ Export JSON :", exp.to_json(sample_data))
    print("✅ Export CSV :", exp.to_csv(sample_data))
