# qstar/core/interop/backend_selector.py
import importlib
import logging


class BackendSelector:
    def __init__(self):
        self.backends = {
            "torch": self._check_available("torch"),
            "tensorflow": self._check_available("tensorflow"),
            "jax": self._check_available("jax"),
        }

    def _check_available(self, module_name):
        try:
            importlib.import_module(module_name)
            return True
        except ImportError:
            return False

    def get_best_backend(self):
        if self.backends["torch"]:
            return "torch"
        elif self.backends["tensorflow"]:
            return "tensorflow"
        elif self.backends["jax"]:
            return "jax"
        else:
            logging.warning(
                "Aucun backend IA disponible. Veuillez installer torch, tensorflow ou jax."
            )
            return None


if __name__ == "__main__":
    selector = BackendSelector()
    print("Backend IA sélectionné :", selector.get_best_backend())
