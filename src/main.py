from tkinter import *

master = Tk()
master.title("Centilator 2019 [Alpha 1.0]")
master.geometry("500x500")

def bc():
    import basic_calculator.py

def sc():
    import scientific_calculator.py

Label(master, text="Centilator 2019 [Indev 1.0]").pack()

Button(master, text="Basic Calculator", command=lambda: bc()).pack()

master.mainloop()
