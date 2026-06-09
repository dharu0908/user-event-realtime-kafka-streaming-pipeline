import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = int(os.getenv("DB_PORT", 5432))
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DB = os.getenv("DB_NAME", "postgres")

try:
conn = psycopg2.connect(
host=HOST,
port=PORT,
user=USER,
password=PASSWORD,
dbname=DB
)

```
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM user_events ORDER BY timestamp DESC LIMIT 10;"
)
rows = cursor.fetchall()

print("Last 10 events in RDS:")
for row in rows:
    print(row)

cursor.execute("SELECT COUNT(*) FROM user_events;")
count = cursor.fetchone()[0]

print(f"\nTotal events in table: {count}")
```

except Exception as e:
print(f"Database Error: {e}")

finally:
if 'cursor' in locals():
cursor.close()

```
if 'conn' in locals():
    conn.close()
```
