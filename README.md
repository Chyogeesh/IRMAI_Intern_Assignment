# IRMAI_Intern_Assignment
# AI-Powered Anomaly Detection Platform
A full-stack Python-based project that uses **ClickHouse**, **Neo4j**, and **OpenAI** to detect and explain financial transaction anomalies using UDFs, graphs, and LLMs.

## Architecture

┌────────────── UI ──────────────┐
│ Streamlit / FastAPI │
└──────────────┬────────────────┘
│
┌──────────────▼───────────────┐
│ Python Microservice Layer │
│ - Ingest & UDF Trigger │
│ - Anomaly Explanation │
│ - Neo4j Graph Connector │
└───────┬──────────────┬───────┘
│ │
┌───────▼──────┐ ┌───▼────────┐
│ ClickHouse │ │ Neo4j │
│ (OLAP + UDF) │ │ (GraphDB) │
└──────────────┘ └────────────┘
↘︎ GraphRAG
(Future)

---


---

## ⚙️ Setup Instructions

### 1. 🔧 Prerequisites
- Docker & Docker Compose
- Python 3.11 (for local runs)
- OpenAI API Key (for explanation module)

### 2. 📦 Clone & Setup
3.Create a .env file:
OPENAI_API_KEY=your-openai-key
CLICKHOUSE_HOST=clickhouse
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password
4.Run With Docker
bash
docker-compose up --build
Streamlit UI → http://localhost:8501
FastAPI API → http://localhost:8000
Neo4j UI → http://localhost:7474
ClickHouse → http://localhost:8123


##  Tech Stack

| Component     | Tech Used |
|---------------|-----------|
| Language      | Python 3.11 |
| DB (OLAP)     | ClickHouse |
| Graph DB      | Neo4j |
| LLM APIs      | OpenAI GPT-4 / Hugging Face |
| Frontend      | Streamlit |
| Microservice  | FastAPI |
| Deployment    | Docker / Docker Compose |
| Optional      | Redis Pub/Sub (future ready) |

---

##  Project Structure

.
├── backend/
│ ├── ingest.py # Load CSV to ClickHouse
│ ├── anomaly_detector.py # UDF + detection logic
│ ├── explain_service.py # LLM explanation
│ ├── graph_loader.py # Neo4j entity relationships
│ └── main.py # FastAPI endpoints
│
├── frontend/
│ └── app.py # Streamlit UI
│
├── deploy/
│ ├── Dockerfile
│ └── docker-compose.yml
│
├── data/
│ ├── synthetic_transactions.csv
│ └── flagged_anomalies.csv
│
└── README.md
AI tools are integrated at multiple layers:

1.OpenAI GPT-4 / Hugging Face
Interprets and explains flagged anomalies in plain English
Used in explain_service.py with a structured prompt system

2.ChatGPT & Copilot during Dev
Used for:
Optimizing ClickHouse UDFs
Designing the graph schema
Writing Streamlit/FastAPI UI
Creating test scenarios

3.Future: GraphRAG + LLM
Retrieve graph-based subgraphs for deeper context
Feed this context to LLMs for even richer explanations

| Area                  | Idea                                                 |
| --------------------- | ---------------------------------------------------- |
|  Graph Enhancements | Add fraud rings via GraphRAG and shortest paths      |
|  ML Integration     | Train a classifier on flagged vs normal transactions |
|  Messaging          | Add Kafka/Redis PubSub for real-time ingestion       |
|  Auth               | Add login + role-based access in UI                  |
| Multi-cloud Ready  | Deploy using Terraform on GCP/AWS                    |
| Dashboards         | Add time series + map-based analytics                |




