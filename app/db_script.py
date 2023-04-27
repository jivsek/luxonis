import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Jelenovgreben123",
    host="localhost",
    port="5432"
)

conn.autocommit = True

cursor = conn.cursor()

# Create the sreality database
cursor.execute("CREATE DATABASE sreality")

# Open a cursor to perform database operations
cur = conn.cursor()

# Connect to sreality database
conn = psycopg2.connect(
    dbname="sreality",
    user="postgres",
    password="Jelenovgreben123",
    host="localhost",
    port="5432"
)
print(conn.status_code)
# Create a new table to store the JSON data
cur.execute("""
    CREATE TABLE IF NOT EXISTS apartments (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        images JSONB
    );
""")

print("Database created successfully!")

# Close the cursor and connection
cursor.close()
conn.close()
