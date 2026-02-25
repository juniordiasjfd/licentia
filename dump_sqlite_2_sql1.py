import sqlite3
import os


# Nome do seu arquivo de banco
con = sqlite3.connect('db.sqlite3')

with open(os.path.join(os.getcwd(), 'base_sqlite3.sql'), 'w', encoding='utf-8') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)

con.close()
print("Arquivo base_sqlite3.sql gerado com sucesso!")