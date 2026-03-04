# 🚀 User Event Real-Time Kafka Streaming Pipeline

A end-to-end data engineering project that simulates real-time user activity on an e-commerce platform — events flow from a Python producer through Kafka, land in PostgreSQL on AWS RDS, and get analyzed through Databricks dashboards.

Built to demonstrate modern streaming architecture using tools that actually matter in production.

---

## Architecture

![Pipeline Architecture](architecture.svg)

**Python Producer → Apache Kafka → Python Consumer → PostgreSQL (AWS RDS) → Databricks**

Here's how data moves through the system:

1. The **producer** generates synthetic user events using Faker — things like product views, cart additions, and purchases
2. Events get pushed to a Kafka topic running in Docker
3. The **consumer** reads from Kafka and writes records into a PostgreSQL table on AWS RDS
4. **Databricks notebooks** connect to the database via JDBC and power the analytics dashboards

---

## Dashboard

![Databricks Dashboard](Screenshot%202026-03-02%20233601.png)

The dashboards surface key e-commerce metrics — conversion rates, top products, most active users, and total event volume — all refreshed from live data in PostgreSQL.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Event Generation | Python, Faker |
| Message Broker | Apache Kafka |
| Infrastructure | Docker, Docker Compose |
| Storage | PostgreSQL on AWS RDS |
| Analytics | Databricks (SQL + Dashboards) |

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
│   └── total_puchases.dbquery.ipynb
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Start Kafka

```bash
docker-compose up -d
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the producer

```bash
python producer/producer.py
```

### 4. Run the consumer

```bash
python consumer/consumer.py
```

Once both are running, events flow continuously into PostgreSQL. Open your Databricks workspace and run the notebooks to see the dashboards update.

---

## Sample Event

```json
{
  "user_id": 1023,
  "product_id": 451,
  "event_type": "purchase",
  "timestamp": "2025-02-01T10:23:45"
}
```

Three event types are simulated: `view`, `add_to_cart`, and `purchase` — enough to calculate a real purchase conversion funnel.

---

## Databricks Analytics

Each notebook in the `databricks/` folder targets a specific business question:

- **Total Events** — overall pipeline throughput
- **Total Customers** — unique users generating events
- **Total Purchases** — revenue-generating actions
- **Top 10 Products** — most interacted-with items
- **Top 10 Users** — most active users by event count
- **Purchase Conversion Rate** — view → purchase funnel
- **Conversion of Top 10 Products** — per-product conversion breakdown
- **Funnel Analysis** — full event funnel visualization

---

## What This Project Demonstrates

- Setting up a working Kafka producer–consumer pipeline from scratch
- Streaming data from Kafka into a relational database in real time
- Running SQL analytics on live event data using Databricks
- Connecting cloud storage (AWS RDS) with a lakehouse analytics platform
- Building an end-to-end data engineering workflow with free/open-source tooling

---

## Possible Next Steps

- Add **Spark Structured Streaming** to process events before they hit the database
- Introduce **schema validation** with Confluent Schema Registry / Avro
- Set up **monitoring** with Kafka UI or Prometheus + Grafana
- Containerize the consumer and deploy the whole stack to the cloud
- Add **dbt** on top of PostgreSQL for transformation layer

---

## Author

**Dharmik** — Data Engineering & Analytics  
Feel free to connect or reach out if you have questions about the project.
