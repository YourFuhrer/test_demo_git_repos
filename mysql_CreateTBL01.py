import mysql.connector

# create object to connect db using mysql.connector.connect() method.
dbobj = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="xyz"
)

# create cusror to point to the db row/s.
dbcurs = dbobj.cursor()

# create execute() to execute SQL query using cursor() method pointer variable.
dbcurs.execute("show databases")

# fetch & store results in variable using fetchone() or fetchall().
dbres = dbcurs.fetchall()

# print stored result.
for x in dbres:
    print(x)
