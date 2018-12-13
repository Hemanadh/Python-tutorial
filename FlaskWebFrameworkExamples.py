from flask import Flask,request,redirect,url_for
import datetime,os,time
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/123')
def hello123():
    return 'Hello, World 123!'
@app.route('/121')
def hello121():
    return '123'
@app.route('/1211')
def hello1211():
    return '1231'

#Static 
@app.route('/now')
def now():
    return str(datetime.datetime.now())

#Dynamic 
@app.route('/env1')
def env():
    strng="<html>"
    strng+="<head><style>h1 {color:blue;}p {color:blue;}trh1 {color:blue;}</style><title>Env_Variables</title><h1 align='center'>Environment Variables</h1></head>"
    strng+="<body>"
    strng+="<table border=1>"
    for x,y in os.environ.items():
        strng+="<tr><td>{}</td><td>{}</td></tr>".format(x,y)
    strng+="</table>"
    strng+="</body>"
    strng+="</html>"
        
    return strng

#interactive route
@app.route('/wish/<name>')
def wish(name):
    return "<head><h1 align='center'>Hello, {}</h1></head> ".format(name)


#interactive route
@app.route('/wisher/<a>/<b>')
def wisher(a,b):
    return "<head><h1 align='center'> Sum of {} + {} = {}</h1></head>".format(a,b,str(int(a)+int(b)))


#interactive route
@app.route('/info/<filename>')
def info(filename):
    return "<head><h1 align='center'> File name - {} , size - {} , Time - {}</h1></head>".format(filename,os.path.getsize("C:\\Users\\ABRIDGE0\\Desktop\\Day3\\"+filename),time.ctime(os.path.getctime("C:\\Users\\ABRIDGE0\\Desktop\\Day3\\"+filename)))




#interactive route
@app.route('/cars')
def cars():
   
    string="""<head>
<h1 align='center'>Cars</h1>
<style>
table, th, td {
  border: 1px solid black;
  padding: 3px;
}
table {
  border-spacing: 4px;
}
th, td {
  padding: 7px;
}
</style>
</head>"""
    string+="<table border=1 align='center' style='width:25%'>"
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM cars"
    cursor.execute(sql)
    for id1,carname,price in cursor.fetchall():
        string+="<tr align='center'><td>{}</td><td>{}</td><td>{}</td><td><a href='/remove/{}'>X</a></td><td><a href='/edit/{}'>Modify</a></td></tr>".format(id1,carname,price,id1,id1)
    conn.close()
    string+="<table border=1>"
    return string+"""<a href="/addcar" align='center'>Add New Car</a>"""


@app.route("/remove/<cid>")
def remove(cid):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "DELETE FROM cars WHERE Id = {}".format(int(cid))
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for("cars"))

@app.route("/update",methods=["post"])
def update():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
 
    sql = "UPDATE cars SET Id = {}, Carname = '{}',Price = {} WHERE Id = {}".format(int(request.form.get("cid")),request.form.get("brand"),int(request.form.get("price")),int(request.form.get("cid")))
    cursor.execute(sql)
    conn.commit()
    return redirect(url_for("cars"))

@app.route("/edit/<cid>")
def edit(cid):

    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars where Id={}".format(int(cid)))
    cid,brand,price=cursor.fetchone()
    html="""
    <form action='/update' method=post>
    <input type=text name=cid value={}>Car Id<br>
    <input type=text name=brand value={}>Brand<br>
    <input type=text name=price value={}>Price<br>
    <input type=submit><br>
    </form>
    """.format(cid,brand,price)
    
    return html

@app.route("/addnewcar",methods=["post"])
def addnewcar():
    cid=request.form.get("cid")
    brand=request.form.get("brand")
    price=request.form.get("price")
    
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    # insert some data
    sql="INSERT INTO cars VALUES ({},'{}',{})".format(int(cid),brand,int(price))
    cursor.execute(sql)
    # save data to database
    conn.commit()

    #return """<a href="/cars" align='center'>View All Cars</a>"""
    return redirect(url_for("cars"))


@app.route("/addcar")
def addcar():
    html="""
<form action='/addnewcar' method=post>
<input type=text name=cid>Car ID<br>
<input type=text name=brand>Brand<br>
<input type=text name=price>Price<br>
<input type=submit><br>
</form>
"""
    return html










