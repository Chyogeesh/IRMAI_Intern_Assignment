User Input
   ↓
Streamlit Web Interface
   ↓
Input Sent to Hugging Face Model (Hosted)
   ↓
Explanation Received → Query Neo4j → Get Related Nodes
   ↓
Graph and Explanation Displayed to User
project/
├── app.py              # Streamlit app
├── graph_utils.py      # Neo4j connection and query
├── hf_utils.py         # Hugging Face model inference
├── requirements.txt
└── README.md
