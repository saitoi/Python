import tkinter


mainwindow = tkinter.Tk()

mainwindow.title("Hello World")
# Centralize the window
mainwindow.geometry('640x480+500+400')

label = tkinter.Label(mainwindow, text="Hello World")
label.pack(side='bottom')

leftFrame = tkinter.Frame(mainwindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainwindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainwindow.mainloop()
