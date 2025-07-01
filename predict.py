model.save_pretrained("finetuned_flan_model")
tokenizer.save_pretrained("finetuned_flan_model")
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_pretrained("finetuned_flan_model")
tokenizer = AutoTokenizer.from_pretrained("finetuned_flan_model")
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("finetuned_flan_model")
model = AutoModelForSeq2SeqLM.from_pretrained("finetuned_flan_model")

def get_explanation(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example
text = "user_id: 102, timestamp: 2023-09-28 12:03:00, metric: cpu, value: 98"
print(get_explanation(text))
