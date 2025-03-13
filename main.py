import sqlite3

banco = sqlite3.connect('database.db')
cursor = banco.cursor() #para escrever em sql, inserir e manipular dados no banco

#cursor.execute("CREATE TABLE cliente(nome text, idade integer, sexo text)")
cursor.execute("INSERT INTO cliente VALUES ('vitor',26,'m'), ('paula',24,'f')")

banco.commit()

cursor.execute("SELECT * from cliente")
print(cursor.fetchall())

cursor.close()
banco.close()
