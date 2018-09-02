from tkinter import *

rt = Tk()
rt.title("Centilator 2019 [Indev 1.1]")
rt.geometry("500x500")

SUP = Frame(rt)
KPD_SUP = Frame(rt)
KPD_TOP = Frame(rt)
KPD_MID = Frame(rt)
KPD_BOT = Frame(rt)
KPD_SUB = Frame(rt)
SUB = Frame(rt, bg="#ffff00")

def calc(equ):
    return eval(equ)

def get():
    txt = inp.get()
    ans = calc(txt)
    print(ans)

def insertKey(key, var):
    var.insert(END, key)

def clear(var): var.delete(0, END)

def oppose(var):
    if var.get()[0] == "-": var.delete(0)
    else: var.insert(0, "-")

inp = Entry(SUP)
inp.pack()

Button(KPD_SUP, text="A/C", command=lambda: clear(inp)).pack(side=LEFT)
Button(KPD_SUP, text="+/-", command=lambda: oppose(inp)).pack(side=LEFT)
Button(KPD_SUP, text="%", command=lambda: insertKey("1", inp)).pack(side=LEFT)
Button(KPD_SUP, text="/", command=lambda: insertKey("/", inp)).pack(side=LEFT)
Button(KPD_TOP, text="1", command=lambda: insertKey("1", inp)).pack(side=LEFT)
Button(KPD_TOP, text="2", command=lambda: insertKey("2", inp)).pack(side=LEFT)
Button(KPD_TOP, text="3", command=lambda: insertKey("3", inp)).pack(side=LEFT)
Button(KPD_TOP, text="*", command=lambda: insertKey("*", inp)).pack(side=LEFT)
Button(KPD_MID, text="4", command=lambda: insertKey("4", inp)).pack(side=LEFT)
Button(KPD_MID, text="5", command=lambda: insertKey("5", inp)).pack(side=LEFT)
Button(KPD_MID, text="6", command=lambda: insertKey("6", inp)).pack(side=LEFT)
Button(KPD_MID, text="-", command=lambda: insertKey("-", inp)).pack(side=LEFT)
Button(KPD_BOT, text="7", command=lambda: insertKey("7", inp)).pack(side=LEFT)
Button(KPD_BOT, text="8", command=lambda: insertKey("8", inp)).pack(side=LEFT)
Button(KPD_BOT, text="9", command=lambda: insertKey("9", inp)).pack(side=LEFT)
Button(KPD_BOT, text="+", command=lambda: insertKey("+", inp)).pack(side=LEFT)
Button(KPD_SUB, text="0", command=lambda: insertKey("0", inp)).pack(side=LEFT)
Button(KPD_SUB, text=".", command=lambda: insertKey(".", inp)).pack(side=LEFT)
Button(KPD_SUB, text="=", command=lambda: get()).pack(side=LEFT)

SUP.pack()
KPD_SUP.pack()
KPD_TOP.pack()
KPD_MID.pack()
KPD_BOT.pack()
KPD_SUB.pack()
SUB.pack()

rt.mainloop()