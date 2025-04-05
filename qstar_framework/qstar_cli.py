# qstar_cli.py
import argparse
from qstar.qstar_core import QStarPipeline
from qstar.models.llm_interface import QStarLLM
from qstar.security.security_module import QStarSecurity
from qstar.hardware.hardware_aware import QStarHardware

parser = argparse.ArgumentParser(description="Interface CLI pour Q-STAR")
parser.add_argument("--mode", choices=["core", "llm", "security", "hardware"], required=True)
parser.add_argument("--input", type=str, help="Texte à traiter")
args = parser.parse_args()

if args.mode == "core":
    pipe = QStarPipeline()
    res = pipe.run(args.input)
    print("[Q-STAR] Résultat:", res)
    print("[Logs]")
    for log in pipe.get_logs():
        print(" ", log)

elif args.mode == "llm":
    model = QStarLLM()
    print("[LLM]", model.qstar_wrap(args.input))

elif args.mode == "security":
    sec = QStarSecurity()
    print(sec.qstar_security_pipeline(args.input))

elif args.mode == "hardware":
    hw = QStarHardware()
    print(hw.qstar_hardware_info())