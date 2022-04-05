from tkinter import *
import os

root = Tk()
root.geometry("400x250")
root.configure(bg="#424F55")

'''Functions'''
def cancel():
    root.destroy()

def add_rule_without_port():

    cred="pkexec iptables -A OUTPUT -d " + ipentry.get() + " -j " + modentry.get() + " && pkexec iptables -L "
    os.system(cred)
    root.destroy()

'''Buttons'''
button1 = Button(text="Add", bg="#FDD365", command=add_rule_without_port)
button1.place(x=85,y=200)

button2 = Button(root,text="Cancel", bg="#FDD365", command=cancel)
button2.place(x=250,y=200)

'''Text Labels'''
text=Label(background="#424F55", text="INPUT RULE", fg="#E67E22", font=("Roboto", 25))
text.place(x=98,y=30)

text1=Label(text="Source IP Address: ", bg="#424F55", fg="#FDD365")
text1.place(x=55, y=102)

text2=Label(text="Mode: ", bg="#424F55", fg="#FDD365")
text2.place(x=55, y=150)

'''Entries'''
ipentry=StringVar()
entry1 = Entry(textvariable=ipentry)
entry1.place(x=185, y=100)

modentry=StringVar()
entry2 = Entry(textvariable=modentry)
entry2.place(x=185, y=150)

root.mainloop()
