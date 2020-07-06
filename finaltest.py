import tkinter as tk
from tkinter import StringVar,IntVar,ttk
from PIL import Image,ImageTk
import pymysql
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox as mbox
import webbrowser
FF_FONT=("action man",22)
F_FONT=("action man",14)
S_FONT=("tahoma",10)
hen=[]
class Application(tk.Tk): #This is the main window
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        tk.Tk.iconbitmap(self,default="vlogo.ico")
        tk.Tk.wm_title(self,"SARAF Hostel Room Allotment System")
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for fram in (loginpage,rdetails,success,reg):
            frame=fram(container,self)
            self.frames[fram]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(loginpage)
        #self.show_frame(reg)
        
    def show_frame(self,cont): # function to show the frame in the main window
        frame=self.frames[cont]
        frame.tkraise()



    
class loginpage(tk.Frame): #This is the login frame
    def __init__(self,parent,controller):
        loginid=StringVar()
        pid=StringVar()
        def loginfunc(lid,password): #checks password
            lid=lid.upper()
            cur.execute("select s.studentID from student s,ainfo a where s.studentID=a.studentID and s.roomID is null order by a.year DESC,a.cgpa DESC;")
            ord=cur.fetchall()
            if(lid==ord[0]['studentID']):
                chance=1
            else:
                chance=0
            if(len(lid)>9 or len(lid)==0):
                popup=tk.Toplevel()
                popup.title("Caution")
                popup.geometry("200x200")
                popup.configure(background="#a1dbcd",bg="#aadbcd")
                inv=tk.Label(popup,text="INVALID REGISTRATION NUMBER")
                pic=Image.open('warn.png')
                ren=ImageTk.PhotoImage(pic)
                w=tk.Label(popup,image=ren)
                w.image=ren
                w.pack()
                inv.pack()
            cur.execute("select password from student where studentID='%s'"%(lid))
            psw=cur.fetchall()
            if(psw[0]['password']==password and chance==1):
                global hen
                hen.append(lid)
                controller.show_frame(reg)
            elif(psw[0]['password']!=password):
                ppopup=tk.Toplevel()
                ppopup.title("Caution")
                ppopup.geometry("250x250")
                pic=Image.open('ad.png')
                ren=ImageTk.PhotoImage(pic)
                w1=tk.Label(ppopup,image=ren)
                w1.image=ren
                w1.pack()
                inv=tk.Label(ppopup,text="INVALID PASSWORD",font=F_FONT)
                inv.pack(side=tk.TOP)
            elif(chance==0):
                hen.append(lid)
                controller.show_frame(reg)
        def aorder():  #function to show the allotment order in a pop up window
            popup1=tk.Tk()
            popup1.title("allotment order")
            popup1.geometry("300x150")
            sb=tk.Scrollbar(master=popup1)
            sb.pack(side=tk.RIGHT,fill=tk.Y)
            listbox=tk.Listbox(master=popup1)
            listbox.pack(side=tk.TOP)
            cur.execute("select s.studentID,a.cgpa,a.year from student s,ainfo a where s.studentID=a.studentID and s.roomID is null;")
            ord=cur.fetchall()
            listbox.insert(tk.END,('RegnNo','|','Year','|','CGPA'))
            for i in range(len(ord)):
                listbox.insert(tk.END,(ord[i]['studentID'],'-',ord[i]['year'],'-',ord[i]['cgpa']))
            listbox.config(yscrollcommand=sb.set)
            sb.config(command=listbox.yview)
            
        tk.Frame.__init__(self,parent)
        photo=tk.PhotoImage(file="vhm.png")
        w=tk.Label(self,image=photo)
        w.image=photo
        w.pack()
        label=tk.Label(self,text="LOGIN PAGE",font=F_FONT)
        label.pack(pady=10,padx=10)
        login=tk.Label(self,text="Reg No",font=F_FONT)
        lo_entry=tk.Entry(self,textvariable=loginid,width=10)
        pas=tk.Label(self,text="Password",font=F_FONT)
        pas_entry=tk.Entry(self,show='*',textvariable=pid)
        login.pack(side=tk.LEFT)
        lo_entry.pack(side=tk.LEFT)
        pas.pack(side=tk.LEFT)
        pas_entry.pack(side=tk.LEFT)
        logbutton=ttk.Button(self,text="Login",command=lambda:loginfunc(loginid.get(),pid.get()))
        logbutton.pack(pady=20,padx=20,side=tk.LEFT)
        rdbutton=ttk.Button(self,text="Room Details",command=lambda: controller.show_frame(rdetails))
        rdbutton.pack(pady=20,padx=20)
        button=ttk.Checkbutton(self,text="Allotment Order",command=lambda:aorder())
        button.pack(pady=20,padx=20)
        
