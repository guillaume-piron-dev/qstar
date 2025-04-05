# qstar/hardware/hardware_aware.py
import platform
import yaml
from pathlib import Path

class HardwareProfiler:
    def __init__(self, profile_path="profile/hardware_profiles.yaml"):
        self.profile_path = Path(profile_path)
        self.profile = self.detect_and_load()

    def detect_system(self):
        system = platform.system()
        machine = platform.machine()
        if "arm" in machine.lower():
            return "raspberry_pi"
        elif "aarch" in machine.lower():
            return "edge_mobile"
        elif system == "Linux" and "x86_64" in machine:
            return "server_gpu"
        elif system == "Darwin":
            return "workstation"
        return "workstation"

    def detect_and_load(self):
        if not self.profile_path.exists():
            raise FileNotFoundError("Profil matériel introuvable")
        with open(self.profile_path) as f:
            profiles = yaml.safe_load(f)
        key = self.detect_system()
        return profiles.get(key, profiles["workstation"])

    def summary(self):
        return self.profile

if __name__ == "__main__":
    profiler = HardwareProfiler()
    print("🔍 Profil matériel détecté :")
    for k, v in profiler.summary().items():
        print(f"{k} : {v}")