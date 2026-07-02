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
INSERT INTO library(book_name, author_name, price)
VALUES (%s, %s, %s)""", ("Atomic Habits", "James Clear", 500))

conn.commit()
print("inserted successfully!")

cur.close()
conn.close()