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

    if signo=="n!":
        resultado = 1
        for i in range(2,int(aux)+1):
            resultado = resultado * i
        txtDisplay.insert(0,str(resultado))
    elif signo=="sqrt":
        resultado=m.sqrt(aux)
        txtDisplay.insert(0,str(resultado))
    elif signo=="DecBin":
        resultado = bin(int(aux))
        resultado = resultado.removeprefix('0b')
        # resultado=format(int(aux),'o')
        txtDisplay.insert(0,str(resultado))
    elif signo=="DecOct":
        resultado = oct(int(aux))
        resultado = resultado.removeprefix('0o')
        # resultado=format(int(aux),'o')
        txtDisplay.insert(0,str(resultado))
    elif signo=="DecHex":
        resultado = hex(int(aux))
        resultado = resultado.removeprefix('0x')
        # resultado=format(int(aux),'o')
        txtDisplay.insert(0,str(resultado))
    elif signo=="BinDec": ######################
        resultado = bin(int(aux))
        resultado = resultado.removeprefix('0b')
        # resultado = int(resultado,2)
        #resultado = int(str(resultado),2)
        print(int(str(resultado),2))
        # resultado=format(int(aux),'o')
        txtDisplay.insert(0,str(int(resultado,2)))
    elif signo=="OctDec":
        resultado = hex(int(aux))
        resultado = resultado.removeprefix('0x')
        # resultado=format(int(aux),'o')
        txtDisplay.insert(0,str(resultado))
    elif signo=="HexDec":
        resultado = hex(int(aux))
        resultado = resultado.removeprefix('0x')
        # resultado=format(int(aux),'o')
        txtDisplay.insert(0,str(resultado))    

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
    txtDisplay.delete(0,END)
    txtDisplay.insert(0,str(resultado))

txtDisplay=tk.Entry(root)
txtDisplay.place(x=10,y=20)
tk.Label(root,text="DEC:").place(x=10,y=40)
tk.Label(root,text="OCT:").place(x=10,y=60)

tk.Label(root,text="HEX:").place(x=10,y=80)
tk.Label(root,text="BIN:").place(x=10,y=100)

btnDecBin = tk.Button(root, text="DecBin", command=lambda: operador("DecBin"))
btnDecBin.place(x=200,y=20)

btnDecOct = tk.Button(root, text="DecOct", command=lambda: operador("DecOct"))
btnDecOct.place(x=200,y=60)

btnDecHex = tk.Button(root, text="DecHex", command=lambda: operador("DecHex"))
btnDecHex.place(x=200,y=100)

btnBinDec = tk.Button(root, text="BinDec", command=lambda: operador("BinDec"))
btnBinDec.place(x=200,y=140)

btnOctDec = tk.Button(root, text="OctDec", command=lambda: operador("OctDec"))
btnOctDec.place(x=200,y=180)

btnHexDec = tk.Button(root, text="HexDec", command=lambda: operador("HexDec"))
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