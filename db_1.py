import mysql.connector

name = input("Enter name :")
father_name = input("Enter father_name :")
address=input("Enter address :")
phone_no = input("Enter phone_no :")
gender = input("Enter gender :")
nationality=input("enter nationality :")

myconn = mysql.connector.connect(host="localhost", user="root", passwd="", database="student")
cur = myconn.cursor()
sql = "insert into student_details(name,father_name,address,phone_no,gender, nationality) values(%s, %s, %s,%s,%s,%s)"

val = (name,father_name,address,phone_no,gender, nationality)
try:
    cur.execute(sql, val)

    myconn.commit()
except:
    myconn.rollback()
print(cur.rowcount, "record inserted!")
myconn.close()
