# 🚀 Real Time End to End LLM Model

This repository provides a **production-ready pipeline** for building, deploying, and running a **real-time end-to-end Large Language Model (LLM) system**.

It integrates **data ingestion, embedding, semantic retrieval (RAG), and text generation** into one deployable and scalable service with Docker and Kubernetes support.

---

## 🧩 Repository Structure

```
Real_Time_End_to_End_LLM_Model/
├── app/                        # Core application logic
│   ├── api.py                  # FastAPI routes for ingest, query, answer (RAG API)
│   ├── main.py                 # Entry point for running the API service
│   ├── ingest.py               # Document ingestion & embedding pipeline
│   ├── embeddings.py           # Handles embedding generation via SentenceTransformers
│   ├── retriever.py            # Chroma-based semantic search retriever
│   ├── generator.py            # LLM text generation (GPT2 or HF model)
│   ├── config.py               # Environment variables and global settings
│   └── utils.py                # Helper functions (if needed)
│
├── infra/
│   ├── docker-compose.yml      # Docker Compose setup (app + Kafka + Chroma DB)
│   ├── Dockerfile              # Docker image for API service
│   └── k8s/                    # Kubernetes deployment manifests
│       ├── deployment.yaml     # API deployment spec
│       ├── service.yaml        # K8s LoadBalancer service
│       └── chroma-pvc.yaml     # Persistent volume for Chroma DB
│
├── producers/
│   └── kafka_producer_sim.py   # Simulated Kafka producer sending live text data
│
├── tests/
│   └── test_api.py             # Unit tests for API endpoints
│
├── .github/workflows/
│   └── ci.yml                  # CI/CD pipeline for testing and Docker image build
│
├── requirements.txt            # Python dependencies
└── README.md                   # (this file)
```

---

## ⚙️ Features

✅ **Real-time ingestion** — uses Kafka for continuous data streaming  
✅ **Embeddings** — powered by SentenceTransformers  
✅ **Semantic Search** — persistent vector database (Chroma)  
✅ **RAG (Retrieval-Augmented Generation)** — context-aware LLM answering  
✅ **FastAPI microservice** — production-grade REST API  
✅ **Docker & Kubernetes** — containerized & deployable stack  
✅ **CI/CD** — GitHub Actions pipeline for build & test  
✅ **Scalable & extensible** — easily plug in Weaviate/Milvus or Ollama/OpenAI models  

---

## 🧠 Quick Start

### 1️⃣ Local setup (Docker Compose)
```bash
docker compose -f infra/docker-compose.yml up --build
```

### 2️⃣ Send data for ingestion
```bash
curl -XPOST "http://localhost:8080/ingest" -H "Content-Type: application/json" -d '[{"id":"1","text":"AI is revolutionizing industries."}]'
```

### 3️⃣ Query or generate
```bash
curl -XPOST "http://localhost:8080/answer" -H "Content-Type: application/json" -d '{"query":"What is AI?"}'
```

---

## 🚀 Deployment Options

- **Local development** — via Docker Compose
- **Production** — deploy using Kubernetes manifests (`infra/k8s/`)
- **Cloud-native** — integrate with managed vector stores (Weaviate/Milvus) and hosted LLMs

---

## 🧰 Technologies Used

- **Python 3.10**
- **FastAPI + Uvicorn**
- **Kafka (real-time ingestion)**
- **SentenceTransformers**
- **ChromaDB / FAISS**
- **Transformers (Hugging Face)**
- **Docker, Kubernetes**
- **GitHub Actions (CI/CD)**

---

