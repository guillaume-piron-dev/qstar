# qstar/modules/recalibrator.py
from transformers import AutoModelForCausalLM, AutoTokenizer


def recalibrer_resultat(output_text, is_valid, model_name="gpt2"):
    if is_valid:
        return output_text  # Rien à recalibrer

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    inputs = tokenizer(f"Corrige ceci : {output_text}", return_tensors="pt")
    outputs = model.generate(
        inputs.input_ids, max_new_tokens=50, do_sample=True, temperature=0.5
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
