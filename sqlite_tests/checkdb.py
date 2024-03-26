import sqlite3

conn = sqlite3.connect("contacts.sqlite")
sql_statement = "INSERT INTO contacts(name) VALUES (?)"
new_name = input("Please enter a name: ")

cursor = conn.cursor()
cursor.execute(sql_statement, (new_name,))  # Passando o parâmetro como uma tupla

# Selecionando e exibindo os resultados da consulta
cursor.execute("SELECT * FROM contacts WHERE name = ?", (new_name,))
# rows = cursor.fetchall()
for row in cursor:
    print(row)

cursor.close()
conn.commit()
conn.close()
# for row in conn.execute("SELECT * FROM contacts"):
#     print(row)
# conn.close()
