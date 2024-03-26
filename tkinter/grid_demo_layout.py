import os
import tkinter
import tkinter as tk

mainwindow = tk.Tk()
mainwindow.title("Grid Demo")
mainwindow.geometry('640x480-400-200')
mainwindow['padx'] = 8

# Label
label = tk.Label(mainwindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# Column config
mainwindow.columnconfigure(0, weight=3)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=5)
mainwindow.columnconfigure(3, weight=5)
mainwindow.columnconfigure(4, weight=5)

# Row config
mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=10)
mainwindow.rowconfigure(2, weight=1)
mainwindow.rowconfigure(3, weight=3)
mainwindow.rowconfigure(4, weight=3)

# List
fileList = tk.Listbox(mainwindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)

# Scrollbar
listScroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command=fileList.yview())
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# Frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainwindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

# Radio Buttons
rbValue = tkinter.IntVar()
rbValue.set(3)
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Result Label
resultLabel = tkinter.Label(mainwindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainwindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

# Time Spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=list(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainwindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Date Labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Buttons 'Ok' and 'Cancel'
okButton = tkinter.Button(mainwindow, text="Ok")
cancelButton = tkinter.Button(mainwindow, text="Cancel", command=mainwindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')


mainwindow.mainloop()

print(rbValue.get())
