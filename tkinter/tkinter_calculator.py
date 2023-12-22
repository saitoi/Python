import tkinter

# Mainwindow
mainwindow = tkinter.Tk()
mainwindow.title("Calculator")
mainwindow.geometry('500x480-400-200')
mainwindow['padx'] = 8

# Display - Entry
result = tkinter.Entry(mainwindow)
result.grid(row=0, column=0, columnspan=4)


# Function to update the display
def update_display(value):
    current_value = result.get()
    result.delete(0, tkinter.END)
    result.insert(tkinter.END, current_value + str(value))


# Function to perform calculation
def calculate():
    expression = result.get()
    try:
        result.delete(0, tkinter.END)
        result.insert(tkinter.END, eval(expression))
    except Exception as e:
        result.delete(0, tkinter.END)
        result.insert(tkinter.END, "Error")


# Numeric buttons
numeric_buttons = []
button_index = 1
for i in range(10):
    numeric_buttons.append(tkinter.Button(mainwindow, text=f"{i}", command=lambda i=i: update_display(i)))
for i in range(4, 1, -1):
    for j in range(3):
        numeric_buttons[button_index].grid(row=i, column=j, sticky='nsew')
        button_index += 1
numeric_buttons[0].grid(row=5, column=0, sticky='nsew')

# Operation buttons
c_button = tkinter.Button(mainwindow, text="C", command=lambda: result.delete(0, tkinter.END))
ce_button = tkinter.Button(mainwindow, text="CE", command=lambda: result.delete(0, tkinter.END))
c_button.grid(row=1, column=0, sticky='nsew')
ce_button.grid(row=1, column=1, sticky='nsew')
plus_button = tkinter.Button(mainwindow, text="+", command=lambda: update_display("+"))
plus_button.grid(row=2, column=3)
minus_button = tkinter.Button(mainwindow, text="-", command=lambda: update_display("-"))
minus_button.grid(row=3, column=3)
multiply_button = tkinter.Button(mainwindow, text="*", command=lambda: update_display("*"))
multiply_button.grid(row=4, column=3)
division_button = tkinter.Button(mainwindow, text="/", command=lambda: update_display("/"))
division_button.grid(row=5, column=3)
equal_button = tkinter.Button(mainwindow, text="=", command=calculate)
equal_button.grid(row=5, column=1, sticky='nsew', columnspan=2)

mainwindow.mainloop()
