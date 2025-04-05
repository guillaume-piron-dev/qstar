# api/gradio_launcher.py
import gradio as gr
from qstar.models.multimodal_interface import QStarMultimodal

qstar = QStarMultimodal()

def process(prompt, image, audio):
    result = qstar.analyze(prompt, image_path=image.name if image else None, audio_path=audio.name if audio else None)
    return result.get("texte", ""), result.get("image", ""), result.get("audio", "")

demo = gr.Interface(
    fn=process,
    inputs=[
        gr.Textbox(label="Prompt textuel"),
        gr.Image(type="filepath", label="Image"),
        gr.Audio(type="filepath", label="Audio")
    ],
    outputs=[
        gr.Textbox(label="Sortie texte"),
        gr.Textbox(label="Sortie image"),
        gr.Textbox(label="Sortie audio")
    ],
    title="Q-STAR Multimodal",
    description="Démonstration de traitement multimodal : texte, image, audio"
)

demo.launch()
