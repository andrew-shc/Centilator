from tkinter import *
from src.lib import *
from src._calculation import *

def main(master):
    rt = master
    clear_w(rt)

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

    def callTtl():
        txt = inp.get()
        ans = expression1(txt)[0]
        answer.set("Total: "+str(ans))
        tapeFnc("\n"+txt)
        tapeFnc("\n= "+str(ans))

    def insertKey(key, var):
        var.insert(END, key)

    def clear(var): var.delete(0, END)

    def oppose(var):
        if var.get()[0] == "-": var.delete(0)
        else: var.insert(0, "-")

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

    Label(rt, text="Scientific Calculator").pack(anchor="n")
    Button(rt, text="Back", command=lambda: back(rt)).pack(anchor="ne")

    #Button(KPD_SUP, text="PHI", height=1, width=3).pack(side=LEFT)
    Button(KPD_SUP, text="E", command=lambda: print("E"), height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_SUP, text="PI", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_SUP, text="A/C", command=lambda: clear(inp), height=1, width=3, bg="#ffffff").pack(side=LEFT)
    Button(KPD_SUP, text="+/-", command=lambda: oppose(inp), height=1, width=3, bg="#ffffff").pack(side=LEFT)
    Button(KPD_SUP, text="\u0025", command=lambda: insertKey("\u0025", inp), height=1, width=3, bg="#ffffff").pack(side=LEFT)  # percent
    Button(KPD_SUP, text="\u00F7", command=lambda: insertKey("\u00F7", inp), height=1, width=3, bg="#ff9900").pack(side=LEFT)  # divide
    Button(KPD_TOP, text="LN", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_TOP, text="LOG", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_TOP, text="1", command=lambda: insertKey("1", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_TOP, text="2", command=lambda: insertKey("2", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_TOP, text="3", command=lambda: insertKey("3", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_TOP, text="\u00D7", command=lambda: insertKey("\u00D7", inp), height=1, width=3, bg="#ff9900").pack(side=LEFT) # multiply
    Button(KPD_MID, text="CHS", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_MID, text="X!", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_MID, text="4", command=lambda: insertKey("4", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_MID, text="5", command=lambda: insertKey("5", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_MID, text="6", command=lambda: insertKey("6", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_MID, text="\u2212", command=lambda: insertKey("\u2212", inp), height=1, width=3, bg="#ff9900").pack(side=LEFT) # subtract
    Button(KPD_BOT, text="2RT", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_BOT, text="POW", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_BOT, text="7", command=lambda: insertKey("7", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_BOT, text="8", command=lambda: insertKey("8", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_BOT, text="9", command=lambda: insertKey("9", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_BOT, text="\u002B", command=lambda: insertKey("\u002B", inp), height=1, width=3, bg="#ff9900").pack(side=LEFT) # plus
    Button(KPD_SUB, text="MOD", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_SUB, text="RND", height=1, width=3, bg="#ddeeff").pack(side=LEFT)
    Button(KPD_SUB, text="0", command=lambda: insertKey("0", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_SUB, text="00", command=lambda: insertKey("00", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_SUB, text=".", command=lambda: insertKey(".", inp), height=1, width=3, bg="#dddddd").pack(side=LEFT)
    Button(KPD_SUB, text="=", command=lambda: callTtl(), height=1, width=3, bg="#ff9900").pack(side=LEFT)

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
