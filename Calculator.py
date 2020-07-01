import tkinter as tk

cal = tk.Tk()
cal.title("Calculator")
cal.resizable(width=False, height=False)

def click(number):
    global oprator
    oprator = oprator + str(number)
    variable.set(oprator)

def clear():
    global oprator
    oprator = ""
    variable.set(oprator)

def delt():
    global oprator
    temp = variable.get()
    temp = temp[0:-1]
    oprator = temp
    variable.set(temp)

def sum():
    global oprator
    oprator = str(eval(oprator))
    variable.set(oprator)

# Display

oprator = ""
variable = tk.StringVar()
display = tk.Entry(cal, textvariable=variable, font=("Verdana", 15, ), bd=12,  insertwidth=4, width=14, justify="right")
display.grid(columnspan=4)

# Numbers Button

button1 = tk.Button(cal, text='1', command=lambda: click(1), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button1.grid(row=2, column=0, )

button2 = tk.Button(cal, text='2', command=lambda: click(2), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button2.grid(row=2, column=1, )

button3 = tk.Button(cal, text='3', command=lambda:click(3), bg="gainsboro",  bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button3.grid(row=2, column=2, )

button4 = tk.Button(cal, text='4', command=lambda: click(4), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button4.grid(row=3, column=0, )

button5 = tk.Button(cal, text='5', command=lambda: click(5), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button5.grid(row=3, column=1, )

button6 = tk.Button(cal, text='6', command=lambda:click(6), bg="gainsboro",  bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button6.grid(row=3, column=2, )

button7 = tk.Button(cal, text='7', command=lambda: click(7), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button7.grid(row=4, column=0, )

button8 = tk.Button(cal, text='8', command=lambda: click(8), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button8.grid(row=4, column=1, )

button9 = tk.Button(cal, text='9', command=lambda: click(9), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button9.grid(row=4, column=2, )

button0 = tk.Button(cal, text='0', command=lambda: click(0), bg="gainsboro", bd=4, padx=12, pady=5, font=("Helvetica", 14, "bold"))
button0.grid(row=5, column=0, )

button_float = tk.Button(cal, text='.', command=lambda: click('.'), bg="gainsboro", bd=4, padx=15, pady=5, font=("Helvetica", 14, "bold"))
button_float.grid(row=5, column=1)

# Oprator Button

button_plus = tk.Button(cal, text='+', command=lambda: click('+'), bg="gray70",  bd=4, padx=11, pady=5, font=("Helvetica", 14, "bold"))
button_plus.grid(row=2, column=3, )

button_minus = tk.Button(cal, text='-', command=lambda: click('-'),  bg="gray70",  bd=4, padx=11, pady=4, font=("Verdana", 14, "bold"))
button_minus.grid(row=3, column=3, )

button_multiply = tk.Button(cal, text='*', command=lambda: click('*'), bg="gray70", bd=4, padx=13, pady=5, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=4, column=3, )

button_division = tk.Button(cal, text='/', command=lambda: click('/'),  bg="gray70", bd=4, padx=14, pady=5, font=("Helvetica", 14, "bold"))
button_division.grid(row=5, column=3, )

button_percent = tk.Button(cal, text='%', command=lambda: click("%"), bg='gray70', bd=4, padx=12, pady=5, font=("Arial", 14))
button_percent.grid(row=5, column=2, )

# Delete Button , Clear All Button

buttondelt = tk.Button(cal, text='DEL', command=delt, bg="#ff0000", fg="#ffffff",  bd=4, padx=11, pady=1, font=("Helvetica", 10))
buttondelt.grid(row=1, column=0)

buttonclear = tk.Button(cal, text='AC', command=lambda: clear(), bg="#ff0000", fg="#ffffff",  bd=4, padx=11, pady=1, font=("Helvetica", 10))
buttonclear.grid(row=1, column=1)

# Result Button

buttonequal = tk.Button(cal, text="=", font=("Helvetica", 14), fg="#ffffff", bg='orange', bd=4, padx=99,  pady=5, command=sum)
buttonequal.grid(row=6, columnspan=5)

cal.mainloop()
