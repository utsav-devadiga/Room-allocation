import tkinter as tk
from tkinter import StringVar,IntVar,ttk
from PIL import Image,ImageTk
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='root',db='project')
print("connection done")
b=conn.cursor(pymysql.cursors.DictCursor)
def update():
    
    sql= "insert into room (roomid, type, beds, block, rno, taken)"\
         + " values (%s, %s, %s, %s, %s, %s) "
    b.execute(sql, ('2344','N','1','A','2','0'))
    conn.commit()

def new_stud():

    sql= "insert into student(studentID, password)"\
         + " values (%s, %s) "
    b.execute(sql,('15BCE0015','UTSAV'))
    conn.commit()
def cancel():
    sql="update room set taken=0 where roomid = %s" 
    b.execute(sql,2011)
    conn.commit()



update()
sql= ("insert into room (roomid=%s, type=%s, beds=%s, block=%s, rno=%s, taken=%s) ",['+rid.get()','+t.get(),+be.get()','+bl.get()','+rno.get()','+tn.get()'])
