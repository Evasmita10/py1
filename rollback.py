import psycopg2 as pg
conn = pg.connect(
    host="localhost",
   database="postgres",
    user="postgres",
    password="evasmita",
    port="5432"
)
cur = conn.cursor()
try:
  cur.execute("""
  INSERT INTO library(book_name, author_name, price)
  VALUES (%s, %s, %s)""", ("Think and grow rich", "Napoleon Hill", 350))
  conn.commit()
  print("inserted successfully!")

except Exception as e :
 conn.rollback()
 print("Error occured,changes undone")

cur.close()
conn.close()
