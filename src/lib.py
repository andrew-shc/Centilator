from tkinter import *

CALCULATION_RECORDER = []

def clear_w(master):
    for widget in master.winfo_children():
        widget.pack_forget()

def back(master):
    for widget in master.winfo_children():
        if widget.winfo_viewable() == TRUE: widget.destroy()
    for widget in master.winfo_children():
        widget.pack()

def nth_ind(l, chr, n):
    try:
        return [i for i, n in enumerate(l) if n == chr][n]
    except IndexError: return -1

def multi_split_chr(string, delimeter):
    l = [""]
    ind = 0
    for i in string:
        if i in delimeter: ind += 1; l.append("")
        elif l[ind] in delimeter: ind += 1; l.append("")
        l[ind] = l[ind]+i
    return l