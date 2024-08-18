# import mysql.connector
# con is a connection object
con=mysql.connector.connect(host='localhost',user='root',password='Shaikh@786',database='Qr_Code',port='3306')
# if con:
#     print("Connection established Sucessfully")
# else:
#     print("Try again")
# cur_obj=con.cursor()    # cur is a object
# def create():
#     cur_obj.execute("create table if not exists qrdetails(name varchar(30),phone_no varchar(20),course varchar(50),record_date DATE)")

# def add(a,b,c,d):
#     cur_obj.execute("insert into qrdetails(Name,phone_no,course,record_date)"   
#                     "values (%s,%s,%s,%s)",(a,b,c,d)) # for type casting
#     con.commit()
# def view_all_records():
#     cur_obj.execute("select * from qrdetails")
#     data=cur_obj.fetchall()
#     return data
# def view_update():
#     cur_obj.execute("Select distinct course from qrdetails")
#     data = cur_obj.fetchall()
#     return data
# def get_course(x):
#     cur_obj.execute(('Select * from qrdetails where course="{}"'.format(x)))
#     data = cur_obj.fetchall()
#     return data
# def update(x,y,z,n):
#     cur_obj.execute('update qrdetails set phone_no=%s,course=%s,record_data=%s,where name=%s',(x,y,z,n))
#     con.commit()
#     data=cur_obj.fetchall()
#     return data
# def delete(course):
#     cur_obj.execute('delete from qrdetails where course="{}"'.format(course))
#     con.commit()
