from tkinter import *

while True:
    win=Tk()
    win.title("Shrek")
    lbl=Label(win, text="Shrek!", fg='green', font=("Helvetica", 16))
    lbl.place(x=60, y=50)
    win.geometry("300x200+10+20")
    win.mainloop()
