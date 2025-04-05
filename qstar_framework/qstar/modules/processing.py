# qstar/modules/processing.py
from qstar.models.text.generate import QStarTextGenerator


def traitement_initial(input_data):
    generator = QStarTextGenerator()
    return generator.generate(input_data)
