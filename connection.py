import psycopg2 as pg
conn = pg.connect(
    host="localhost",
   database="postgres",
    user="postgres",
    password="evasmita",
    port="5432"
)
cur = conn.cursor()
print("Connected successfully!")

cur.close()
conn.close()