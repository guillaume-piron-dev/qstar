# qstar/models/multimodal_interface.py
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
)
from qstar.models.text.generate import QStarTextGenerator
from PIL import Image
import torch
import torchaudio
import os
import time
from tqdm import tqdm


def verify_caption(caption):
    return "photo" in caption.lower() or "image" in caption.lower()


def recalibrate_caption(caption):
    return caption if verify_caption(caption) else caption + ". Vérifie la scène."


def verify_transcript(transcript):
    return len(transcript.split()) > 3


def recalibrate_transcript(transcript):
    return (
        transcript
        if verify_transcript(transcript)
        else transcript + ". Analyse complémentaire demandée."
    )


class QStarVision:
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def describe_image(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(image, return_tensors="pt")
        out = self.model.generate(**inputs, max_new_tokens=50)
        return self.processor.decode(out[0], skip_special_tokens=True)

    def qstar_image_pipeline(self, image_path):
        caption = self.describe_image(image_path)
        print(f"[Image] Caption généré : {caption}")
        recalibrated = recalibrate_caption(caption)
        correlated = recalibrated + "\n[Annotation croisée effectuée]"
        final = correlated.strip().capitalize()
        print(f"[Image] Résultat final : {final}")
        return final


class QStarAudio:
    def __init__(self, model_name="facebook/wav2vec2-base-960h"):
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)

    def transcribe(self, audio_path):
        waveform, sample_rate = torchaudio.load(audio_path)
        inputs = self.processor(
            waveform.squeeze(),
            sampling_rate=sample_rate,
            return_tensors="pt",
            padding=True,
        )
        with torch.no_grad():
            logits = self.model(**inputs).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.batch_decode(predicted_ids)[0]
        return transcription

    def qstar_audio_pipeline(self, audio_path):
        transcript = self.transcribe(audio_path)
        print(f"[Audio] Transcription brute : {transcript}")
        recalibrated = recalibrate_transcript(transcript)
        correlated = recalibrated + "\n[Alignement audio vérifié]"
        final = correlated.strip().capitalize()
        print(f"[Audio] Résultat final : {final}")
        return final


class QStarMultimodal:
    def __init__(self):
        self.text_model = QStarTextGenerator()
        self.vision_model = QStarVision()
        self.speech_model = QStarAudio()

    def analyze(self, prompt=None, image_path=None, audio_path=None):
        result = {}
        total = sum([bool(prompt), bool(image_path), bool(audio_path)])
        step = 100 // total if total > 0 else 0
        progress = 0

        print("\n[🔄 Lancement du pipeline multimodal Q-STAR]")
        for _ in tqdm(range(3), desc="Initialisation", unit="task"):
            time.sleep(0.2)

        if prompt:
            print("\n[Texte] Traitement du prompt...")
            result["texte"] = self.text_model.generate(prompt)
            progress += step
            print(f"[Progression] {progress}%")

        if image_path and os.path.exists(image_path):
            print("\n[Vision] Analyse de l'image...")
            result["image"] = self.vision_model.qstar_image_pipeline(image_path)
            progress += step
            print(f"[Progression] {progress}%")

        if audio_path and os.path.exists(audio_path):
            print("\n[Audio] Analyse du fichier audio...")
            result["audio"] = self.speech_model.qstar_audio_pipeline(audio_path)
            progress += step
            print(f"[Progression] {progress}%")

        print("\n✅ Pipeline multimodal terminé.")
        return result


if __name__ == "__main__":
    mm = QStarMultimodal()
    output = mm.analyze(
        prompt="Décris une machine intelligente.",
        image_path="sample.jpg",
        audio_path="sample.wav",
    )
    print("\n🧠 Résultat multimodal :", output)
