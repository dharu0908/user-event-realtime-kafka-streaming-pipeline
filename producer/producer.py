import json
import time
import random
from datetime import datetime
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

EVENT_TYPES = ["view", "add_to_cart", "purchase"]

while True:
    event = {
        "user_id": random.randint(1, 100),
        "product_id": random.randint(1, 50),
        "event_type": random.choice(EVENT_TYPES),
        "timestamp": datetime.utcnow().isoformat()
    }

    producer.send("user_events", event)
    print("Sent:", event)
    time.sleep(1)
