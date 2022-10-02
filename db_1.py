import mysql.connector
x=int(input('enter your Choice \n 1.Student result \n 2.Student Details\n 3.student_attendence '))
y=int(input('select option \n 1.insert \n 2.delete \n 3.update'))

if(x==1):
    if(y==1):
     standard=input('enter the standard :')
     reg_no=input('enter the reg_no  :')
     mark_1=input('enter the mark_1 :')
     mark_2=input('enter the mark_2  :')
     mark_3=input('enter the mark_3 :')
     mark_4=input('enter the mark_4 :')
     mark_5=input('enter the mark_5 :')
     myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
     cur=myconn.cursor()
     sql_insert='insert into student_result(standard,reg_no,mark_1,mark_2,mark_3,mark_4,mark_5) values(%s,%s,%s,%s,%s,%s,%s)'
     val=(standard,reg_no,mark_1,mark_2,mark_3,mark_4,mark_5)
     try:
        cur.execute(sql_insert,val)
        myconn.commit()
     except:
        myconn.rollback()
     print(cur.rowcount,'record inserted successfully!!')
     myconn.close()
     print('student result ')

    
    if(y==2):   
      myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
      cur=myconn.cursor()
      sql_delete_="""delete from student_result where name=%s  """
      try:
         cur.execute(sql_delete)
         myconn.commit()
      except:
         myconn.rollback()
      print(cur.rowcount,'record deleted successfully!!')
      myconn.close()
      print('student result ')


    if(y==3):
        myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
        cur=myconn.cursor()
        sql_update="""update student_result set %s where %s"""

        try:
          cur.execute(sql_update)
          myconn.commit()
        except:
          myconn.rollback()
        print(cur.rowcount,'record update successfully!!')
        myconn.close()
        print('student result ')




#***************************************************************************************

if(x==2):
    if(y==1):
    
     reg_no=input('enter the reg_no  :')
     name=input('enter the name :')
     father_name=input('enter the father_name  :')
     address=input('enter the address :')
     phone_no=input('enter the phone_no :')
     gender=input('enter the gender :')
     nationality=input('enter the nationality :')

     myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
     cur=myconn.cursor()
     sql_insert='insert into student_details(reg_no,name,father_name,address,phone_no,gender,nationality) values(%s,%s,%s,%s,%s,%s,%s)'
     val=(reg_no,name,father_name,address,phone_no,gender,nationality)
     
     try:
         cur.execute(sql_insert,val)
         myconn.commit()
     except:
        myconn.rollback()
     print(cur.rowcount,'record inserted successfully!!')
     myconn.close()
     print('student result ')

    if(y==2):   
      myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
      cur=myconn.cursor()
      sql_delete="""delete from student_details where %s """
      try:
         cur.execute(sql_delete)
         myconn.commit()
      except:
         myconn.rollback()
      print(cur.rowcount,'record deleted successfully!!')
      myconn.close()
      print('student result ')


      
    if(y==3):
        myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
        cur=myconn.cursor()
        sql_update="""update student_details set %s where %s """

        try:
          cur.execute(sql_update)
          myconn.commit()
        except:
          myconn.rollback()
        print(cur.rowcount,'record update successfully!!')
        myconn.close()
        print('student result ')

#***************************************************************************************

        

if(x==3):
    if(y==1):
     reg_no=input('enter the reg_no  :')
     name=input('enter the name :')
     date=input('enter the date :')
     attendence=input('enter the attendence :')
     myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
     cur=myconn.cursor()
     sql_insert='insert into student_attendence(reg_no,name,date,attendence) values(%s,%s,%s,%s)'
     val=(reg_no,name,date,attendence)
     try:
         cur.execute(sql_insert,val)
         myconn.commit()
     except:
        myconn.rollback()
     print(cur.rowcount,'record inserted successfully!!')
     myconn.close()
     print('student result ')

    if(y==2):   
      myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
      cur=myconn.cursor()
      sql_delete="""delete from student_attendence where %s """
      try:
         cur.execute(sql_delete)
         myconn.commit()
      except:
         myconn.rollback()
      print(cur.rowcount,'record deleted successfully!!')
      myconn.close()
      print('student result ')


      
    if(y==3):
        myconn=mysql.connector.connect(host='localhost',user='root',passwd='',database='student')
        cur=myconn.cursor()
        sql_update="""update student_attendence set %s where attendence=%s"""

        try:
          cur.execute(sql_update)
          myconn.commit()
        except:
          myconn.rollback()
        print(cur.rowcount,'record update successfully!!')
        myconn.close()
        print('student result ')

#***************************************************************************************

