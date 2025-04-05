# qstar/core/learning/eval_monitor.py
import json
import time


class EvalMonitor:
    def __init__(self, log_file="eval_log.json"):
        self.log_file = log_file
        self.records = []

    def log_evaluation(self, input_text, output_text, score, model_name="qstar-v1"):
        record = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "model": model_name,
            "input": input_text,
            "output": output_text,
            "score": score,
        }
        self.records.append(record)
        self._save()

    def _save(self):
        with open(self.log_file, "w") as f:
            json.dump(self.records, f, indent=2)

    def load_history(self):
        try:
            with open(self.log_file, "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            self.records = []
        return self.records


if __name__ == "__main__":
    monitor = EvalMonitor()
    monitor.log_evaluation("Quel temps fait-il ?", "Il fait beau.", 0.95)
    print("Derniers logs d’évaluation :")
    print(monitor.load_history())
