# Kafka producer simulation placeholder
import time, json, uuid, random
from kafka import KafkaProducer
from datetime import datetime

KAFKA_BOOTSTRAP = "localhost:9092"
TOPIC = "ingest-topic"

producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

sample_texts = [
    "New research shows transformers can compress representations.",
    "Stock market rises as company reports record profits.",
    "Study links air pollution to cognitive decline.",
    "Local team wins championship after dramatic finish.",
    # ... extend with many more or stream from RSS
]

def run_sim(interval=2.0):
    while True:
        doc = {
            "id": str(uuid.uuid4()),
            "text": random.choice(sample_texts),
            "meta": {"source": "sim", "ts": datetime.utcnow().isoformat()}
        }
        producer.send(TOPIC, value=doc)
        print("Produced:", doc["id"])
        time.sleep(interval)

if __name__ == "__main__":
    run_sim()
