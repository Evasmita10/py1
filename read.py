import psycopg2 as pg
conn = pg.connect(
    host="localhost",
   database="postgres",
    user="postgres",
    password="evasmita",
    port="5432"
)
cur = conn.cursor()
cur.execute("SELECT * FROM library")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()