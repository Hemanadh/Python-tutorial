import sqlite3
 
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
 
print ("listing of all the records in the table:")
for row in cursor.execute("SELECT * FROM cars"):
    print (row)
 
print ("Results")
sql = "SELECT * FROM cars"
cursor.execute(sql)
for id,carname,price in cursor.fetchall():
	print ("The car is {} and its price is {}".format(carname,price))
conn.commit()
conn.close()