| Tech                   | Role in Project                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **ClickHouse**         | High-speed OLAP database used to store and query 50K+ transaction records. Custom UDFs are created for fast anomaly flagging. |
| **UDFs in ClickHouse** | Detect large transactions, geographic outliers, etc., at query-time using custom functions.                                   |
| **Neo4j**              | Graph database used to model user-location-transaction-type relationships for deeper anomaly context.                         |
| **GraphRAG (planned)** | Used with Neo4j to enrich anomalies by retrieving relevant graph data during explanation.                                     |
| **OpenAI GPT-4**       | Used to explain flagged anomalies in plain language using `describe_anomalies.py`.                                            |
| **Python**             | Orchestration language for ingestion, Neo4j loading, AI API calls, and overall project control.                               |
| **Streamlit**          | Used to create a clean UI to view anomalies and get explanations.                                                             |
| **Docker**             | Used to deploy the app on the cloud with a containerized, reproducible environment.                                           |
| IRMAI Requirement                 | How I Fulfill It                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Strong Python/Golang**          | Project is built using Python. Can be extended to Go if needed.                                              |
| **Microservices & APIs**          | Anomaly detection, AI explanation, and graph enrichment can be modularized into FastAPI-based microservices. |
| **Efficient data handling**       | ClickHouse (OLAP DB) + optimized SQL + UDFs = high-performance detection.                                    |
| **Messaging / PubSub / Firebase** | Easily integrated into anomaly pipeline using Redis, RabbitMQ, or Firebase Pub/Sub.                          |
| **SQL/NoSQL**                     | Uses both ClickHouse (OLAP SQL) and Neo4j (NoSQL GraphDB).                                                   |
| **Quality, secure coding**        | Structured modules, proper validation, Dockerized deployment.                                                |
| **Team Collaboration**            | Clear APIs between backend and frontend. Easily usable by app developers.                                    |
| **Ownership mindset**             | Demonstrated via clean documentation, clear interfaces, extensible architecture.                             |
            ┌────────────────────────────────────────┐
            │          OpenAI/HuggingFace API        │
            └──────────────┬─────────────────────────┘
                           │
        ┌──────────────────▼──────────────────┐
        │     Python Microservice Layer       │
        │  - Data Ingestor                    │
        │  - UDF Trigger Engine               │
        │  - AI Anomaly Explainer             │
        │  - Neo4j Graph Linker               │
        └──────────────────┬──────────────────┘
                           │
        ┌──────────────────▼─────────────────────┐
        │        🛢 ClickHouse (OLAP DB)          │
        └──────────────────┬─────────────────────┘
                           │
        ┌──────────────────▼────────────────────┐
        │        🔗 Neo4j (GraphDB)             │
        └──────────────────┬────────────────────┘
                           │
        ┌──────────────────▼────────────────────┐
        │       🌐 Streamlit or FastAPI UI       │
        └───────────────────────────────────────┘
Detailed Component Breakdown
1. ingest.py — Transaction Loader
Ingests CSV data into ClickHouse using clickhouse_driver.
Uses MergeTree engine and columnar compression for performance.

2. anomaly_detector.py — UDFs for Anomaly Detection
UDFs flag:
High-value transactions
Rare geolocations
Abnormal frequency (can extend using time window logic)
Optimized for batch scanning.

3. explain_service.py — OpenAI/Hugging Face Integration
API to convert raw transaction data into plain English anomaly summaries.
You can extend this with Hugging Face local models if offline.

4. graph_loader.py — Neo4j Graph Modeling
Builds relationships:
User → Transaction
Transaction → Location / Type
Enables future GraphRAG integration.

5. main.py — FastAPI Microservice Layer
API endpoints to:
Trigger detection
Get flagged anomalies
Explain them
Return graph paths

| Requirement                | Fulfilled?    | How                                           |
| -------------------------- | ------------- | --------------------------------------------- |
| Python backend + framework | ✅             | FastAPI + modular services                    |
| Data structures + design   | ✅             | UDFs, batch ingest, graph modeling            |
| Messaging/pubsub           | 🔲 (optional) | Can add Redis or RabbitMQ trigger             |
| SQL/NoSQL                  | ✅             | ClickHouse + Neo4j                            |
| Write & optimize queries   | ✅             | OLAP UDFs in ClickHouse                       |
| Problem solving            | ✅             | Transaction fraud explained in plain language |
| Team alignment             | ✅             | Clean REST API + Streamlit frontend           |
| Ownership                  | ✅             | Dockerized, modular, documented               |
| Learning mindset           | ✅             | Uses latest AI + GraphRAG + OLAP              |

MIT License © 2025 IRMAI Intern Project

---

## 2. `docker-compose.yml`

