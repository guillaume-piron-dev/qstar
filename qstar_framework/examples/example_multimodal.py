# examples/example_multimodal.py
from qstar.models.llm_interface import QStarLLM
from qstar.models.multimodal_interface import QStarVision, QStarAudio

text_input = "Décris la situation actuelle de l’IA médicale."
image_path = "sample.jpg"
audio_path = "sample.wav"

# Texte
llm = QStarLLM()
print("[Texte]", llm.qstar_wrap(text_input))

# Image
vision = QStarVision()
print("[Image]", vision.qstar_image_pipeline(image_path))

# Audio
audio = QStarAudio()
print("[Audio]", audio.qstar_audio_pipeline(audio_path))