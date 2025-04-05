# qstar/models/audio/speech.py
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch


class QStarSpeechRecognizer:
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


if __name__ == "__main__":
    recognizer = QStarSpeechRecognizer()
    print("🔊 Transcription:", recognizer.transcribe("sample.wav"))
