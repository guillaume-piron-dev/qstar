# scripts/run.py
import argparse
import subprocess
from qstar.hardware.hardware_profile import HardwareProfile
from qstar.hardware.calibration import CalibrationManager
from qstar.hardware.fallback import fallback_message
from qstar.hardware.log_monitor import log_system_event

def run_module(module_name):
    profile = HardwareProfile()
    config = CalibrationManager().get_config()
    log_system_event(f"Profil détecté : {profile.profile}")
    fallback_message()

    modules = {
        "rlhf": "python qstar/reinforcement/train_rlhf.py",
        "api": "python api/app_fastapi.py",
        "vision": "python qstar/models/vision/inference.py",
        "text": "python qstar/models/text/generate.py",
        "gradio": "python api/gradio_launcher.py"
    }

    if module_name not in modules:
        print(f"❌ Module '{module_name}' inconnu. Modules disponibles : {list(modules.keys())}")
        return

    print(f"🚀 Lancement du module : {module_name}")
    subprocess.run(modules[module_name], shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lanceur central des modules Q-STAR")
    parser.add_argument("module", help="Nom du module à exécuter (ex: rlhf, api, vision, text, gradio)")
    args = parser.parse_args()

    run_module(args.module)