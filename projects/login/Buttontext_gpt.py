import sqlite3
import tkinter as tk
from tkinter import messagebox


def focus_in_out(entry: tk.Entry, placeholder, color_in, color_out):
    def inner(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=color_in)
        elif entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg=color_out)
    return inner


class Buttontext(tk.Button):
    def __init__(self, window, text, connection, placeholders: list, **kwargs):
        super().__init__(window, text=text, command=self.get_input, **kwargs)

        self.cursor = connection.cursor()
        self.entry_list = []

        for placeholder in placeholders:
            self.entry_list.append((placeholder, self.entry_setup(window, placeholder)))

    @staticmethod
    def entry_setup(window, text) -> tk.Entry:
        entry = tk.Entry(window, fg='grey')
        entry.insert(0, text)
        entry.bind("<FocusIn>", focus_in_out(entry, text, 'black', 'grey'))
        entry.bind("<FocusOut>", focus_in_out(entry, text, 'black', 'grey'))
        return entry

    @staticmethod
    def message_popup(title: str, message: str):
        messagebox.showinfo(title, message)

    def grid(self, row, column, sticky, rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        for i, (_, entry) in enumerate(self.entry_list):
            entry.grid(row=row - i - 1, column=column, sticky='sew', padx=30, pady=0)

    def get_input(self):
        input_list = [entry.get() for _, entry in self.entry_list]

        # Clean entry boxes with button press
        for placeholder, entry in self.entry_list:
            entry.delete(0, tk.END)
            entry.config(fg='black')

        self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (input_list[1], input_list[0]))
        user = self.cursor.fetchone()
        if user:
            # self.message_popup('Login', 'Login Successful')
            mainwindow.after(1000, mainwindow.destroy)
        else:
            self.message_popup('Login Failed', 'Username or password incorrect')


if __name__ == '__main__':
    conn = sqlite3.connect('random_users.db')

    # Setup
    mainwindow = tk.Tk()
    mainwindow.title("Login Tkinter Prototype")
    mainwindow.geometry('640x480-400-200')

    # Rows and Column
    mainwindow.rowconfigure([0, 1, 2, 3], weight=1)
    mainwindow.columnconfigure(0, weight=1)

    tk.Label(mainwindow, text="LOGIN IN SAITO'S SECURE WEBSITE !!!").grid(row=0, column=0, sticky='nsew')
    placeholder_list = ['Password', 'Username',]

    # Buttontext widget
    enter_bttn = Buttontext(mainwindow, connection=conn, text='Enter', placeholders=placeholder_list)
    enter_bttn.grid(row=3, column=0, padx=50, pady=30, sticky='ns')
    enter_bttn.config(width=8)

    mainwindow.maxsize(400, 250)
    mainwindow.mainloop()
