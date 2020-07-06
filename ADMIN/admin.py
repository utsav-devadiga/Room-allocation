from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image,ImageTk
from tkinter import StringVar,IntVar,ttk
from tkinter import messagebox as mbox
import webbrowser
import pymysql
import os
import ctypes
#import win32console
#import win32gui
#import win32process


conn=pymysql.connect(host='localhost',user='root',password='root',db='project')
cur=conn.cursor(pymysql.cursors.DictCursor)
conn.commit()

print("connection succesfull")

FF_FONT=("action man",22)
F_FONT=("action man",14)
S_FONT=("tahoma",10)
hen=[]

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    global tch49
    tch49 = tk.StringVar()
    global tch50
    tch50 = tk.StringVar()
    top = Toplevel1 (root)
    root.mainloop()



w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)
class Toplevel1:
       def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font9 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        root.iconbitmap('vlogo.ico')
        top.geometry("600x450+698+293")
        top.title("SARAF ROOMS ALLOTMENT")
        top.configure(background="#d9d9d9")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.05, rely=0.067, relheight=0.296
                , relwidth=0.367)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''LOGIN PAGE FOR SARAF FACULTIES''')
        self.Message1.configure(width=220)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.467, rely=0.022, relheight=0.356)
        self.TSeparator1.configure(orient="vertical")

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.017, rely=0.6, relheight=0.14, relwidth=0.233)

        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''ADMIN PASSWORD:''')
        self.Message2.configure(width=140)
        mystring = StringVar()

        self.TEntry1 = ttk.Entry(top,textvariable = mystring)
        self.TEntry1.place(relx=0.233, rely=0.644, relheight=0.047
                , relwidth=0.243)
        self.TEntry1.configure(width=146)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        self.TEntry1.configure(show="*", width=15)
        def getvalue():
            print(mystring.get())
            mystring.get()
       
    
     

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton2 = ttk.Checkbutton(top)
        self.TCheckbutton2.place(relx=0.217, rely=0.756, relwidth=0.218
                , relheight=0.0, height=21)
        self.TCheckbutton2.configure(variable=tch50)
        self.TCheckbutton2.configure(takefocus="")
        self.TCheckbutton2.configure(text='''KEEP ME SIGNED IN''')
        self.TCheckbutton2.configure(width=131)

        
        def login_admin():
            login_message()
            def update():
                top=Toplevel()
                top.geometry("475x291+652+297")
                top.title("UPDATE")
                top.configure(background="#8eb574")
                x=IntVar()
                y=StringVar()
                z=IntVar()
                w=StringVar()
                p=IntVar()
                def run_update():
                   
                    sql= "insert into room (roomid, type, beds, block, rno, taken)"\
                     + " values (%s, %s, %s, %s, %s, %s) "
                    cur.execute(sql, ("'x.get'",'y.get',"'z.get'",'w.get',"'p.get'",'0'))


    
                self.Entry1 = tk.Entry(top,textvariable = x)
                self.Entry1.place(relx=0.253, rely=0.103,height=20, relwidth=0.345)
                self.Entry1.configure(background="white")
                self.Entry1.configure(disabledforeground="#a3a3a3")
                self.Entry1.configure(font="TkFixedFont")
                self.Entry1.configure(foreground="#000000")
                self.Entry1.configure(insertbackground="black")

                self.Entry2 = tk.Entry(top,textvariable = y)
                self.Entry2.place(relx=0.253, rely=0.206,height=20, relwidth=0.345)
                self.Entry2.configure(background="white")
                self.Entry2.configure(disabledforeground="#a3a3a3")
                self.Entry2.configure(font="TkFixedFont")
                self.Entry2.configure(foreground="#000000")
                self.Entry2.configure(insertbackground="black")

                self.Entry3 = tk.Entry(top,textvariable = z)
                self.Entry3.place(relx=0.253, rely=0.412,height=20, relwidth=0.345)
                self.Entry3.configure(background="white")
                self.Entry3.configure(disabledforeground="#a3a3a3")
                self.Entry3.configure(font="TkFixedFont")
                self.Entry3.configure(foreground="#000000")
                self.Entry3.configure(insertbackground="black")

                self.Entry4 = tk.Entry(top,textvariable = w)
                self.Entry4.place(relx=0.253, rely=0.309,height=20, relwidth=0.345)
                self.Entry4.configure(background="white")
                self.Entry4.configure(disabledforeground="#a3a3a3")
                self.Entry4.configure(font="TkFixedFont")
                self.Entry4.configure(foreground="#000000")
                self.Entry4.configure(insertbackground="black")

                self.Entry6 = tk.Entry(top,textvariable = p)
                self.Entry6.place(relx=0.253, rely=0.515,height=20, relwidth=0.345)
                self.Entry6.configure(background="white")
                self.Entry6.configure(disabledforeground="#a3a3a3")
                self.Entry6.configure(font="TkFixedFont")
                self.Entry6.configure(foreground="#000000")
                self.Entry6.configure(insertbackground="black")

                self.Button1 = tk.Button(top,command = run_update)
                self.Button1.place(relx=0.253, rely=0.722, height=64, width=187)
                self.Button1.configure(activebackground="#ececec")
                self.Button1.configure(activeforeground="#000000")
                self.Button1.configure(background="#d9d9d9")
                self.Button1.configure(disabledforeground="#a3a3a3")
                self.Button1.configure(foreground="#000000")
                self.Button1.configure(highlightbackground="#d9d9d9")
                self.Button1.configure(highlightcolor="black")
                self.Button1.configure(pady="0")
                self.Button1.configure(text='''UPDATE''')
                self.Button1.configure(width=187)

                self.Message1 = tk.Message(top)
                self.Message1.place(relx=0.042, rely=0.103, relheight=0.079
                        , relwidth=0.128)
                self.Message1.configure(background="#d9d9d9")
                self.Message1.configure(foreground="#000000")
                self.Message1.configure(highlightbackground="#d9d9d9")
                self.Message1.configure(highlightcolor="black")
                self.Message1.configure(text='''ROOMID''')
                self.Message1.configure(width=60)

                self.Message2 = tk.Message(top)
                self.Message2.place(relx=0.042, rely=0.206, relheight=0.096
                        , relwidth=0.135)
                self.Message2.configure(background="#d9d9d9")
                self.Message2.configure(foreground="#000000")
                self.Message2.configure(highlightbackground="#d9d9d9")
                self.Message2.configure(highlightcolor="black")
                self.Message2.configure(text='''TYPE''')
                self.Message2.configure(width=64)

                self.Message3 = tk.Message(top)
                self.Message3.place(relx=0.042, rely=0.309, relheight=0.079
                        , relwidth=0.086)
                self.Message3.configure(background="#d9d9d9")
                self.Message3.configure(foreground="#000000")
                self.Message3.configure(highlightbackground="#d9d9d9")
                self.Message3.configure(highlightcolor="black")
                self.Message3.configure(text='''BEDS''')
                self.Message3.configure(width=60)

                self.Message4 = tk.Message(top)
                self.Message4.place(relx=0.042, rely=0.412, relheight=0.079
                        , relwidth=0.107)
                self.Message4.configure(background="#d9d9d9")
                self.Message4.configure(foreground="#000000")
                self.Message4.configure(highlightbackground="#d9d9d9")
                self.Message4.configure(highlightcolor="black")
                self.Message4.configure(text='''BLOCK''')
                self.Message4.configure(width=60)

                self.Message5 = tk.Message(top)
                self.Message5.place(relx=0.042, rely=0.515, relheight=0.079
                        , relwidth=0.149)
                self.Message5.configure(background="#d9d9d9")
                self.Message5.configure(foreground="#000000")
                self.Message5.configure(highlightbackground="#d9d9d9")
                self.Message5.configure(highlightcolor="black")
                self.Message5.configure(text='''ROOMNO.''')
                self.Message5.configure(width=60)

                self.Message6 = tk.Message(top)
                self.Message6.place(relx=0.042, rely=0.619, relheight=0.079
                        , relwidth=0.107)
                self.Message6.configure(background="#d9d9d9")
                self.Message6.configure(foreground="#000000")
                self.Message6.configure(highlightbackground="#d9d9d9")
                self.Message6.configure(highlightcolor="black")
                self.Message6.configure(text='''TAKEN''')
                self.Message6.configure(width=60)

                self.Message7 = tk.Message(top)
                self.Message7.place(relx=0.253, rely=0.619, relheight=0.079
                        , relwidth=0.337)
                self.Message7.configure(background="#d9d9d9")
                self.Message7.configure(foreground="#000000")
                self.Message7.configure(highlightbackground="#d9d9d9")
                self.Message7.configure(highlightcolor="black")
                self.Message7.configure(text='''0''')
                self.Message7.configure(width=160)
        

            class Toplevel1_1:
                    top=Toplevel()
                    def __init__(self, top=None):
                    #This class configures and populates the toplevel window.top is the toplevel containing window
                        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
                    _fgcolor = '#000000'  # X11 color: 'black'
                    _compcolor = '#d9d9d9' # X11 color: 'gray85'
                    _ana1color = '#d9d9d9' # X11 color: 'gray85' 
                    _ana2color = '#ececec' # Closest X11 color: 'gray92' 
                    font12 = "-family Rockwell -size 40 -weight normal -slant "  \
                    "roman -underline 0 -overstrike 0"

                    top.geometry("600x450+670+298")
                    top.title("ADMIN")
                    top.configure(background="#c2d89c")
                    top.configure(highlightbackground="#6ee6ef")
    

                    def add_bed():
                        print("beds gonna be added soon...........")
                        mbox.showinfo("ADDING BEDS","YOU WILL BE ADDING BEDS....")
                        update()
                    def add_room():
                        print("rooms gonna be added soon...........")
                        mbox.showinfo("ADDING ROOMS","YOU WILL BE ADDING ROOMS....")
                        update()
                        
                    def add_block():
                        print("blocks gonna be added soon...........")
                        mbox.showinfo("ADDING BLOCKS","YOU WILL BE ADDING BLOCKS....")
                        update()
                    def add_student():
                        print("student is gonna be added soon...........")
                        mbox.showinfo("ADDING STUDENTS","YOU WILL BE ADDING STUDENTS....")

                    self.Button1 = tk.Button(top,command = add_room )
                    self.Button1.place(relx=0.017, rely=0.422, height=64, width=197)
                    self.Button1.configure(activebackground="#ececec")
                    self.Button1.configure(activeforeground="#000000")
                    self.Button1.configure(background="#d9d9d9")
                    self.Button1.configure(cursor="hand2")
                    self.Button1.configure(disabledforeground="#a3a3a3")
                    self.Button1.configure(foreground="#000000")
                    self.Button1.configure(highlightbackground="#d9d9d9")
                    self.Button1.configure(highlightcolor="black")
                    self.Button1.configure(pady="0")
                    self.Button1.configure(text='''ADD ROOMS''')
                    self.Button1.configure(width=197)

                    self.Button2 = tk.Button(top,command = add_block )
                    self.Button2.place(relx=0.383, rely=0.422, height=64, width=157)
                    self.Button2.configure(activebackground="#ececec")
                    self.Button2.configure(activeforeground="#000000")
                    self.Button2.configure(background="#d9d9d9")
                    self.Button2.configure(cursor="hand2")
                    self.Button2.configure(disabledforeground="#a3a3a3")
                    self.Button2.configure(foreground="#000000")
                    self.Button2.configure(highlightbackground="#d9d9d9")
                    self.Button2.configure(highlightcolor="black")
                    self.Button2.configure(pady="0")
                    self.Button2.configure(text='''ADD BLOCKS''')
                    self.Button2.configure(width=157)

                    self.Button3 = tk.Button(top,command = add_bed )
                    self.Button3.place(relx=0.683, rely=0.422, height=64, width=167)
                    self.Button3.configure(activebackground="#ececec")
                    self.Button3.configure(activeforeground="#000000")
                    self.Button3.configure(background="#d9d9d9")
                    self.Button3.configure(cursor="hand2")
                    self.Button3.configure(disabledforeground="#a3a3a3")
                    self.Button3.configure(foreground="#000000")
                    self.Button3.configure(highlightbackground="#d9d9d9")
                    self.Button3.configure(highlightcolor="black")
                    self.Button3.configure(pady="0")
                    self.Button3.configure(text='''ADD BEDS''')
                    self.Button3.configure(width=167)

                    self.Message1 = tk.Message(top)
                    self.Message1.place(relx=0.067, rely=0.089, relheight=0.229
                    , relwidth=0.6)
                    self.Message1.configure(background="#d9d9d9")
                    self.Message1.configure(font=font12)
                    self.Message1.configure(foreground="#000000")
                    self.Message1.configure(highlightbackground="#d9d9d9")
                    self.Message1.configure(highlightcolor="black")
                    self.Message1.configure(text='''__ADMIN__''')
                    self.Message1.configure(width=360)

                    self.Button4 = tk.Button(top,command = add_student )
                    self.Button4.place(relx=0.017, rely=0.622, height=74, width=197)
                    self.Button4.configure(activebackground="#ececec")
                    self.Button4.configure(activeforeground="#000000")
                    self.Button4.configure(background="#9fe889")
                    self.Button4.configure(cursor="hand2")
                    self.Button4.configure(disabledforeground="#a3a3a3")
                    self.Button4.configure(foreground="#000000")
                    self.Button4.configure(highlightbackground="#d9d9d9")
                    self.Button4.configure(highlightcolor="black")
                    self.Button4.configure(pady="0")
                    self.Button4.configure(text='''ADD STUDENT''')
                    self.Button4.configure(width=197)

                    def quit_1():
                        print("time to say good bye!!!!")
                        root.destroy()

                    self.Button5 = tk.Button(top,command = quit_1 )
                    self.Button5.place(relx=0.367, rely=0.644, height=64, width=357)
                    self.Button5.configure(activebackground="#ececec")
                    self.Button5.configure(activeforeground="#000000")
                    self.Button5.configure(background="#bc4f5a")
                    self.Button5.configure(cursor="hand2")
                    self.Button5.configure(disabledforeground="#a3a3a3")
                    self.Button5.configure(foreground="#000000")
                    self.Button5.configure(highlightbackground="#000000")
                    self.Button5.configure(highlightcolor="black")
                    self.Button5.configure(pady="0")
                    self.Button5.configure(text='''LOGOUT''')
                    self.Button5.configure(width=357)

                    def link():
                        webbrowser.open("http://www.rset.edu.in/gscc/")



                    self.Button6 = tk.Button(top,command = link )
                    self.Button6.place(relx=0.683, rely=0.0, height=164, width=177)
                    self.Button6.configure(activebackground="#ececec")
                    self.Button6.configure(activeforeground="#000000")
                    self.Button6.configure(background="#d9d9d9")
                    self.Button6.configure(cursor="hand2")
                    self.Button6.configure(disabledforeground="#a3a3a3")
                    self.Button6.configure(foreground="#000000")
                    self.Button6.configure(highlightbackground="#d9d9d9")
                    self.Button6.configure(highlightcolor="black")
                    self._img2 = tk.PhotoImage(file="./saraf.png")
                    self.Button6.configure(image=self._img2)
                    self.Button6.configure(pady="0")
                    self.Button6.configure(text='''Button''')
                    self.Button6.configure(width=177)

                    self.Button7 = tk.Button(top)
                    self.Button7.place(relx=0.017, rely=0.844, height=64, width=247)
                    self.Button7.configure(activebackground="#ececec")
                    self.Button7.configure(activeforeground="#000000")
                    self.Button7.configure(background="#d9d9d9")
                    self.Button7.configure(disabledforeground="#a3a3a3")
                    self.Button7.configure(foreground="#000000")
                    self.Button7.configure(highlightbackground="#d9d9d9")
                    self.Button7.configure(highlightcolor="black")
                    self.Button7.configure(pady="0")
                    self.Button7.configure(text='''CANCELATION''')
                    self.Button7.configure(width=247)
        def login_message():
            mbox.showinfo("LOGIN STATUS","You Are Bieng Succesfully Logged In")
        def button_clicked():
                    if mystring.get()== 'secret':
                        getvalue()
                        login_admin()
                    else:
                        getvalue()
                        ppopup=tk.Toplevel()
                        ppopup.title("DENIED")
                        ppopup.geometry("300x300")
                        pic=Image.open('ad.png')
                        ren=ImageTk.PhotoImage(pic)
                        w1=tk.Label(ppopup,image=ren)
                        w1.image=ren
                        w1.pack()
                        inv=tk.Label(ppopup,text="INVALID PASSWORD",font=F_FONT)
                        inv.pack(side=tk.TOP)
        
        self.Button1 = tk.Button(top,command = button_clicked )
        self.Button1.place(relx=0.533, rely=0.778, height=84, width=257)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(cursor="hand2")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''LOGIN''')
        self.Button1.configure(width=257)
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.517, rely=0.111, height=171, width=254)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="./Ghanshyamdas-Saraf-College-of-Arts-and-Commerce.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=254)

if __name__ == '__main__':
    vp_start_gui()

