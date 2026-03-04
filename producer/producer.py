import json
import time
import random
import os
from datetime import datetime
from faker import Faker
from kafka import KafkaProducer
from dotenv import load_dotenv

load_dotenv()

fake = Faker()

# ── Kafka Producer ──────────────────────────────────────────────────────────
producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Weighted distribution — realistic e-commerce funnel
# Most users view, fewer add to cart, even fewer purchase
EVENT_TYPES = ["view", "add_to_cart", "purchase"]
EVENT_WEIGHTS = [0.70, 0.20, 0.10]

TOPIC = "user_events"

print("Kafka Producer started... Sending events.")

# ── Produce Events ──────────────────────────────────────────────────────────
while True:
    event = {
        "user_id":    random.randint(1, 100),
        "product_id": random.randint(1, 50),
        "event_type": random.choices(EVENT_TYPES, weights=EVENT_WEIGHTS, k=1)[0],
        "timestamp":  datetime.utcnow().isoformat()
    }

    producer.send(TOPIC, event)
    print(f"Sent → {event}")
    time.sleep(1)
