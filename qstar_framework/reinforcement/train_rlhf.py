# qstar/reinforcement/train_rlhf.py

from trl import PPOTrainer, PPOConfig
from transformers import AutoTokenizer, AutoModelForCausalLM
from qstar.core.verifier import QStarVerifier
import torch

# Configuration PPO
config = PPOConfig(
    model_name="gpt2",
    batch_size=4,
    learning_rate=1e-5,
    log_with=None  # Peut être remplacé par "wandb"
)

# Chargement modèle/tokenizer
tokenizer = AutoTokenizer.from_pretrained(config.model_name)
model = AutoModelForCausalLM.from_pretrained(config.model_name).to("cuda" if torch.cuda.is_available() else "cpu")

# Vérificateur Q-STAR pour feedback RLHF
verifier = QStarVerifier()

def reward_fn(prompt, response):
    score = verifier.score(prompt, response)
    penalty = 0.2 if verifier.detect_hallucination(response) else 0.0
    return score - penalty

# Initialisation PPO Trainer
ppo_trainer = PPOTrainer(
    config=config,
    model=model,
    tokenizer=tokenizer,
    reward_fn=reward_fn
)

# Exemples simples
sample_prompts = [
    "Décris les symptômes de la grippe.",
    "Quels sont les effets du réchauffement climatique ?"
]

# Entraînement boucle PPO
for prompt in sample_prompts:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    generated_ids = model.generate(input_ids, max_new_tokens=100)
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    reward = reward_fn(prompt, response)
    ppo_trainer.step([prompt], [response], [reward])

    print(f"\n🧪 Prompt : {prompt}")
    print(f"🧠 Réponse : {response}")
    print(f"🏅 Récompense : {reward:.4f}")
