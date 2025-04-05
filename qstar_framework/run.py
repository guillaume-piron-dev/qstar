# run.py
import argparse
from qstar.core import QStarPipeline
from qstar.models.llm_interface import QStarLLM
from qstar.models.multimodal_interface import QStarVision, QStarAudio
from qstar.security.security_module import QStarSecurity
from qstar.hardware.hardware_aware import QStarHardware

parser = argparse.ArgumentParser(description="Exécution centralisée de Q-STAR")
parser.add_argument("--mode", choices=["core", "llm", "vision", "audio", "security", "hardware"], required=True)
parser.add_argument("--input", type=str, help="Texte ou chemin vers le fichier à analyser")
args = parser.parse_args()

if args.mode == "core":
    pipeline = QStarPipeline()
    output = pipeline.run(args.input)
    print("[Q-STAR Pipeline]")
    for log in pipeline.get_logs():
        print("  ", log)
    print("Résultat final:", output)

elif args.mode == "llm":
    llm = QStarLLM()
    print("[LLM] Résultat:", llm.qstar_wrap(args.input))

elif args.mode == "vision":
    vision = QStarVision()
    print("[Image] Résultat:", vision.qstar_image_pipeline(args.input))

elif args.mode == "audio":
    audio = QStarAudio()
    print("[Audio] Résultat:", audio.qstar_audio_pipeline(args.input))

elif args.mode == "security":
    sec = QStarSecurity()
    print("[Sécurité]", sec.qstar_security_pipeline(args.input))

elif args.mode == "hardware":
    hw = QStarHardware()
    print(hw.qstar_hardware_info())
