import tkinter


def parabola(x):
    y = x * x / 200
    return y

def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())

def plot(canvas_par, x, y):
    canvas_par.create_line(x, y, x + 1, y + 1, fill='red')


mainWindow = tkinter.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480-8-200')

canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background='gray')
canvas2.grid(row=0, column=1)

draw_axes(canvas2)
draw_axes(canvas)

for x in range(-100, 100):
    y = parabola(x)
    print(y)
    plot(canvas, x, -y)

mainWindow.mainloop()
