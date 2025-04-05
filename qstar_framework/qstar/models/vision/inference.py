# qstar/models/vision/inference.py
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch


class QStarImageClassifier:
    def __init__(self, model_name="google/vit-base-patch16-224"):
        self.processor = AutoImageProcessor.from_pretrained(model_name)
        self.model = AutoModelForImageClassification.from_pretrained(model_name)

    def classify(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        return self.model.config.id2label[predicted_class_idx]


if __name__ == "__main__":
    clf = QStarImageClassifier()
    print("📷 Prédiction :", clf.classify("sample.jpg"))
