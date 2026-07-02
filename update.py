import psycopg2 as pg
conn = pg.connect(
    host="localhost",
   database="postgres",
    user="postgres",
    password="evasmita",
    port="5432"
)
cur = conn.cursor()

query = """
UPDATE library
SET price = %s
WHERE book_name = %s
"""

cur.execute(query, (550, "Atomic Habits"))
conn.commit()

print("updated successfully!")

cur.close()
conn.close()