# qstar/hardware/hardware_aware.py
import torch
import platform

class QStarHardware:
    def __init__(self):
        self.device = self.detect_device()

    def detect_device(self):
        if torch.cuda.is_available():
            return "GPU - CUDA"
        elif torch.backends.mps.is_available():
            return "GPU - Apple MPS"
        elif "arm" in platform.machine():
            return "NPU/ARM"
        else:
            return "CPU"

    def qstar_hardware_info(self):
        return f"[Hardware] Utilisation du périphérique: {self.device}"