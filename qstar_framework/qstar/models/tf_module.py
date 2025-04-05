# qstar/models/tf_module.py
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer


class QStarTF:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = TFAutoModelForSequenceClassification.from_pretrained(model_name)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="tf")
        logits = self.model(inputs)[0]
        return tf.argmax(logits, axis=-1).numpy()[0]

    def qstar_tf_pipeline(self, text):
        initial = self.predict(text)
        verified = initial == 1
        recalibrated = initial if verified else (1 - initial)
        correlated = (initial + recalibrated) // 2
        return correlated
