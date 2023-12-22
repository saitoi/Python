import tkinter

keys = [
    [('C', 1), ('CE', 1)],
    [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
    [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
    [('0', 1), ('=', 2), ('/', 1)]
]

mainWindow = tkinter.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8


def update_display(value):
    if value == 'C' or value == 'CE':
        result.delete(0, tkinter.END)
        return
    current_value = result.get()
    result.delete(0, tkinter.END)
    result.insert(tkinter.END, current_value + str(value))


def calculate():
    expression = result.get()
    try:
        result.delete(0, tkinter.END)
        result.insert(tkinter.END, eval(expression))
    except Exception:
        result.delete(0, tkinter.END)
        result.insert(tkinter.END, "Error")


# Result Entry
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# KeyPad Frame
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# KeyPad Buttons
row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        button_tmp = tkinter.Button(
            keyPad, text=key[0],
            command=lambda k=key[0]: update_display(k) if k != '=' else calculate())
        button_tmp.grid(
            row=row, column=col, columnspan=key[1],
            sticky=tkinter.E + tkinter.W)
        button_tmp.config(border=1, relief='raised')
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + 8, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 8, result.winfo_height() + keyPad.winfo_height())

mainWindow.mainloop()
