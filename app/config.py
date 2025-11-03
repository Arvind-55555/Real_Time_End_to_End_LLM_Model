from pydantic import BaseSettings

class Settings(BaseSettings):
    # General
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080

    # Embedding model
    EMBED_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    DEVICE: str = "cuda" if __import__("torch").cuda.is_available() else "cpu"

    # Vector DB (chroma)
    CHROMA_DIR: str = "/data/chroma_db"

    # Generation model (causal)
    GEN_MODEL: str = "gpt2"  # replace with your production model or API
    MAX_GEN_TOKENS: int = 256

    # Kafka
    KAFKA_BOOTSTRAP: str = "kafka:9092"
    KAFKA_TOPIC: str = "ingest-topic"

    # Security
    API_KEY: str = ""

settings = Settings()
