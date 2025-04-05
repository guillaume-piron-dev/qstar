# qstar/security/security_module.py
import re
from transformers import pipeline

class QStarSecurity:
    def __init__(self):
        self.classifier = pipeline("text-classification", model="facebook/bart-large-mnli")

    def detect_threat(self, text):
        keywords = ["attack", "exploit", "vulnerability", "malware", "unauthorized"]
        found = any(k in text.lower() for k in keywords)
        classified = self.classifier(text)[0]
        return found, classified['label'], classified['score']

    def qstar_security_pipeline(self, text):
        found, label, score = self.detect_threat(text)
        log = f"[Security] Label: {label}, Score: {score:.2f}, Threat Detected: {found}"
        return log