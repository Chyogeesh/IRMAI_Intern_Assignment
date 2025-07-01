from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Replace with your actual Hugging Face repo name (e.g., your-username/flan-t5-anomaly-explainer)
model_id = "your-username/flan-t5-anomaly-explainer"

# Push tokenizer and model
model.push_to_hub(model_id)
tokenizer.push_to_hub(model_id)

huggingface-cli login
