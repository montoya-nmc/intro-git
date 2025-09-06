from tkinter import *

operador = ""
numero1 = ""
entrada_actual = ""

def agregar7():
    agregar('7')

def agregar8():
    agregar('8')

def agregar9():
    agregar('9')

def agregar4():
    agregar('4')

def agregar5():
    agregar('5')

def agregar6():
    agregar('6')

def agregar1():
    agregar('1')

def agregar2():
    agregar('2')

def agregar3():
    agregar('3')

def agregar0():
    agregar('0')

def agregar_punto():
    agregar('.')

def agregar(digito):
    global entrada_actual
    if digito == '.' and '.' in entrada_actual:
        return
    entrada_actual += str(digito)
    entry.delete(0, END)
    entry.insert(0, entrada_actual)

def sumar():
    global operador, numero1, entrada_actual
    if entrada_actual != "":
        numero1 = float(entrada_actual)
        operador = "+"
        entrada_actual = ""
        entry.delete(0, END)

def restar():
    global operador, numero1, entrada_actual
    if entrada_actual != "":
        numero1 = float(entrada_actual)
        operador = "-"
        entrada_actual = ""
        entry.delete(0, END)

def multiplicar():
    global operador, numero1, entrada_actual
    if entrada_actual != "":
        numero1 = float(entrada_actual)
        operador = "*"
        entrada_actual = ""
        entry.delete(0, END)

def dividir():
    global operador, numero1, entrada_actual
    if entrada_actual != "":
        numero1 = float(entrada_actual)
        operador = "/"
        entrada_actual = ""
        entry.delete(0, END)

def resultado():
    global operador, numero1, entrada_actual
    if operador == "" or entrada_actual == "":
        label_resultado.config(text="Resultado: " + entrada_actual)
        return

    numero2 = float(entrada_actual)

    if operador == "+":
        res = numero1 + numero2
    elif operador == "-":
        res = numero1 - numero2
    elif operador == "*":
        res = numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            label_resultado.config(text="Error: División por 0")
            entrada_actual = ""
            entry.delete(0, END)
            operador = ""
            return
        else:
            res = numero1 / numero2

    label_resultado.config(text="Resultado: " + str(res))
    entrada_actual = str(res)
    entry.delete(0, END)
    entry.insert(0, entrada_actual)
    operador = ""

def limpiar():
    global operador, numero1, entrada_actual
    operador = ""
    numero1 = ""
    entrada_actual = ""
    entry.delete(0, END)
    label_resultado.config(text="Resultado: -")


ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("230x280")

entry = Entry(ventana, bg='lightgray')
entry.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="we")

label_resultado = Label(ventana, text="Resultado: -")
label_resultado.grid(row=1, column=0, columnspan=3, pady=5)


Button(ventana, text='7', bg='lightblue', command=agregar7, width=5).grid(row=2, column=0, padx=2, pady=2)
Button(ventana, text='8', bg='lightblue', command=agregar8, width=5).grid(row=2, column=1, padx=2, pady=2)
Button(ventana, text='9', bg='lightblue', command=agregar9, width=5).grid(row=2, column=2, padx=2, pady=2)

Button(ventana, text='4', bg='lightblue', command=agregar4, width=5).grid(row=3, column=0, padx=2, pady=2)
Button(ventana, text='5', bg='lightblue', command=agregar5, width=5).grid(row=3, column=1, padx=2, pady=2)
Button(ventana, text='6', bg='lightblue', command=agregar6, width=5).grid(row=3, column=2, padx=2, pady=2)

Button(ventana, text='1', bg='lightblue', command=agregar1, width=5).grid(row=4, column=0, padx=2, pady=2)
Button(ventana, text='2', bg='lightblue', command=agregar2, width=5).grid(row=4, column=1, padx=2, pady=2)
Button(ventana, text='3', bg='lightblue', command=agregar3, width=5).grid(row=4, column=2, padx=2, pady=2)

Button(ventana, text='0', bg='lightblue', command=agregar0, width=5).grid(row=5, column=1, padx=2, pady=2)


Button(ventana, text='.', bg='lightblue', command=agregar_punto, width=5).grid(row=8, column=2, padx=2, pady=2)
Button(ventana, text='+', bg='lightblue', command=sumar, width=5).grid(row=6, column=0, padx=2, pady=2)
Button(ventana, text='-', bg='lightblue', command=restar, width=5).grid(row=6, column=1, padx=2, pady=2)
Button(ventana, text='x', bg='lightblue', command=multiplicar, width=5).grid(row=6, column=2, padx=2, pady=2)

Button(ventana, text='/', bg='lightblue', command=dividir, width=5).grid(row=7, column=0, padx=2, pady=2)
Button(ventana, text='=', bg='lightblue', command=resultado, width=5).grid(row=7, column=1, padx=2, pady=2)
Button(ventana, text='Limpiar (C)', bg='lightblue', command=limpiar, width=10).grid(row=7, column=2, padx=2, pady=2)

ventana.mainloop()
