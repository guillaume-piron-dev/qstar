# examples/example_pipeline.py
from qstar.core import QStarPipeline

examples = [42, "bonjour", 7.5, "ALGORITHME", 99]

for ex in examples:
    pipeline = QStarPipeline()
    result = pipeline.run(ex)
    print("\nInput:", ex)
    for log in pipeline.get_logs():
        print("  ", log)
    print("Résultat final:", result)
