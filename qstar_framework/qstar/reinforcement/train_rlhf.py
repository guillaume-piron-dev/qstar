# Q-STAR: Entraînement TRL (Reinforcement Learning with Human Feedback)
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import PPOTrainer, PPOConfig
from datasets import load_dataset
from qstar.reinforcement.reward_fn import composite_reward


def prepare_model(model_name="gpt2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return tokenizer, model


def prepare_dataset(name="imdb", split="train[:1%]"):
    dataset = load_dataset(name, split=split)
    return dataset["text"]


def train_rlhf():
    config = PPOConfig(
        model_name="gpt2",
        learning_rate=1.41e-5,
        batch_size=4,
        mini_batch_size=2,
        gradient_accumulation_steps=4,
        optimize_cuda_cache=True,
    )

    tokenizer, model = prepare_model(config.model_name)
    texts = prepare_dataset()

    ppo_trainer = PPOTrainer(config, model, tokenizer)

    for epoch, prompt in enumerate(texts):
        if not isinstance(prompt, str) or len(prompt.strip()) == 0:
            continue

        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        response_ids = model.generate(inputs.input_ids, max_new_tokens=30)
        response = tokenizer.decode(response_ids[0], skip_special_tokens=True)

        reward = composite_reward(prompt, response)
        print(f"📊 Époque {epoch} | Récompense : {reward:.4f}")

        ppo_trainer.step([prompt], [response], [reward])

    model.save_pretrained("outputs/ppo_rlhf_qstar")
    tokenizer.save_pretrained("outputs/ppo_rlhf_qstar")
    print("✅ Modèle RLHF entraîné et sauvegardé.")


if __name__ == "__main__":
    train_rlhf()
