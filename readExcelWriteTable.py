import sqlite3
import xlrd

conn = sqlite3.connect("mymarks.db")#connecting to a database
cursor = conn.cursor()
# create a table
sql = """
CREATE TABLE marks(
student text,
english int,
maths int,
science int) 
               """
try:
    cursor.execute(sql)
except Exception as e:
    print(e)

wb = xlrd.open_workbook("marks.xls")
ws = wb.sheet_by_index(0)


def importxl(xlsheet,dbtable):
    data=[]
    for x in range(xlsheet.nrows):
        data.append(tuple(xlsheet.row_values(x)))
    sql = "INSERT INTO {} VALUES (?,?,?,?)".format(dbtable)
    try:
        cursor.executemany(sql, data)
    except:
        conn.rollback()
    else:
        conn.commit()
        print("{} row(s) inserted".format(cursor.rowcount))
    finally:
        result=conn.execute("select * from marks")
        print("Rows in the table",result. fetchall())
        conn.close()        

importxl(ws,"marks")