class rdetails(tk.Frame): #This is the room details frame
    def __init__(self,parent,controller):
        blok=StringVar()
        rno=StringVar()
        def rdet(block,rno):
            cur.execute("select * from room where block='%s' and rno=%s"%(block,rno))
            res=cur.fetchall()
            size=res[0]['beds']
            avail=res[0]['taken']
            if(res[0]['Type']=='A'):
                rtype='AC'
            elif(res[0]['Type']=='N'):
                rtype='Non AC'
            if(avail==1):
                avail='No'
            elif(avail==0):
                avail='Yes'
            rinfo=tk.Toplevel()
            rinfo.title("{} Block {} Room info".format(block,rno))
            rinfo.geometry("550x400")
            photo1=tk.PhotoImage(file="map.png")
            w1=tk.Label(rinfo,image=photo1)
            w1.image=photo1
            w1.pack()
            if(size==1):
                p=tk.PhotoImage(file="bed1.png")
                w=tk.Label(rinfo,image=p)
                w.image=p
                w.pack(padx=10,pady=0,side=tk.LEFT)  
            else:
                for k in range(0,int(size/2)):
                    p=tk.PhotoImage(file="bed.png")
                    w=tk.Label(rinfo,image=p)
                    w.image=p
                    w.pack(side=tk.LEFT)
                    
            num=tk.Label(rinfo,text="No of beds={}\nBLOCK={}\nROOM NO:{}\nTYPE:{}\nAVAIL:{}".format(size,block,rno,rtype,avail),font=F_FONT)
            num.pack(pady=10,padx=10,side=tk.TOP)
                
        tk.Frame.__init__(self,parent)
        photo=tk.PhotoImage(file="rdetails.png")
        w=tk.Label(self,image=photo)
        w.image=photo
        w.pack()
        block=tk.Label(self,text="Block:",fg="#383239",bg="#a1dbcd")
        b_ent=tk.Entry(self,textvariable=blok)
        r_no=tk.Label(self,text="Room No:",fg="#383239",bg="#a1dbcd")
        r_ent=tk.Entry(self,textvariable=rno)
        block.pack(pady=10,padx=10)
        b_ent.pack(pady=5,padx=5)
        r_no.pack(pady=10,padx=10)
        r_ent.pack(pady=5,padx=5)
        getinfo=ttk.Button(self,text="Get Room details",command=lambda: rdet(blok.get(),rno.get()))
        getinfo.pack(pady=7,padx=7)
        button=ttk.Button(self,text="Back to Login Page",command=lambda: controller.show_frame(loginpage))
        button.pack()
        
class success(tk.Frame): #This is the success message frame
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        suc=tk.Label(self,text="SUCCESSFULLY REGISTERED",font=FF_FONT)
        suc.pack(side=tk.TOP)
        def show_reg():
            global hen
            for i in hen:
                l1=tk.Label(self,text=str(i),font=F_FONT)
                l1.pack(padx=2,pady=2,side=tk.TOP)
        button=ttk.Checkbutton(self,text="Show Registration Details",command=lambda: show_reg())
        button.pack(pady=20,padx=20)
        button=ttk.Button(self,text="Back to Login Page",command=lambda: controller.show_frame(loginpage))
        button.pack()
        
