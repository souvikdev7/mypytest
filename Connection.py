
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="test")
mycursor = mydb.cursor()
#query = "show databases"
query = "select * from tab1"
mycursor.execute(query)
result = mycursor.fetchall()    #fetchone()
for i in result:
    print(i)