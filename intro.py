# realizamos a importação da biblioteca sqlite
import sqlite3
#Abrimos a conexão e atribuimos ela a uma variavel
conexao = sqlite3.connect('exemplo.db')
#Utilizamos as opçoes presente na conexão
cursor = conexao.cursor()
#Exacutamos uma tarefa: criamos uma tabela caso ela não exista, especificamos os campos
# que precisam ser preenchimos com nome campo, tipo do campo precise,
# chave primária.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios
        id INTEGER,
        nome TEXT,
        idade INTEGER
    ''')
#fechamos a conexão com o banco
conexao.close()
