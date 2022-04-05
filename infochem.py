import os
from tkinter import *
from PIL import ImageTk, Image


mainwindow = Tk()
mainwindow.geometry("1100x550")
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

#img = ImageTk.PhotoImage(Image.open("InfoChem.png"))
label = Label(frame, background="#424F55", text="InfoCHEM", fg="#E67E22", font=("Roboto", 50))
label.pack()

frame4 = Frame(width=93, height=93)
frame4.pack()

frame4.place(anchor='center', relx=0.91, rely=0.131)

img4 = ImageTk.PhotoImage(Image.open("Shield.png"))
label4 = Label(frame4, image=img4, bg="#424F55")
label4.pack()

applyimg = ImageTk.PhotoImage(Image.open("Checked.png"))
button1 = Button(width=93, height=93, image=applyimg, bg="#424F55", command=apply, bd=0)
button1.pack()
button1.place(anchor='center', relx=0.91, rely=0.55)

addimg = ImageTk.PhotoImage(Image.open("Add.png"))
button2 = Button(width=93, height=93, image=addimg, bg="#424F55", command=imput_rule, bd=0)
button2.pack()
button2.place(anchor='center', relx=0.67, rely=0.13)

removeimg = ImageTk.PhotoImage(Image.open("Remove.png"))
button3 = Button(width=93, height=93, image=removeimg, bg="#424F55", command=removerule)
button3.pack()
button3.place(anchor='center', relx=0.77, rely=0.13)

frame2 = Frame(width=800, height=355, bg="#647176")
frame2.pack()
frame2.place(anchor='center', relx=0.40, rely=0.58)

#rulelabel = Label(frame2, text="", bg="#DADAFF")
#rulelabel.pack()
#rulelabel.place(anchor='center', relx=0.10, rely=0.10)

startimg = ImageTk.PhotoImage(Image.open("play.png"))
button3 = Button(width=93, height=93, image=startimg, bg="#424F55", command=stopbutton, bd=0)
button3.pack()
button3.place(anchor='center', relx=0.91, rely=0.35)

stopimg = ImageTk.PhotoImage(Image.open("stop.png"))
button3 = Button(width=93, height=93, image=stopimg, bg="#424F55", command=playbutton, bd=0)
button3.pack()
button3.place(anchor='center', relx=0.91, rely=0.75)

mainwindow.mainloop()
