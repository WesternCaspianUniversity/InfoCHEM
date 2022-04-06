import os
from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="dbadm",passwd="root123!",database="InfoCHEM")
cursordb = connectiondb.cursor()


def login():
    global root2
    root2 = Tk()
    #root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("350x270")
    root2.config(bg="#424F55")

    global username_verification
    global password_verification
    #text = Label(background="#424F55", text="INPUT RULE", fg="#E67E22", font=("Roboto", 25))
    #text.place(x=98, y=30)

    text1=Label(text='InfoCHEM Login Portal', bd=5, bg="#424F55", fg="#E67E22", font=("Roboto", 20, "bold"))
    text1.place(x=17, y=25)

    username_verification = StringVar()
    password_verification = StringVar()

    Label(root2, text="Username :", fg="#E67E22", bg="#424F55" , font=('Roboto', 12, 'bold')).place(x=45,y=95)
    Entry(root2, textvariable=username_verification).place(x=145, y=97)

    Label(root2, text="Password :", fg="#E67E22", bg="#424F55" , font=('Roboto', 12, 'bold')).place(x=45,y=145)
    Entry(root2, textvariable=password_verification, show="*").place(x=145,y=145)

    Button(root2, text="Login", fg="#424F55", bg='#E67E22', relief="ridge", font=('arial', 12, 'bold'),command=login_verification).place(x=145,y=195)
    #Label(root2, text="")

def logged_destroy():

    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    os.system("python secprogram.py")

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("300x100")
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

'''def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut:
        root2.destroy()
    return

def main_display():
    global root
    root = Tk()
    root.config(bg="#424F55")
    root.title("Login System")
    root.geometry("500x500")
    Label(root,text='InfoCHEM Log In System', bd=20, font=('arial', 20, 'bold'), fg="#E67E22",
    bg="#424F55",width=300).pack()

    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="ridge", fg="#424F55",
    bg="#E67E22",command=login).place(x=140,y=150)

    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="ridge", fg="#424F55",
    bg="#E67E22",command=Exit).place(x=140,y=300)
'''
login()
root2.mainloop()