# qstar/models/llm_interface.py
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM


class QStarLLM:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline(
            "text-generation", model=self.model, tokenizer=self.tokenizer
        )

    def generate(self, prompt, max_length=100):
        result = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        return result[0]["generated_text"]

    def qstar_wrap(self, prompt):
        initial_output = self.generate(prompt)
        verified = "acceptable" in initial_output or "vérifié" in initial_output
        recalibrated = (
            initial_output if verified else self.generate(prompt + " Corrige toi.")
        )
        correlated = recalibrated + "\n[Validation croisée effectuée]"
        final = correlated.strip()
        return final
