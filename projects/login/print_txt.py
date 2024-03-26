import sqlite3

with sqlite3.connect('random_users.db') as conn:
    with open('new.txt', 'w') as new_file:
        new_file.write("ID\tUsername\tPassword\n")
        for _id, username, password in conn.execute('SELECT * FROM users'):
            print(f"{_id}\t{username}\t{password}", file=new_file)