class reg(tk.Frame): #This is the registration frame
    def __init__(self,parent,controller):
        rno=IntVar()
        def availa(blo,ty,si): #func to show the available rooms
            blo=blo.upper()
            ty=ty.upper()
            if ty=='AC':
                ty='A'
            elif ty=='NON AC':
                ty='N'
            cur.execute("select rno from room where block='%s' and Type='%s' and beds=%d and taken=0"%(blo,ty,si))
            res=cur.fetchall()
            l=tk.Label(self,text="The Following rooms are available",font=F_FONT)
            l.grid()
            tr=''
            for i in range(len(res)):
                tr=tr+'\n'+str(res[i]['rno'])
            l1=tk.Label(self,text=tr,font=F_FONT)
            l1.grid(row=18)
            cf=tk.PhotoImage(file='cb.png')
            cb=tk.Button(self,image=cf,command=lambda:(l.grid_forget(),l1.grid_forget(),rb.grid_forget(),cb.grid_forget(),rs()))
            cb.image=cf
            cb.grid(row=30,column=0,sticky='N',padx=10,pady=10)
            rf=tk.PhotoImage(file='ref.png')
            rb=tk.Button(self,image=rf,command=lambda:(l.grid_forget(),l1.grid_forget(),rb.grid_forget(),cb.grid_forget()))
            rb.image=rf
            rb.grid(row=32,column=0,sticky='N',padx=10,pady=10)
        def rs():
            r1=tk.Label(self,text='enter the selected room number',font=F_FONT)
            r1.grid(row=24)
            r2=tk.Label(self,text='Disclaimer:\nRoom number once selected cannot be changed.',font=S_FONT)
            r2.grid(row=25)
            r_ent=tk.Entry(self,textvariable=rno)
            r_ent.grid(row=26)
            cf=tk.PhotoImage(file='cb.png')
            cb=tk.Button(self,image=cf,command=lambda:(r1.grid_forget(),r2.grid_forget(),r_ent.grid_forget(),cb.grid_forget(),fin()))
            cb.image=cf
            cb.grid(row=30,sticky='S',padx=10,pady=10)
        def fin():
            
            entry=tk.Tk()
            entry.title("Enter Roommates")
            entry.geometry('900x300')
            cur.execute("select roomID,beds from room where rno=%d and block='%s'"%(rno.get(),blok.get()))
            res=cur.fetchall()
            def com():
                    global hen
                    for j in range(0,res[0]['beds']-1):
                        hen.append(ss[j].get())
                    for k in range(0,res[0]['beds']):
                        cur.execute("update student set roomID=%d where studentID='%s'"%(res[0]['roomID'],hen[k]))
                        conn.commit()
                    cur.execute("update room set taken=1 where roomID=%d"%res[0]['roomID'])
                    conn.commit()
                    controller.show_frame(success)
                    entry.destroy()
            if(res[0]['beds']==1):
                s=tk.Label(entry,text='This is a One bed Room and no roommates')
                s.pack()
                r=tk.Button(entry,text="Continue",command=lambda:com())
                r.pack()
            else:  
                ss=[]
                s=tk.Label(entry,text='enter details of roommates')
                s.pack()
                for i in range(0,res[0]['beds']-1):              
                    e=tk.Entry(entry)
                    e.pack(padx=7,pady=7)
                    ss.append(e)
                r=tk.Button(entry,text="Register",command=lambda:com())
                r.pack()
            
        t1=StringVar()
        blok=StringVar()
        capacity=IntVar()
        tk.Frame.__init__(self,parent)
        w=tk.Label(self,text="ROOM ALLOTMENT",font=F_FONT)
        w.grid(row=1,sticky='N',padx=250,pady=10)
        block=tk.Label(self,text="Block:",fg="#383239",bg="#a1dbcd")
        b_ent=tk.Entry(self,textvariable=blok)
        typ=tk.Label(self,text="Type:",fg="#383239",bg="#a1dbcd")
        t_ent=tk.Entry(self,textvariable=t1)
        size=tk.Label(self,text="Beds:",fg="#383239",bg="#a1dbcd")
        s_ent=tk.Entry(self,textvariable=capacity)
        block.grid(row=4,sticky='N',padx=10,pady=10)
        b_ent.grid(row=6,sticky='N',padx=10,pady=10)
        typ.grid(row=8,sticky='N',padx=10,pady=10)
        t_ent.grid(row=10,sticky='N',padx=10,pady=10)
        size.grid(row=12,sticky='N',padx=10,pady=10)
        s_ent.grid(row=14)
        avail=ttk.Button(self,text="Check Availability",command=lambda: availa(blok.get(),t1.get(),capacity.get()))
        avail.grid(row=16,sticky='N',padx=10,pady=10)

    from tkinter import *
    import tkinter as tk
    import tkinter.ttk as ttk
    from PIL import Image,ImageTk
    from tkinter import StringVar,IntVar,ttk
    from tkinter import messagebox as mbox
    import webbrowser
    FF_FONT=("action man",22)
    F_FONT=("action man",14)
    S_FONT=("tahoma",10)
    hen=[]

    def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root
        root = tk.Tk()
        glot.mainloop()



    w = None
    def create_Toplevel1(root, *args, **kwargs):
        '''Starting point when module is imported by another program.'''
        global w, w_win, rt
        rt = root
        w = tk.Toplevel (root)
        top=Toplevell (w)


    class Toplevel:
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
                        def add_room():
                            print("rooms gonna be added soon...........")
                            mbox.showinfo("ADDING ROOMS","YOU WILL BE ADDING ROOMS....")
                        def add_block():
                            print("blocks gonna be added soon...........")
                            mbox.showinfo("ADDING BLOCKS","YOU WILL BE ADDING BLOCKS....")
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
                        self._img1 = tk.PhotoImage(file="./saraf.png")
                        self.Button6.configure(image=self._img1)
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
    op = Toplevel1 (w)
    return (w, top)

    #def destroy_Toplevel1():
    #    global w
    #    w.destroy()
    #    w = None

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
                        def add_room():
                            print("rooms gonna be added soon...........")
                            mbox.showinfo("ADDING ROOMS","YOU WILL BE ADDING ROOMS....")
                        def add_block():
                            print("blocks gonna be added soon...........")
                            mbox.showinfo("ADDING BLOCKS","YOU WILL BE ADDING BLOCKS....")
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
                        self._img1 = tk.PhotoImage(file="./saraf.png")
                        self.Button6.configure(image=self._img1)
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
    obal tch49
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
        t   '''This class configures and populates the toplevel window.
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
                        def add_room():
                            print("rooms gonna be added soon...........")
                            mbox.showinfo("ADDING ROOMS","YOU WILL BE ADDING ROOMS....")
                        def add_block():
                            print("blocks gonna be added soon...........")
                            mbox.showinfo("ADDING BLOCKS","YOU WILL BE ADDING BLOCKS....")
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
                        self._img1 = tk.PhotoImage(file="./saraf.png")
                        self.Button6.configure(image=self._img1)
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
    op = Toplevel1 (w)
        return (w, top)

    #def destroy_Toplevel1():
    #    global w
    #    w.destroy()
    #    w = None

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
                        def add_room():
                            print("rooms gonna be added soon...........")
                            mbox.showinfo("ADDING ROOMS","YOU WILL BE ADDING ROOMS....")
                        def add_block():
                            print("blocks gonna be added soon...........")
                            mbox.showinfo("ADDING BLOCKS","YOU WILL BE ADDING BLOCKS....")
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
                        self._img1 = tk.PhotoImage(file="./saraf.png")
                        self.Button6.configure(image=self._img1)
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

        



conn=pymysql.connect(host='localhost',user='root',password='root',db='project')
cur=conn.cursor(pymysql.cursors.DictCursor)
cur.execute("update student set roomID=NULL")
conn.commit()
app= Application()
app.mainloop()
