import psycopg
import redis

# PostgreSQL connection
try:
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="agentic_db",
        user="agentic",
        password="devpassword"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    print("PostgreSQL connected:", cursor.fetchone())

    cursor.execute(
        "SELECT extname FROM pg_extension WHERE extname = 'vector'"
    )
    print("pgvector extension:", cursor.fetchone())

    cursor.close()
    conn.close()

except Exception as e:
    print("PostgreSQL error:", e)


# Redis connection
try:
    r = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )

    r.set("project", "agentic-45")
    print("Redis connected:", r.get("project"))

except Exception as e:
    print("Redis error:", e)