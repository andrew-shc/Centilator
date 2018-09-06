from tkinter import *
from src.basic_calculator import main as bc
from src.scientific_calculator import main as sc

root = Tk()
root.title("Centilator 2019 [Alpha 2.0]")
root.geometry("500x500")

Label(root, text="Centilator 2019 [Alpha 2.0]").pack()

Button(root, text="Basic Calculator", command=lambda: bc(root)).pack()
Button(root, text="Scientific Calculator", command=lambda: sc(root)).pack()

root.mainloop()
