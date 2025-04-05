# qstar/models/jax_module.py
import jax.numpy as jnp
from transformers import FlaxAutoModelForSequenceClassification, AutoTokenizer


class QStarJAX:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = FlaxAutoModelForSequenceClassification.from_pretrained(model_name)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="np")
        outputs = self.model(**inputs)
        logits = outputs.logits
        return jnp.argmax(logits, axis=-1).item()

    def qstar_jax_pipeline(self, text):
        initial = self.predict(text)
        verified = initial == 1  # dummy rule
        recalibrated = initial if verified else 1 - initial
        correlated = (initial + recalibrated) // 2
        return correlated
