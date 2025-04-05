# qstar/logging/logger.py
import json
import datetime
from pathlib import Path


class QStarLogger:
    def __init__(self, session_name="default_session", save_path="logs"):
        self.session_name = session_name
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.save_dir = Path(save_path) / self.session_name / self.timestamp
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.logs = []

    def log_step(self, step_name, content):
        entry = {
            "step": step_name,
            "timestamp": datetime.datetime.now().isoformat(),
            "content": content,
        }
        self.logs.append(entry)

    def export_json(self, filename="pipeline_log.json"):
        file_path = self.save_dir / filename
        with open(file_path, "w") as f:
            json.dump(self.logs, f, indent=2)
        return str(file_path)

    def export_txt(self, filename="pipeline_log.txt"):
        file_path = self.save_dir / filename
        with open(file_path, "w") as f:
            for log in self.logs:
                f.write(f"[{log['step']}] {log['timestamp']} : {log['content']}\n")
        return str(file_path)

    def print_latest(self):
        if self.logs:
            last = self.logs[-1]
            print(f"🧩 [{last['step']}] → {last['content']}")

    def print_all(self):
        for log in self.logs:
            print(f"[{log['step']}] {log['timestamp']} : {log['content']}")
