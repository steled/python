from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Nur ein Fenster")

Label(root, text="Username").grid(row=0, column=0)
username = Entry(root)
username.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
password = Entry(root, show="*")
password.grid(row=1, column=1)

def callback():
    messagebox.showinfo("Show Password", "Username: " + username.get() + "\nPassword: " + password.get())
#    pw = StringVar()
#    Entry(root, textvariable=pw).grid(row=4, column=0)
#    pw.set(password.get())

Button(root, text="OK", command=callback).grid(row=2, column=0)
Button(root, text="Beenden", command=root.quit).grid(row=2, column=1)

root.mainloop()
