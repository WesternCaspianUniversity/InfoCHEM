import os
from tkinter import *
import tkinter.messagebox
import mysql.connector
from PIL import ImageTk, Image

#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="daadm",passwd="",database="InfoCHEM")
cursordb = connectiondb.cursor()



#global root2


def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    root2.destroy()
    os.system("python3 secprogram.py")
    

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("340x100")
    failed_message.configure(bg="#424F55")
    Label(failed_message, text="Invalid Username or Password", fg="#E67E22", bg="#424F55", font=("Roboto", 12, 'bold')).place(x=30,y=20)
    Button(failed_message,text="Ok", bg="#E67E22", fg="#424F55", relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).place(x=128,y=55)


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from users where username = %s and password = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

root2 = Tk()
root2.title("InfoCHEM Login Portal")
root2.geometry("385x270")
root2.config(bg="#424F55")

global username_verification
global password_verification

little_addimg = ImageTk.PhotoImage(Image.open("login.png"))
little_add=Label(root2, image=little_addimg, bg="#424F55")
little_add.place(x=247,y=15)

text1=Label(text='Login', bd=5, bg="#424F55", fg="#E67E22", font=("Roboto", 20, "bold"))
text1.place(x=47, y=28)


username_verification = StringVar()
password_verification = StringVar()

Label(root2, text="Username", fg="#E67E22", bg="#424F55" , font=('Roboto', 12, 'bold')).place(x=40,y=95)
Entry(root2, textvariable=username_verification).place(x=147, y=95)

Label(root2, text="Password", fg="#E67E22", bg="#424F55" , font=('Roboto', 12, 'bold')).place(x=40,y=145)
Entry(root2, textvariable=password_verification, show="*").place(x=147,y=145)

Button(root2, text="Login", fg="#424F55", bg='#E67E22', relief="ridge", font=('arial', 12, 'bold'),command=login_verification).place(x=145,y=195)



#login()
root2.mainloop()
