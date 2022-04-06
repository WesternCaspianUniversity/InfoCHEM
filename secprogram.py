import os
from tkinter import *
from PIL import ImageTk, Image


mainwindow = Tk()
mainwindow.geometry("650x450")
mainwindow.title("InfoCHEM")
mainwindow.configure(bg="#424F55")


def imput_rule():
    os.system("python3 command.py")

def apply():
    print("I Don't Know Your Name2")

def removerule():
    print("remove")

def stopbutton():
    os.system("pkexec ufw disable")

def playbutton():
    os.system("pkexec ufw enable")

frame = Frame(width=300, height=55)
frame.pack()
frame.place(anchor='center', relx=0.18, rely=0.12)

label = Label(frame, background="#424F55", text="InfoCHEM", fg="#E67E22", font=("Roboto", 25, 'bold'))
label.pack()

frame4 = Frame(width=93, height=93)
frame4.pack()
frame4.place(anchor='center', relx=0.91, rely=0.131)

img4 = ImageTk.PhotoImage(Image.open("Shield.png"))
label4 = Label(frame4, image=img4, bg="#424F55")
label4.pack()

addimg = ImageTk.PhotoImage(Image.open("Add.png"))
button2 = Button(width=303, height=93, image=addimg, bg="#424F55", command=imput_rule, bd=0)
button2.pack()
button2.place(anchor='center', relx=0.49, rely=0.34)

startimg = ImageTk.PhotoImage(Image.open("play.png"))
button3 = Button(width=303, height=93, image=startimg, bg="#424F55", command=playbutton, bd=0)
button3.pack()
button3.place(anchor='center', relx=0.49, rely=0.60)

stopimg = ImageTk.PhotoImage(Image.open("stop.png"))
button3 = Button(width=303, height=93, image=stopimg, bg="#424F55", command=stopbutton, bd=0)
button3.pack()
button3.place(anchor='center', relx=0.49, rely=0.86)

mainwindow.mainloop()

