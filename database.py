import mysql.connector as connection
myconn=connection.connect(
    host="localhost",
    user="root",
    password="@asifsaif9661",
    database="ACME"
)

if(myconn.is_connected()):
    print("Connected to db")

x = myconn.cursor()
qry = "SELECT * FROM STUDENTS"
x.execute(qry)
data= x.fetchall()
for i in data:
  print(i)