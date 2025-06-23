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

