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
DELETE FROM library
WHERE book_name = %s
"""
cur.execute(query, ("Atomic Habits",))
conn.commit()
print("deleted successfully!")
cur.close()
conn.close()