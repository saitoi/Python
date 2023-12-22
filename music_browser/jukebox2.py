import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('music.db')

mainwindow = tkinter.Tk()
mainwindow.title('Music DB Browser')
mainwindow.geometry('1024x768')

mainwindow.columnconfigure(0, weight=2)
mainwindow.columnconfigure(1, weight=2)
mainwindow.columnconfigure(2, weight=2)
mainwindow.columnconfigure(3, weight=1)

mainwindow.rowconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=5)
mainwindow.rowconfigure(2, weight=5)
mainwindow.rowconfigure(3, weight=1)

tkinter.Label
