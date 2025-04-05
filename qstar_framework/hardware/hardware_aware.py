# qstar/hardware/hardware_aware.py
import torch
import psutil
import platform
import os
import json


def detect_hardware_profile():
    profile = {
        "device": "cuda" if torch.cuda.is_available() else "cpu",
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        "cpu": platform.processor(),
        "ram_total_gb": round(psutil.virtual_memory().total / (1024**3), 2),
        "os": platform.system() + " " + platform.release(),
        "cores": psutil.cpu_count(logical=True),
        "env": dict(os.environ)
    }
    return profile


def suggest_runtime_config(profile):
    suggestion = {
        "batch_size": 1,
        "precision": "fp32",
        "mode": "async" if profile["device"] == "cuda" else "sync"
    }

    if profile["device"] == "cuda" and profile["ram_total_gb"] > 16:
        suggestion.update({
            "batch_size": 8,
            "precision": "fp16"
        })
    elif profile["ram_total_gb"] < 4:
        suggestion.update({
            "batch_size": 1,
            "mode": "minimal"
        })

    return suggestion


if __name__ == "__main__":
    profile = detect_hardware_profile()
    config = suggest_runtime_config(profile)

    print("\n🖥️ Profil Matériel :")
    print(json.dumps(profile, indent=2))

    print("\n⚙️ Configuration Suggérée :")
    print(json.dumps(config, indent=2))
