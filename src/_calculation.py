# this is where all the calculation will be
from src.constants import *


class Error(Exception): __module__ = Exception.__module__

# functions


def multi_split_chr(string, delimeter):
    l = [""]
    ind = 0
    for i in string:
        if i in delimeter: ind += 1; l.append("")
        elif l[ind] in delimeter: ind += 1; l.append("")
        l[ind] = l[ind]+i
    return l

# calculation


def operation(n1, op, n2):
    try:
        n1, n2 = float(n1), float(n2)
    except ValueError:
        raise Error("(EC-A00; ERROR-BAD_CHARACTER) Error Catched: Invalid number; the number must be 'real number' not characters.") from None
    if op == "+": return n1+n2
    elif op == "-": return n1-n2
    elif op == "*": return n1*n2
    elif op == "/": return n1/n2
    elif op == "%": return n1*.01
    elif op == "rt2": return n1**.5
    elif op == "rt3": return -1  # n1**(1/3)
    elif op == "^": return n1**n2
    else: print("Invalid Operator")


def basic_expression(equ):
    i = 0
    while i < len(equ):
        if equ[i] == "*":
            equ.insert(i+2, operation(equ[i-1], equ[i], equ[i+1]))
            del equ[i-1:i+2]
            i -= 1
        elif equ[i] == "/":
            equ.insert(i+2, operation(equ[i-1], equ[i], equ[i+1]))
            del equ[i-1:i+2]
            i -= 1
        i += 1
    i = 0
    while i < len(equ):
        if equ[i] == "+":
            equ.insert(i+2, operation(equ[i-1], equ[i], equ[i+1]))
            del equ[i-1:i+2]
            i -= 1
        elif equ[i] == "-":
            equ.insert(i+2, operation(equ[i-1], equ[i], equ[i+1]))
            del equ[i-1:i+2]
            i -= 1
        i += 1
    return equ


def expression1(equ):
    equ = multi_split_chr(sym_decoder(equ), OPERATION)
    j = 0
    while j < len(equ):
        if equ[j] == "%":
            equ.insert(j, operation(equ[j-1], equ[j], 0))
            del equ[j-1]; del equ[j]
        j += 1
    return basic_expression(equ)


def sym_decoder(equ):
    for i in range(len(equ)):
        if equ[i] in DICTKEY.keys():
            a = DICTKEY[equ[i]]
            equ = equ[:i]+DICTKEY[equ[i]]+equ[i+1:]
    return equ
