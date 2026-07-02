import psycopg2 as pg
conn = pg.connect(
    host="localhost",
   database="postgres",
    user="postgres",
    password="evasmita",
    port="5432"
)
cur = conn.cursor()
cur.execute("""
CREATE TABLE library(
    id SERIAL PRIMARY KEY,
    book_name VARCHAR(100),
    author_name VARCHAR(100),
    price INTEGER)
""");

conn.commit()
print(" Table Created successfully!")
cur.close()
conn.close()