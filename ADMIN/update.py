from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image,ImageTk
from tkinter import StringVar,IntVar,ttk
from tkinter import messagebox as mbox
import webbrowser
import pymysql
def vp_start_gui1():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    UPDATE_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 

        top.geometry("475x291+652+297")
        top.title("UPDATE")
        top.configure(background="#8eb574")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.253, rely=0.103,height=20, relwidth=0.345)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.253, rely=0.206,height=20, relwidth=0.345)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.253, rely=0.412,height=20, relwidth=0.345)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.253, rely=0.309,height=20, relwidth=0.345)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.253, rely=0.515,height=20, relwidth=0.345)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.253, rely=0.722, height=64, width=187)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')
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
        self.Message7.configure(text='''Message''')
        self.Message7.configure(width=160)

if __name__ == '__main__':
    vp_start_gui1()





