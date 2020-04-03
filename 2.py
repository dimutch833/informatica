from tkinter import *
 
root = Tk()
 
e = Entry(width=20)
b = Button(text="Агрегатний стан води")
l = Label(bg='black', fg='white', width=20)
 
def make(event):
    s = e.get()
    temp = int(s)
    if temp <= 0:
       l["text"] = "Стан льоду"
    if temp >= 100:
       l["text"] = "Газовий стан води"
    if temp > 0 and temp < 100:
        l["text"] = "Звичний стан води"


b.bind('<Button-1>', make)
 
e.pack()
b.pack()
l.pack()
root.mainloop()
