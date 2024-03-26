import sqlite3
import tkinter as tk

def focus_in_out(entry: tk.Entry, color: str, placeholder, content='') -> None:
    if entry.get() == content:
        if content:
            entry.delete(0, tk.END)
        else:
            entry.insert(0, placeholder)
        entry.config(fg=color)


def on_focus_in(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')


def on_focus_out(entry, placeholder):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')

class Buttontext(tk.Button):
    def __init__(self, window, text, connection, element_count, placeholders: list, command=self.get_input, **kwargs):
        super().__init__(text=text, command=command, **kwargs)
        self.cursor = connection.cursor()

        self.element_count = element_count
        self.entry_list = []

        for placeholder in placeholders:
            entry = tk.Entry(window, fg='grey')
            entry.insert(0, placeholder)
            entry.bind("<FocusIn>", lambda event, e=entry, p=placeholder: focus_in_out(e, p, color='black', content=placeholder))
            entry.bind("<FocusOut>", lambda event, e=entry, p=placeholder: focus_in_out(e, p, placeholder, color='grey'))
            self.entry_list.append(entry)

    def grid(self, row, column, sticky, rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)

        for i, entry in enumerate(self.entry_list):
            entry.grid(row=row - i - 1, column=column, sticky='new', padx=30, pady=0)
            entry.config(width=25)

    def get_input(self):
        input_list = []
        for entry in self.entry_list:
            entry.delete(0, tk.END)
            input_list.append(entry.get())
        for entry in self.entry_list:
            # input_list.append(entry.get())
            self.cursor.execute(sql_username, (entry.get(),))
            if self.cursor.fetchone():
                continue
            else:
            #     TODO Username not identified
                break
                pass
            # query = sql_username + sql_password
            # self.cursor.execute(query, (input_list[0], input_list[1]))

sql_username = 'SELECT * FROM users WHERE username=?'
sql_password = ' AND password=?'

if __name__ == '__main__':
    conn = sqlite3.connect('random_users.db')
    mainwindow = tk.Tk()
    mainwindow.title("Login Tkinter Prototype")
    mainwindow.geometry('640x480')

    # Rows and Column
    mainwindow.rowconfigure([0, 1, 2, 3], weight=1)
    mainwindow.columnconfigure(0, weight=1)

    #
    tk.Label(mainwindow, text="LOGIN IN SAITO'S SECURE WEBSITE !!!").grid(row=0, column=0, sticky='nsew')
    placeholder_list = ['password', 'username']

    enter_bttn = Buttontext(mainwindow, connection=conn, text='Enter', element_count=2, placeholders=placeholder_list)
    enter_bttn.grid(row=3, column=0, padx=50, pady=30, sticky='ns')
    enter_bttn.config(width=10)

    mainwindow.maxsize(500, 350)
    mainwindow.mainloop()
