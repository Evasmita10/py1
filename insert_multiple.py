import psycopg2 as pg
conn = pg.connect(
    host="localhost",
   database="postgres",
    user="postgres",
    password="evasmita",
    port="5432"
)
cur = conn.cursor()

records =[
    ("The Alchemist", "Paulo Coelho", 450),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", 400)
]
query = """INSERT INTO library(book_name, author_name, price)VALUES (%s, %s, %s)"""
cur.executemany(query, records)
conn.commit()


print("inserted successfully!")

cur.close()
conn.close()
