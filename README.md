# User Event Real-Time Kafka Streaming Pipeline

This project demonstrates a real-time event streaming pipeline built using Apache Kafka.  
It simulates user activity events, streams them through Kafka, stores them in PostgreSQL (AWS RDS), and analyzes the data using Databricks dashboards.

The goal of this project is to showcase an end-to-end data engineering workflow using modern streaming architecture.

---

## Architecture

Python Producer → Kafka → Python Consumer → PostgreSQL (AWS RDS) → Databricks Dashboard

### Flow Overview

1. The producer generates synthetic user events such as:
   - view
   - add_to_cart
   - purchase

2. Events are pushed to a Kafka topic.

3. The consumer reads events from Kafka and writes them into a PostgreSQL table.

4. Databricks notebooks connect to PostgreSQL to create analytics dashboards.

---

## Tech Stack

- Apache Kafka
- Python
- Docker & Docker Compose
- PostgreSQL (AWS RDS)
- Databricks (SQL + Dashboards)
- Faker (for data generation)

---

## Project Structure

```
.
├── producer.py
├── consumer.py
├── docker-compose.yml
├── requirements.txt
├── databricks/
│   ├── Total Customer.dbquery.ipynb
│   ├── Top 10 product.dbquery.ipynb
│   ├── Top 10 users.dbquery.ipynb
│   ├── Purchase_conversion_rate.dbquery.ipynb
│   └── Conversion of top 10 products.dbquery.ipynb
└── README.md
```

---

## How to Run

### 1. Start Kafka

```
docker-compose up -d
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Producer

```
python producer.py
```

### 4. Run Consumer

```
python consumer.py
```

Once both are running, events will continuously flow into PostgreSQL.

---

## Sample Event Format

```json
{
  "user_id": 1023,
  "product_id": 451,
  "event_type": "purchase",
  "timestamp": "2025-02-01T10:23:45"
}
```

---

## Dashboards & Analytics

The Databricks notebooks generate insights such as:

- Total events
- Total customers
- Top 10 products
- Top 10 users
- Purchase conversion rate
- Product conversion analysis

---

## What This Project Demonstrates

- Real-time event streaming using Kafka
- Producer–consumer architecture
- Writing streaming data to a relational database
- SQL-based analytics on live event data
- Building an end-to-end data pipeline

---

## Possible Improvements

- Add Spark Structured Streaming
- Introduce schema validation
- Add monitoring and logging
- Containerize the consumer application
- Deploy to cloud infrastructure

---

## Author

Dharmik  
Data Engineering & Analytics
