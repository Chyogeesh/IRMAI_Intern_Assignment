# Step 6: Show anomalies
anomalies = data[data['anomaly'] == 1]
print("🔎 Found", len(anomalies), "anomalies:")
print(anomalies)
from transformers import pipeline

# Load your model from Hugging Face Hub (replace with your username/model_id)
explanation_pipeline = pipeline("text2text-generation", model="your-username/flan-t5-anomaly-explainer")

# Generate explanations
def explain(row):
    prompt = f"User {row['user_id']} had response time {row['response_time']}ms and sent {row['bytes_sent']} bytes. Explain the anomaly."
    output = explanation_pipeline(prompt, max_new_tokens=50)[0]['generated_text']
    return output

anomalies = data[data['anomaly'] == 1].copy()
anomalies['explanation'] = anomalies.apply(explain, axis=1)

# Print and save
print("🔎 Found", len(anomalies), "anomalies with explanations:")
print(anomalies[['timestamp', 'user_id', 'response_time', 'bytes_sent', 'explanation']])
anomalies.to_csv("data/explained_anomalies.csv", index=False)
