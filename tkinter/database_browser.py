import tkinter
import sqlite3

def on_artist_select(event=None):
    # Obtém o artista selecionado na lista de artistas
    selected_artist_index = list_listboxes[0].curselection()
    if selected_artist_index:
        selected_artist = list_listboxes[0].get(selected_artist_index[0])

        # Limpa o destaque de todos os itens da lista de álbuns
        list_listboxes[1].selection_clear(0, tkinter.END)

        # Destaca os álbuns correspondentes ao artista selecionado
        cursor.execute("SELECT albums.name FROM albums "
                       "JOIN artists ON albums.artist = artists._id "
                       "WHERE artists.name = ?", (selected_artist,))
        albums = cursor.fetchall()

        # Realiza o highlighting dos álbuns correspondentes ao artista
        for i in range(list_listboxes[1].size()):
            album_name = list_listboxes[1].get(i)
            if (album_name,) in albums:
                list_listboxes[1].selection_set(i)

def on_album_select(event=None):
    selected_album_index = list_listboxes[1].curselection()
    if selected_album_index:
        selected_album = list_listboxes[1].get(selected_album_index[0])
        list_listboxes[2].selection_clear(0, tkinter.END)
        cursor.execute("SELECT songs.title FROM songs "
                       "JOIN albums ON songs.album = albums._id "
                       "WHERE albums.name = ?", (selected_album,))
        songs = cursor.fetchall()

        for i in range(list_listboxes[2].size()):
            song_name = list_listboxes[2].get(i)
            if (song_name,) in songs:
                list_listboxes[2].selection_set(i)


conn = sqlite3.connect('music.db')
cursor = conn.cursor()
sqlite_queries = [
    "SELECT name FROM artists ORDER BY name COLLATE NOCASE",
    "SELECT name FROM albums ORDER BY name COLLATE NOCASE",
    "SELECT title FROM songs ORDER BY title COLLATE NOCASE"
]

mainwindow = tkinter.Tk()
mainwindow.title('Music Database Browser')
mainwindow.geometry('640x480+500+200')

mainFrame = tkinter.Frame(mainwindow)
mainFrame.grid(row=1, column=0, columnspan=6, sticky='nsew')
mainFrame.rowconfigure(0, weight=1)
mainFrame.rowconfigure(1, weight=10)
mainFrame['padx'] = 8
mainFrame['pady'] = 10
for i in range(6):
    mainFrame.columnconfigure(i, weight=7 if i == 2*i else 1)

columns_list = ['Artists Database List',
                'Albums Database List',
                'Songs Database List']
list_labels = []
list_listboxes = []
list_scrollbars = []
for i in range(3):
    list_labels.append(tkinter.Label(mainFrame, text=columns_list[i]))
    list_labels[i].grid(row=0, column=2 * i, sticky='nsew')

    list_listboxes.append(tkinter.Listbox(mainFrame, width=30, height=40))
    list_listboxes[i].grid(row=1, column=2 * i, sticky='nsew')

    list_scrollbars.append(tkinter.Scrollbar(mainFrame))
    list_scrollbars[i].grid(row=1, column=(2 * i) + 1, sticky='nsw')
    list_listboxes[i]['yscrollcommand'] = list_scrollbars[i].set

    cursor.execute(sqlite_queries[i])
    for zone in cursor.fetchall():
        list_listboxes[i].insert(tkinter.END, zone[0])

# Configurando o evento de seleção para a lista de artistas e álbuns
list_listboxes[0].bind('<<ListboxSelect>>', on_artist_select)
list_listboxes[1].bind('<<ListboxSelect>>', on_album_select)


mainwindow.update()
mainwindow.minsize(mainFrame.winfo_width() + 10, mainFrame.winfo_height() + 10)
mainwindow.maxsize(mainFrame.winfo_width() + 10, mainFrame.winfo_height() + 10)

mainwindow.mainloop()
