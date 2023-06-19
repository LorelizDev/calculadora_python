from tkinter import *
from math import *

root = Tk()
root.title("CALCULADLORE")
root.geometry("418x590")
root.iconbitmap("./favicon/calculadora.ico")
root.resizable(0,0)
root.config(background="#9333FF")

#-------------------- PANTALLA ----------------

screen = Entry(root, font=("arial", 28, "bold"), width=16, bd=20, insertwidth=4, bg="powder blue", justify="right").grid(row=1, column=1, columnspan=4, padx=20, pady=35)

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
button_c = Button(root, text="C", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=2, column=1, padx=button_padx_left, pady=button_pady)
button_exp = Button(root, text="EXP", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=2, column=2, pady=button_pady)
button_sqr = Button(root, text="√x", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=2, column=3, pady=button_pady)
button_percent = Button(root, text="%", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=2, column=4,padx=button_padx_right, pady=button_pady)

# Fila 2
button_7 = Button(root, text="7", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=3, column=1, padx=button_padx_left, pady=button_pady)
button_8 = Button(root, text="8", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=3, column=2, pady=button_pady)
button_9 = Button(root, text="9", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=3, column=3, pady=button_pady)
button_div = Button(root, text="÷", bg=button_color, font=(button_font), width=button_width, height=button_height).grid(row=3, column=4,padx=button_padx_right, pady=button_pady)

# Fila 3
button_4 = Button(root, text="4", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=4, column=1, padx=button_padx_left, pady=button_pady)
button_5 = Button(root, text="5", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=4, column=2, pady=button_pady)
button_6 = Button(root, text="6", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=4, column=3, pady=button_pady)
button_mult = Button(root, text="x", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=4, column=4, padx=button_padx_right, pady=button_pady)

# Fila 4
button_1 = Button(root, text="1", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=5, column=1,padx=button_padx_left, pady=button_pady)
button_2 = Button(root, text="2", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=5, column=2, pady=button_pady)
button_3 = Button(root, text="3", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=5, column=3, pady=button_pady)
button_resta = Button(root, text="-", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=5, column=4, padx=button_padx_right, pady=button_pady)

# Fila 5
button_0 = Button(root, text="0", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=6, column=1, padx=button_padx_left, pady=button_pady)
button_punto = Button(root, text=".", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=6, column=2, pady=button_pady)
button_igual = Button(root, text="=", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=6, column=3, pady=button_pady)
button_suma = Button(root, text="+", bg=button_color, font=button_font, width=button_width, height=button_height).grid(row=6, column=4,padx=button_padx_right, pady=button_pady)



root.mainloop()