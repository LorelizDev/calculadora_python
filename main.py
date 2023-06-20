from tkinter import *
from math import *

root = Tk()
root.title("CALCULADORA by LorelizDev")
root.geometry("418x590")
root.iconbitmap("./favicon/calculadora.ico")
root.resizable(0,0)
root.config(background="#9333FF")

screen_text = StringVar() # Variable de cadena de string
screen_text.set("0")
operation = ""

# VISUALIZAR LAS PULSACIONES DEL TECLADO EN LA PANTALLA
def btn_click(num):
    global operation # Variable que viene desde afuera de la función
    
    if num == "+" or num == "-" or num == "*" or num == "/" or num == "**":
        screen_text.set(screen_text.get() + num) # .get obtiene lo que hay en pantalla
        operation = screen_text.get()
    else:    
        operation = operation + str(num)
        screen_text.set(operation)


    """if operation != "" or screen_text.get() == "0" or screen_text.get() == "ERROR":
        screen_text.set(num)
        operation = ""
    else:
        screen_text.set(screen_text.get() + num) # .get obtiene lo que hay en pantalla"""

# CÁLCULO Y MUESTRA DE RESULTADOS
def calculation():
    global operation

    try:
        operation=str(eval(screen_text.get()))
        screen_text.set(operation)
    except:
        screen_text.set("ERROR")
    operation = ""
    
# LIMPIEZA DE PANTALLA
def clear():
    global operation

    operation = ""
    screen_text.set("0")

#-------------------- PANTALLA ----------------

screen = Entry(root, font=("arial", 28, "bold"), textvariable=screen_text, width=16, bd=20, insertwidth=0, bg="powder blue", justify="right").grid(row=1, column=1, columnspan=4, padx=20, pady=35) # columnspan indica la cantidad de columnas que ocupa el elemento

#--------------------BOTONES-------------------
# Diseño de los botones
button_width = 8
button_height = 3
button_padx_left = (20, 0)
button_padx_right = (0, 15)
button_pady = 5
button_color = "#BFE1FF"
button_font = ("arial", 12, "bold")

# Fila 1
button_c = Button(root, text="C", bg=button_color, font=button_font, width=button_width, height=button_height, command=clear).grid(row=2, column=1, padx=button_padx_left, pady=button_pady)
button_exp = Button(root, text="EXP", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("**")).grid(row=2, column=2, pady=button_pady)
button_sqrt = Button(root, text="√x", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("sqrt(")).grid(row=2, column=3, pady=button_pady)
button_percent = Button(root, text="%", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("%")).grid(row=2, column=4,padx=button_padx_right, pady=button_pady)

# Fila 2
button_7 = Button(root, text="7", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("7")).grid(row=3, column=1, padx=button_padx_left, pady=button_pady)
button_8 = Button(root, text="8", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("8")).grid(row=3, column=2, pady=button_pady)
button_9 = Button(root, text="9", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("9")).grid(row=3, column=3, pady=button_pady)
button_div = Button(root, text="÷", bg=button_color, font=(button_font), width=button_width, height=button_height, command=lambda:btn_click("/")).grid(row=3, column=4,padx=button_padx_right, pady=button_pady)

# Fila 3
button_4 = Button(root, text="4", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("4")).grid(row=4, column=1, padx=button_padx_left, pady=button_pady)
button_5 = Button(root, text="5", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("5")).grid(row=4, column=2, pady=button_pady)
button_6 = Button(root, text="6", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("6")).grid(row=4, column=3, pady=button_pady)
button_mult = Button(root, text="x", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("*")).grid(row=4, column=4, padx=button_padx_right, pady=button_pady)

# Fila 4
button_1 = Button(root, text="1", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("1")).grid(row=5, column=1,padx=button_padx_left, pady=button_pady)
button_2 = Button(root, text="2", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("2")).grid(row=5, column=2, pady=button_pady)
button_3 = Button(root, text="3", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("3")).grid(row=5, column=3, pady=button_pady)
button_resta = Button(root, text="-", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("-")).grid(row=5, column=4, padx=button_padx_right, pady=button_pady)

# Fila 5
button_0 = Button(root, text="0", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("0")).grid(row=6, column=1, padx=button_padx_left, pady=button_pady)
button_punto = Button(root, text=".", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click(".")).grid(row=6, column=2, pady=button_pady)
button_result = Button(root, text="=", bg=button_color, font=button_font, width=button_width, height=button_height, command=calculation).grid(row=6, column=3, pady=button_pady)
button_suma = Button(root, text="+", bg=button_color, font=button_font, width=button_width, height=button_height, command=lambda:btn_click("+")).grid(row=6, column=4,padx=button_padx_right, pady=button_pady)

root.mainloop()