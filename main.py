import sqlite3

banco = sqlite3.connect('database.db')
cursor = banco.cursor() #para escrever em sql, inserir e manipular dados no banco

