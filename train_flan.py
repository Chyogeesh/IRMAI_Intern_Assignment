from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, TrainingArguments, Trainer

# === 1. Model and Dataset Loading ===
MODEL_NAME = "google/flan-t5-small"
dataset = load_dataset("csv", data_files={"train": "data/train.csv"})

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# === 2. Tokenization Function with Instruction Prompt ===
def tokenize(batch):
    prompts = [f"Explain this anomaly:\n{x}" for x in batch["input"]]
    
    model_inputs = tokenizer(
        prompts,
        truncation=True,
        padding="max_length",
        max_length=256,
    )

    with tokenizer.as_target_tokenizer():  # Use this for backward compatibility
        labels = tokenizer(
            batch["target"],
            truncation=True,
            padding="max_length",
            max_length=64,
        )

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# === 3. Tokenize Entire Dataset ===
tokenized = dataset["train"].map(
    tokenize,
    batched=True,
    remove_columns=dataset["train"].column_names
)

# === 4. Load Model and Collator ===
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

# === 5. Define TrainingArguments ===
args = TrainingArguments(
    output_dir="finetuned-flan",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    fp16=False,
    learning_rate=5e-5,
    push_to_hub=True,
    hub_model_id="Yogi0505/flan-t5-anomaly-explainer",
    hub_strategy="every_save",
)

# === 6. Set up Trainer ===
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized,  # ✅ corrected this line
    data_collator=data_collator,
    tokenizer=tokenizer
)

# === 7. Train and Push to Hugging Face Hub ===
trainer.train()
trainer.push_to_hub()
tokenizer.push_to_hub("Yogi0505/flan-t5-anomaly-explainer")
