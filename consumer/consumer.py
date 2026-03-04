from kafka import KafkaConsumer
import json
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# ── Kafka Consumer ──────────────────────────────────────────────────────────
consumer = KafkaConsumer(
    'user_events',
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='user-events-consumer-group'
)

print("Kafka Consumer started... Waiting for messages.")

# ── PostgreSQL Connection ───────────────────────────────────────────────────
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 5432)),
    database=os.getenv("DB_NAME", "postgres"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
cur = conn.cursor()

# ── Create Table If Not Exists ──────────────────────────────────────────────
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_events (
        id         SERIAL PRIMARY KEY,
        user_id    INT          NOT NULL,
        product_id INT          NOT NULL,
        event_type VARCHAR(50)  NOT NULL,
        timestamp  TIMESTAMP    NOT NULL
    )
""")
conn.commit()
print("Table 'user_events' is ready.")

# ── Consume & Persist ───────────────────────────────────────────────────────
for msg in consumer:
    event = msg.value

    try:
        cur.execute(
            """
            INSERT INTO user_events (user_id, product_id, event_type, timestamp)
            VALUES (%s, %s, %s, %s)
            """,
            (event['user_id'], event['product_id'], event['event_type'], event['timestamp'])
        )
        conn.commit()
        print(f"Stored → {event}")

    except Exception as e:
        conn.rollback()
        print(f"Failed to store event: {event}\nError: {e}")
