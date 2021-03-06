#insert values in to the database
import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
# insert some data
cursor.execute("INSERT INTO cars VALUES (1, 'Audi',5000000)")
# save data to database
conn.commit()
# insert multiple records using the more secure "?" method
mycars = [(2, 'Mercedes', 4500000),
          (3, 'Skoda', 110000),
	  (4, 'Volkswagen', 150000)]
cursor.executemany("INSERT INTO cars VALUES (?,?,?)", mycars)
print("Records Inserted")
conn.commit()

conn.close()

