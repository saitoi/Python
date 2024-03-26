import sqlite3

db = sqlite3.connect("contacts.sqlite")
# for row in db.execute("SELECT * FROM contacts"):
#     print(row)
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
while cursor.fetchone() is not None:
    print(cursor.fetchall())
db.close()
