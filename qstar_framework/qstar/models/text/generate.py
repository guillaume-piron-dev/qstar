# qstar/models/text/generate.py
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm
import time


class QStarTextGenerator:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate(self, prompt, max_tokens=100):
        print("\n⏳ Génération en cours...")
        for _ in tqdm(range(3), desc="Préparation", unit="étape"):
            time.sleep(0.2)

        inputs = self.tokenizer(str(prompt), return_tensors="pt")
        outputs = self.model.generate(
            inputs.input_ids,
            max_new_tokens=max_tokens,
            do_sample=True,
            top_k=50,
            temperature=0.7,
        )

        for _ in tqdm(range(5), desc="Décodage", unit="étape"):
            time.sleep(0.1)

        print("✅ Génération terminée")
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    gen = QStarTextGenerator()
    result = gen.generate("Explique le principe de superposition en physique quantique")
    print("\n🧠 Réponse générée :\n", result)
