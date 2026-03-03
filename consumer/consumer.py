from kafka import KafkaConsumer
import json
import psycopg2
from psycopg2 import sql


consumer = KafkaConsumer(
    'user_events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True
)

print("Kafka Consumer started... Waiting for messages.")


conn = psycopg2.connect(
    host="database-1.cv8wcy8air5c.us-east-2.rds.amazonaws.com",
    port=5432,
    database="postgres",    # replace with your DB name if different
    user="postgres",        # your RDS username
    password="dharmikp" # your RDS password
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS user_events (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL
)
""")
conn.commit()
print("Table 'user_events' is ready in RDS.")


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
        print("Stored in RDS:", event)
    except Exception as e:
        conn.rollback()
        print("Failed to store message:", event, "\nError:", e)
