# qstar/hardware/calibration.py
from qstar.hardware.hardware_profile import HardwareProfile

class CalibrationManager:
    def __init__(self):
        self.profile = HardwareProfile().profile

    def get_config(self):
        if self.profile == "PI4_Light":
            return {
                "batch_size": 1,
                "max_length": 64,
                "use_gpu": False,
                "threads": 2
            }
        elif self.profile == "Basic_Low_RAM":
            return {
                "batch_size": 2,
                "max_length": 128,
                "use_gpu": False,
                "threads": 4
            }
        elif self.profile == "Standard_Desktop":
            return {
                "batch_size": 4,
                "max_length": 256,
                "use_gpu": False,
                "threads": 6
            }
        elif self.profile == "Pro_GPU":
            return {
                "batch_size": 8,
                "max_length": 512,
                "use_gpu": True,
                "threads": 8
            }
        elif self.profile == "Datacenter_Heavy":
            return {
                "batch_size": 16,
                "max_length": 1024,
                "use_gpu": True,
                "threads": 16
            }
        else:
            return {
                "batch_size": 2,
                "max_length": 128,
                "use_gpu": False,
                "threads": 4
            }

if __name__ == "__main__":
    cal = CalibrationManager()
    print("Configuration adaptée :")
    print(cal.get_config())
