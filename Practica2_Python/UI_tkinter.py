import tkinter as tk
from tkinter import END,messagebox
import math as m

root=tk.Tk()
root.title("Calculadora")
root.config(width=300,height=500)
aux=0
signo=""

def operador(x):
    global signo,aux
    signo=x
    aux=float(txtDisplay.get())
    txtDisplay.delete(0,END)

def operacion():
    resultado=0
    global signo,aux
    if signo=="+":
        resultado=aux+float(txtDisplay.get())
    elif signo=="-":
        resultado=aux-float(txtDisplay.get())
    elif signo=="*":
        resultado=aux*float(txtDisplay.get())
    elif signo=="/":
        resultado=aux/float(txtDisplay.get())
    elif signo=="^":
        resultado=aux**float(txtDisplay.get())
    elif signo=="%":
        resultado=aux%float(txtDisplay.get())
    elif signo=="n!":
        start = 1
        for i in range(1,txtDisplay.get()): ## TO DO
            start = start * i
        resultado = start
    elif signo=="sqrt":
        resultado=m.sqrt(aux)
    

    txtDisplay.delete(0,END)
    txtDisplay.insert(0,str(resultado))

txtDisplay=tk.Entry(root)
txtDisplay.place(x=10,y=20)
tk.Label(root,text="DEC:").place(x=10,y=40)
tk.Label(root,text="OCT:").place(x=10,y=60)

tk.Label(root,text="HEX:").place(x=10,y=80)
tk.Label(root,text="BIN:").place(x=10,y=100)

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