```yaml
version: '3.9'
services:

  clickhouse:
    image: clickhouse/clickhouse-server
    ports:
      - "8123:8123"
      - "9000:9000"
    volumes:
      - ./data/clickhouse:/var/lib/clickhouse

  neo4j:
    image: neo4j:5
    environment:
      - NEO4J_AUTH=neo4j/your-password
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - ./data/neo4j:/data

  backend:
    build:
      context: .
      dockerfile: deploy/Dockerfile
    command: uvicorn backend.main:app --host 0.0.0.0 --port 8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - clickhouse
      - neo4j

  frontend:
    image: python:3.11
    working_dir: /frontend
    volumes:
      - ./frontend:/frontend
    command: streamlit run app.py --server.port=8501 --server.enableCORS=false
    ports:
      - "8501:8501"
    depends_on:
      - backend

          ┌────────────┐     ┌────────────┐
          │  Data In   │────▶│ ClickHouse │
          └────────────┘     └────┬───────┘
                                   │
                        ┌──────────▼─────────┐
                        │  Anomaly Detection │ (PyOD, IsolationForest)
                        └──────────┬─────────┘
                                   │
         ┌────────────┬────────────▼─────────────┐
         │    Store Anomalies in Neo4j +        │
         │    Extract Graph Features            │
         └────────────┴─────────────────────────┘
                                   │
                       ┌───────────▼────────────┐
                       │  Streamlit / Dashboard │
                       └────────────────────────┘

user_id | timestamp           | page       | response_time
--------|---------------------|------------|---------------
101     | 2025-06-23 10:00:01 | /login     | 120
102     | 2025-06-23 10:00:02 | /checkout  | 550
(John)-[:LOGGED_IN_FROM]->(IP 192.168.1.1)
        ↳ Other anomalies also linked to this IP
[120, 150, 200, 8000, 190, 160]
GET /detect-anomalies?from=2025-06-22&to=2025-06-23
| Component            | Purpose                                 |
| -------------------- | --------------------------------------- |
| **ClickHouse**       | Store and analyze huge time-series data |
| **ML (PyOD)**        | Detect anomalies in data                |
| **Neo4j**            | Add context/relationships to anomalies  |
| **Streamlit**        | Show results visually                   |
| **Backend (Python)** | Connect everything                      |
| **Docker**           | Run all parts smoothly in one place     |
💡 What is Anomaly Detection?
An anomaly is something unusual or unexpected in your data — like a sudden spike in website traffic, a failed login attempt from a strange location, or a drop in server response time.

Anomaly Detection means automatically finding these unusual patterns using logic or machine learning.

🧠 What is AI-Powered Anomaly Detection?
Instead of using simple rules like “value > 1000”, we use AI/ML algorithms to learn patterns and detect what’s abnormal — even if we can’t define it with simple rules.

Example:

Normal: CPU usage between 20-70% most of the time.

Anomaly: Sudden 95% spike lasting 5 minutes → AI flags it.

🗃️ What is ClickHouse?
ClickHouse is a very fast database for analytics — especially for:

Large datasets

Time-series data (like logs, user activity, server metrics)

Real-time queries (for dashboards or ML)
ClickHouse can help query:

“What’s the average response time per page in last 1 hour?”

“Which users made most API calls?”

🧾 What is Neo4j?
Neo4j is a graph database, where data is stored as:

Nodes (entities like people, IPs, logins)

Relationships (edges like “connected_to”, “clicked_on”)

Why Graph?
Graphs help find patterns like:

“Is this anomalous user connected to other suspicious users?”

“Do anomalies cluster around a certain IP/device?”

What is PyOD or ML Anomaly Detection?
PyOD is a Python library with pre-built anomaly detection algorithms.

We can give it data like:

It can tell us:

Normal values: 120, 150, 200, 190, 160

Anomaly: 8000 (way too high)

Algorithms we can use:

Isolation Forest

AutoEncoder (Deep Learning)

One-Class SVM

KNN-based detectors

📊 What is Streamlit / Gradio?
These are Python-based tools to create dashboards and UIs easily.

Why Use Them?
To show anomalies on a chart

Let the user click and explore patterns

Easy to deploy on Hugging Face Spaces

🧰 What is Docker?
Docker lets us run:

ClickHouse

Neo4j

API backend

Frontend UI

… all together in isolated containers that work on any computer.

No dependency issues. One command runs everything.

🌐 What’s the Backend/API?
We’ll use Python + FastAPI or Flask to:

Talk to ClickHouse and Neo4j

Run the ML model

Return results to the frontend

GET /detect-anomalies?from=2025-06-22&to=2025-06-23
| Tool                   | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| **Python (>=3.9)**     | Main programming language                  |
| **Docker Desktop**     | To run ClickHouse and Neo4j easily         |
| **VS Code (optional)** | Editor for writing code                    |
| **Git**                | For version control (optional but helpful) |
anomaly-detector/
│
├── backend/              ← Python APIs
├── data/                 ← Sample input data
├── ml_models/            ← ML code for anomaly detection
├── dashboard/            ← Streamlit or Gradio dashboard
├── neo4j_graph/          ← Graph code for Neo4j
├── docker-compose.yml    ← To run everything
└── README.md             ← Documentation



