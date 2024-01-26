import tkinter as tk
from tkinter import END,messagebox
import math as m
import re

root=tk.Tk()
root.title("Calculadora")
root.config(width=330,height=500)
aux=0
signo=""

def operador(x):
    clear()
    global signo,aux
    signo=x
    aux=txtDisplay.get()
    txtDisplay.delete(0,END)

    regex = re.compile(r'[+-]?\d*\.?\d+') # Acepta numeros + y - asi como decimales y enteros
    if regex.fullmatch(aux):
        aux=float(aux)
        if signo=="n!":
            resultado = 1
            for i in range(2,int(aux)+1):
                resultado = resultado * i
            txtDisplay.insert(0,str(resultado))
            txtOperators.insert(0,f'{aux}! = {resultado}')

        elif signo=="sqrt":
            resultado=m.sqrt(aux)
            txtDisplay.insert(0,str(resultado))  
            txtOperators.insert(0,f'sqrt({aux}) = {resultado}')
    else:
        messagebox.showinfo(message="Caracteres no aceptados", title="Error de Entrada")

def operacion():
    resultado=0
    global signo,aux

    regex = re.compile(r'[+-]?\d*\.?\d+') # Acepta numeros + y - asi como decimales y enteros
    if regex.fullmatch(txtDisplay.get()) :

        if signo=="+":
            resultado=aux+float(txtDisplay.get())
            txtOperators.insert(0,f'{aux} + {float(txtDisplay.get())} = {resultado}')
        elif signo=="-":
            resultado=aux-float(txtDisplay.get())
            txtOperators.insert(0,f'{aux} - {float(txtDisplay.get())} = {resultado}')
        elif signo=="*":
            resultado=aux*float(txtDisplay.get())
            txtOperators.insert(0,f'{aux} x {float(txtDisplay.get())} = {resultado}')
        elif signo=="/":
            if txtDisplay.get() == "0":
                messagebox.showinfo(message="Division entre 0, no valido", title="Error de Calculo")
            else:
                resultado=aux/float(txtDisplay.get())
                txtOperators.insert(0,f'{aux} / {float(txtDisplay.get())} = {resultado}')
        elif signo=="^":
            resultado=aux**float(txtDisplay.get())
            txtOperators.insert(0,f'{aux} ^ {float(txtDisplay.get())} = {resultado}')
        elif signo=="%":
            if txtDisplay.get() == "0":
                messagebox.showinfo(message="Division entre 0, no valido", title="Error de Calculo")
            else:
                resultado=aux%float(txtDisplay.get())
                txtOperators.insert(0,f'{aux} % {float(txtDisplay.get())} = {resultado}')
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,str(resultado))

def conversion(x):
    clear()

    global signo,aux
    signo=x
    aux=txtDisplay.get()
    txtDisplay.delete(0,END) #############

    regex = re.compile(r'^[0-9A-Fa-f]+$') #Acepta numeros del 0 al 9 asi como de la A a la F, y minusculas de esas letras
    if regex.fullmatch(aux):
        if signo=="DecBin":
            try:
                resultado = bin(int(aux))
                resultado = resultado.removeprefix('0b')
                BinOut.insert(0,str(resultado))
            except:
                print('Tipo de Valor Incorrecto')

        elif signo=="DecOct":
            try:
                resultado = oct(int(aux))
                resultado = resultado.removeprefix('0o')
                OctOut.insert(0,str(resultado))
            except:
                print('Tipo de Valor Incorrecto')

        elif signo=="DecHex":
            try:
                resultado = hex(int(aux))
                resultado = resultado.removeprefix('0x')
                HexOut.insert(0,str(resultado))
            except:
                print('Tipo de Valor Incorrecto')

        elif signo=="BinDec":
            try:
                resultado = int(aux)
                # print(aux)
                # print(int(str(int(aux)),2))
                resultado = int(str(resultado),2)
                DecOut.insert(0,str(resultado))
            except:
                print('Tipo de Valor Incorrecto')

        elif signo=="OctDec":
            try:
                resultado = int(aux)
                resultado = int(str(resultado),8)
                DecOut.insert(0,str(resultado))
            except:
                print('Tipo de Valor Incorrecto')

        elif signo=="HexDec":
            try:
                # resultado = aux
                resultado = int(str(aux),16)  
                DecOut.insert(0,str(resultado))
            except:
                print('Tipo de Valor Incorrecto')
        
        txtDisplay.insert(0,str(resultado)) ##############
    else:
        messagebox.showinfo(message="Decimales no aceptados o caracteres no aceptados", title="Error de Conversión")

def clear():
    DecOut.delete(0,END)
    OctOut.delete(0,END)
    HexOut.delete(0,END)
    BinOut.delete(0,END)
    txtOperators.delete(0,END)

txtDisplay=tk.Entry(root)
txtDisplay.place(x=45,y=20)

tk.Label(root,text="Ope:").place(x=10,y=50)
txtOperators=tk.Entry(root)
txtOperators.place(x=45,y=50)

tk.Label(root,text="DEC:").place(x=10,y=80)
DecOut = tk.Entry(root)
DecOut.place(x=45,y=80)

tk.Label(root,text="OCT:").place(x=10,y=110)
OctOut = tk.Entry(root)
OctOut.place(x=45,y=110)

tk.Label(root,text="HEX:").place(x=10,y=140)
HexOut = tk.Entry(root)
HexOut.place(x=45,y=140)

tk.Label(root,text="BIN:").place(x=10,y=170)
BinOut = tk.Entry(root)
BinOut.place(x=45,y=170)

btnDecBin = tk.Button(root, text="DecBin", command=lambda: conversion("DecBin"))
btnDecBin.place(x=200,y=20)

btnDecOct = tk.Button(root, text="DecOct", command=lambda: conversion("DecOct"))
btnDecOct.place(x=200,y=60)

btnDecHex = tk.Button(root, text="DecHex", command=lambda: conversion("DecHex"))
btnDecHex.place(x=200,y=100)

btnBinDec = tk.Button(root, text="BinDec", command=lambda: conversion("BinDec"))
btnBinDec.place(x=200,y=140)

btnOctDec = tk.Button(root, text="OctDec", command=lambda: conversion("OctDec"))
btnOctDec.place(x=200,y=180)

btnHexDec = tk.Button(root, text="HexDec", command=lambda: conversion("HexDec"))
btnHexDec.place(x=200,y=220)

btnExp = tk.Button(root, text="^", command=lambda: operador("^"))
btnExp.place(x=280,y=20)

btnPor = tk.Button(root, text="%", command=lambda: operador("%"))
btnPor.place(x=280,y=60)

btnFac = tk.Button(root, text="n!", command=lambda: operador("n!"))
btnFac.place(x=278,y=100)

btnRaiz = tk.Button(root, text="sqrt", command=lambda: operador("sqrt"))
btnRaiz.place(x=270,y=140)

btnSuma = tk.Button(root, text="+", command=lambda: operador("+"))
btnSuma.place(x=280,y=180)

btnResta = tk.Button(root, text="-", command=lambda: operador("-"))
btnResta.place(x=280,y=220)

btnMul = tk.Button(root, text="x", command=lambda: operador("*"))
btnMul.place(x=280,y=260)

btnDiv = tk.Button(root, text="/", command=lambda: operador("/"))
btnDiv.place(x=280,y=300)

btnIgual=tk.Button(root,text="=", command=operacion)
btnIgual.place(x=280,y=340)

root.mainloop()