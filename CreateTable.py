import sqlite3
conn = sqlite3.connect("mydatabase.db")#connecting to a database
cursor = conn.cursor()
cursor.execute("""CREATE TABLE cars
                  (Id int, Carname text, Price INT) 
               """)
print("Table Created")

