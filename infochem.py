import tkinter
from tkinter import *
from PIL import ImageTk, Image

mainwindow = Tk()
mainwindow.geometry("1100x550")
mainwindow.title("InfoCHEM")

frame = Frame(width=300, height=55)
frame.pack()
frame.place(anchor='center', relx=0.18, rely=0.10)

img = ImageTk.PhotoImage(Image.open("InfoChem.png"))
label = Label(frame, image = img)
label.pack()

frame1 = Frame(width=876, height=396)
frame1.pack()
frame1.place(anchor='center', relx=0.44, rely=0.56)

img1 = ImageTk.PhotoImage(Image.open("commands.png"))
label1 = Label(frame1, image = img1)
label1.pack()

frame2 = Frame(width=93, height=93)
frame2.pack()
frame2.place(anchor='center', relx=0.67, rely=0.10)

img2 = ImageTk.PhotoImage(Image.open("Add.png"))
label2 = Label(frame2, image = img2)
label2.pack()

frame3 = Frame(width=93, height=93)
frame3.pack()
frame3.place(anchor='center', relx=0.77, rely=0.10)

img3 = ImageTk.PhotoImage(Image.open("Remove.png"))
label3 = Label(frame3, image = img3)
label3.pack()

frame4 = Frame(width=93, height=93)
frame4.pack()
frame4.place(anchor='center', relx=0.91, rely=0.11)

img4 = ImageTk.PhotoImage(Image.open("Shield.png"))
label4 = Label(frame4, image = img4)
label4.pack()

frame5 = Frame(width=93, height=93)
frame5.pack()
frame5.place(anchor='center', relx=0.91, rely=0.40)

img5 = ImageTk.PhotoImage(Image.open("Checked.png"))
label5 = Label(frame5, image = img5)
label5.pack()

frame6 = Frame(width=93, height=93)
frame6.pack()
frame6.place(anchor='center', relx=0.91, rely=0.72)

img6 = ImageTk.PhotoImage(Image.open("Close.png"))
label6 = Label(frame6, image = img6)
label6.pack()
mainwindow.mainloop()
