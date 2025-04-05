# qstar/core/learning/adaptive_trainer.py
import json
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
import torch


class AdaptiveTrainer:
    def __init__(
        self,
        model_name="gpt2",
        eval_log_path="eval_log.json",
        output_dir="./adapted_model",
    ):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.eval_log_path = eval_log_path
        self.output_dir = output_dir
        self.min_score_threshold = 0.9

    def load_high_score_texts(self):
        if not os.path.exists(self.eval_log_path):
            raise FileNotFoundError("Fichier d'historique d'évaluation introuvable.")

        with open(self.eval_log_path, "r") as f:
            records = json.load(f)

        high_quality_texts = []
        for entry in records:
            if entry["score"] >= self.min_score_threshold:
                full_text = f"{entry['input']} {entry['output']}"
                high_quality_texts.append(full_text)

        if not high_quality_texts:
            raise ValueError(
                "Aucune donnée d'entraînement de qualité suffisante trouvée."
            )

        return high_quality_texts

    def fine_tune(self):
        train_texts = self.load_high_score_texts()
        encodings = self.tokenizer(
            train_texts, truncation=True, padding=True, return_tensors="pt"
        )

        class SimpleDataset(torch.utils.data.Dataset):
            def __init__(self, enc):
                self.enc = enc

            def __len__(self):
                return len(self.enc["input_ids"])

            def __getitem__(self, idx):
                return {key: val[idx] for key, val in self.enc.items()}

        dataset = SimpleDataset(encodings)

        args = TrainingArguments(
            output_dir=self.output_dir,
            overwrite_output_dir=True,
            per_device_train_batch_size=2,
            num_train_epochs=1,
            logging_dir="./logs",
            logging_steps=10,
        )

        trainer = Trainer(model=self.model, args=args, train_dataset=dataset)

        trainer.train()
        self.model.save_pretrained(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)
        print("✅ Apprentissage auto-adaptatif Q-STAR terminé.")


if __name__ == "__main__":
    trainer = AdaptiveTrainer()
    trainer.fine_tune()
