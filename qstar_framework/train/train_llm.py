# train/train_llm.py
from transformers import Trainer, TrainingArguments, AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")

# Prétraitement
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True, remove_columns=["text"])

# Entraînement
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,
    num_train_epochs=1,
    save_total_limit=1,
    logging_dir="./logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    tokenizer=tokenizer
)

trainer.train()
