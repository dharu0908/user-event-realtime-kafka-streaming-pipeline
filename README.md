# 🚀 User Event Real-Time Kafka Streaming Pipeline

An end-to-end data engineering project that simulates real-time user activity on an e-commerce platform. Events stream through Kafka into PostgreSQL on AWS RDS, and the collected data is analyzed through Databricks dashboards built on Delta tables.

---

## Architecture


![Databricks Dashboard](databricks%20analytics%20and%20dashboard/Screenshot%202026-03-03%195353.png)

The project is split into two distinct layers:

**Phase 1 — Streaming Ingestion**
A Python producer generates synthetic user events (view, add_to_cart, purchase) using Faker with a realistic weighted distribution — 70% views, 20% add-to-cart, 10% purchases. Events are published to a Kafka topic running in Docker. A Python consumer reads from that topic and writes each event into a PostgreSQL table on AWS RDS. This ran until ~4,500 rows were collected.

**Phase 2 — Analytics**
The collected data was exported into Databricks and loaded into Delta tables. SQL notebooks query the Delta tables to power dashboards covering conversion rates, top products, top users, and funnel analysis.

Keeping ingestion and analytics as separate layers mirrors how production data platforms are typically structured — the streaming layer doesn't need to know anything about the analytics layer, and vice versa.

---

## Dashboard

![Databricks Dashboard](databricks%20analytics%20and%20dashboard/Screenshot%202026-03-02%20233601.png)

---

## Tech Stack

| Layer | Tool |
|---|---|
| Event Generation | Python, Faker |
| Message Broker | Apache Kafka |
| Infrastructure | Docker, Docker Compose |
| Storage | PostgreSQL on AWS RDS |
| Analytics Storage | Databricks Delta Tables |
| Dashboards | Databricks SQL Notebooks |

---

## Project Structure

```
.
├── producer/
│   └── producer.py
├── consumer/
│   └── consumer.py
├── databricks/
│   ├── Total Customer.dbquery.ipynb
│   ├── Top 10 product.dbquery.ipynb
│   ├── Top 10 users.dbquery.ipynb
│   ├── Purchase_conversion_rate.dbquery.ipynb
│   ├── Conversion of top 10 products.dbquery.ipynb
│   ├── funnel.dbquery.ipynb
│   ├── total_event.dbquery.ipynb
│   ├── total_puchases.dbquery.ipynb
│   └── Screenshot 2026-03-02 233601.png
├── architecture.svg
├── docker-compose.yml
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repo and set up environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your RDS credentials:

```env
KAFKA_BOOTSTRAP_SERVERS=localhost:9092

DB_HOST=your-rds-endpoint.rds.amazonaws.com
DB_PORT=5432
DB_NAME=postgres
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

> ⚠️ Never commit your `.env` file. It is already in `.gitignore`.

### 2. Start Kafka

```bash
docker-compose up -d
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the producer

```bash
python producer/producer.py
```

### 5. Run the consumer

```bash
python consumer/consumer.py
```

Once both are running, events flow into PostgreSQL continuously. Stop when you have enough data, export to Databricks, and run the notebooks.

---

## Sample Event

```json
{
  "user_id": 42,
  "product_id": 17,
  "event_type": "purchase",
  "timestamp": "2025-02-01T10:23:45"
}
```

Events are generated with a weighted distribution to reflect a realistic e-commerce funnel — most users view products, fewer add to cart, even fewer purchase.

---

## Databricks Analytics

Each notebook in the `databricks/` folder answers a specific business question:

| Notebook | What it answers |
|---|---|
| `total_event.dbquery.ipynb` | Overall pipeline throughput |
| `Total Customer.dbquery.ipynb` | Unique users in the dataset |
| `total_puchases.dbquery.ipynb` | Total purchase events |
| `Top 10 product.dbquery.ipynb` | Most interacted-with products |
| `Top 10 users.dbquery.ipynb` | Most active users by event count |
| `Purchase_conversion_rate.dbquery.ipynb` | view → purchase conversion rate |
| `Conversion of top 10 products.dbquery.ipynb` | Per-product conversion breakdown |
| `funnel.dbquery.ipynb` | Full event funnel visualization |

---

## What This Project Demonstrates

- Building a working Kafka producer–consumer pipeline from scratch
- Streaming and persisting event data into a cloud relational database (AWS RDS)
- Managing credentials securely using environment variables
- Separating streaming ingestion from the analytics layer — a pattern common in production data platforms
- Loading data into Databricks Delta tables and running SQL analytics on top
- Answering real business questions (conversion, funnels, top-N) from raw event data

---

## Possible Next Steps

- Add **Spark Structured Streaming** to process and transform events before they hit the database
- Use **Databricks Auto Loader** to incrementally ingest new RDS data automatically
- Introduce **schema validation** with Confluent Schema Registry and Avro
- Set up **monitoring** with Kafka UI or Prometheus + Grafana
- Add a **dbt transformation layer** on top of the Delta tables

---

## Author

**Dharmik** — Data Engineering & Analytics
