# qstar/hardware/hardware_profile.py
import platform
import psutil
import torch

class HardwareProfile:
    def __init__(self):
        self.cpu_info = platform.processor()
        self.architecture = platform.machine()
        self.os = platform.system()
        self.total_ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)  # in GB
        self.gpu_available = torch.cuda.is_available()
        self.gpu_name = torch.cuda.get_device_name(0) if self.gpu_available else "None"
        self.profile = self.classify_profile()

    def classify_profile(self):
        if self.os == "Linux" and "arm" in self.architecture.lower():
            return "PI4_Light"
        elif self.total_ram < 8:
            return "Basic_Low_RAM"
        elif self.gpu_available and "A100" in self.gpu_name:
            return "Datacenter_Heavy"
        elif self.gpu_available:
            return "Pro_GPU"
        else:
            return "Standard_Desktop"

    def summary(self):
        return {
            "OS": self.os,
            "Architecture": self.architecture,
            "CPU": self.cpu_info,
            "RAM (GB)": self.total_ram,
            "GPU Available": self.gpu_available,
            "GPU Name": self.gpu_name,
            "Profile": self.profile
        }

if __name__ == "__main__":
    profile = HardwareProfile()
    print("Profil matériel Q-STAR :")
    for k, v in profile.summary().items():
        print(f"{k}: {v}")
