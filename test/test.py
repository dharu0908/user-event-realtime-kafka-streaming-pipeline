import psycopg2

# RDS connection details
HOST = "database-1.cv8wcy8air5c.us-east-2.rds.amazonaws.com"
PORT = 5432
USER = "postgres"
PASSWORD = "dharmikp"
DB = "postgres"

# Connect to RDS
conn = psycopg2.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, dbname=DB)
cursor = conn.cursor()

# Query to preview events
cursor.execute("SELECT * FROM user_events ORDER BY timestamp DESC LIMIT 10;")
rows = cursor.fetchall()

print("Last 10 events in RDS:")
for row in rows:
    print(row)

# Count total events
cursor.execute("SELECT COUNT(*) FROM user_events;")
count = cursor.fetchone()[0]
print(f"\nTotal events in table: {count}")

# Close connection
cursor.close()
conn.close()
