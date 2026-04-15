import psycopg2
from psycopg2 import sql, OperationalError

def connect_to_postgres(host='localhost', port=5432, dbname='vectordb', user='tatun', password=''):
    try:
        conn=psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        print("✅ Connected to PostgreSQL successfully!")
        return conn
    except OperationalError as e:
        print("❌ Unable to connect to the database")
        print(e)
        return None

def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                            CREATE TABLE IF NOT EXISTS users (
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(100),
                                email VARCHAR(100) UNIQUE
                            );
                        """)
            conn.commit()
            print("📦 Table 'users' created or already exists.")


    except Exception as e:
        print("❌ Error creating table:", e)

def insert_data(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                        ('Alice', 'alice@example.com'))
            cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                        ('Bob', 'bob@example.com'))
            conn.commit()
            print("✅ Sample data inserted.")
    except Exception as e:
        print("❌ Error inserting data:", e)

def query_data(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email FROM users;")
            rows = cur.fetchall()
            print("📋 Users in DB:")
            for row in rows:
                print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    except Exception as e:
        print("❌ Error querying data:", e)

if __name__ == '__main__':
    conn = connect_to_postgres(
        dbname='vectordb',
        user='tatun',
        password=''
    )

    if conn:
        create_table(conn)
        insert_data(conn)
        query_data(conn)
        conn.close()