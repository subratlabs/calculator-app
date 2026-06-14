import tkinter as tk

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    if b == 0:
        return "Error (Div by 0)"
    return a / b

def avg(a, b):
    return (a + b) / 2

# gui logic

def button_click(char):     # FUNCTION runs whnever calculator button pressed
    current = entry.get()    
    entry.delete(0, tk.END)   # clear disppay
    entry.insert(0, current + str(char))

def clear():
    entry.delete(0, tk.END)      # remove all text fom display

def calculate():                   # RUNS  when = button is clicked
    expression = entry.get()   

    try:
        if "+" in expression:   # checks wheather expression contains +
            a, b = map(float, expression.split("+"))   # split the value like "5", "10" map float means store the values a = 5 , b = 10  
            result = add(a, b)

        elif "-" in expression:
            a, b = map(float, expression.split("-"))
            result = substract(a, b)       

        elif "*" in expression:
            a, b = map(float, expression.split("*"))
            result = multiply(a, b)    

        elif "/" in expression:
            a, b = map(float, expression.split("/"))
            result = devide(a, b)  

        elif "avg" in expression:
            a, b = map(float, expression.split("avg"))
            result = avg(a, b)     

        else:
            result = "Error"      # if any error them type this dont crash program

        entry.delete(0, tk.END)            # clear old expression
        entry.insert(0, str(result))        # inserting value then take result
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Syntax Error")

root = tk.Tk()     # create calculator window
root.title("Simple GUI Calculator")    # simple GUI calculator

entry = tk.Entry(root, width=20, font=("Arail", 16), bd=5, justify="right")  # create text box
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)             # place display

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),   # each tuple ['7', 1, 0] contains button 7, in row 1 amd column 0
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('avg', 4, 3)
]

for (text, row, col) in buttons:  # create button automatically
    btn = tk.Button(root, text=text, font=("Arail", 12), width=5, height=2,   # creates button
                    command=lambda t=text: button_click(t))   # when button is clicked
    btn.grid(row=row, column=col, padx=2, pady=2)    # places button as correct position

clear_btn = tk.Button(root, text="C", font=("Arial", 12), width=11, height=2, bg="orange", command=clear)   # creayes clear button
clear_btn.grid(row=5, column=0, columnspan=2, padx=2, pady=2)    #

equal_btn = tk.Button(root, text="=", font=("Arial", 12), width=11, height=2, bg="lightgreen", command=calculate)  # create equal button
equal_btn.grid(row=5, column=2, columnspan=2, padx=2, pady=2)

root.mainloop()  # this is the most important command it keeps the window alive and waits for button click and keyboard input, window closing
