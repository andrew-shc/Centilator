from tkinter import *

rt = Tk()
rt.title("Centilator 2019 [Indev 1.0]")
rt.geometry("500x500")

fSUP = Frame(rt)
KPD_SUP = Frame(rt)
KPD_TOP = Frame(rt)
KPD_MID = Frame(rt)
KPD_BOT = Frame(rt)
KPD_SUB = Frame(rt)
fSUB = Frame(rt)
fTOP = Frame(rt)

answer = StringVar()
answer.set("")

def calc(equ):
    return eval(equ)

def callTtl():
    txt = inp.get()
    ans = calc(txt)
    total(ans)
    tapeFnc("\n"+txt)
    tapeFnc("\n= "+str(ans))

def insertKey(key, var):
    var.insert(END, key)

def clear(var): var.delete(0, END)

def oppose(var):
    if var.get()[0] == "-": var.delete(0)
    else: var.insert(0, "-")

def total(ans): answer.set(ans)

def toggleTape():
    global hidden
    if hidden: tape.pack()
    else: tape.pack_forget()
    hidden = not hidden

def tapeFnc(txt):
    tape.insert(END, txt)

inp = Entry(fSUP)
inp.pack(side=LEFT)

hidden = False
tapeTG = Button(fTOP, text="Tape Mode", command=lambda: toggleTape())
tapeTG.pack(side=TOP)

tape = Text(fTOP)
tape.pack(side=TOP)

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
Button(KPD_SUB, text="=", command=lambda: callTtl()).pack(side=LEFT)

Label(fSUB, textvariable=answer).pack()

fSUP.pack()
KPD_SUP.pack()
KPD_TOP.pack()
KPD_MID.pack()
KPD_BOT.pack()
KPD_SUB.pack()
fSUB.pack()
fTOP.pack()

rt.mainloop()
