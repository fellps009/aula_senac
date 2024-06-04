# realizamos a importação da biblioteca sqlite
import sqlite3

#Abrimos a conexão e atribuimos ela a uma variavel
conexao = sqlite3.connect('exemplo.bd')
#Utilizamos as opçoes presente na conexão
cursor = conexao.cursor()

#realizamos a operação de inserir dados nos campos informados e colocamos placeholders
# em seguida nos informamos os dados 
cursor.execute('INSERT INTO usuarias (nome, idade) VALUES (?, ?)', ('Alice', 30))
cursor.execute('INSERT INTO usuarias (nome, idade) VALUES (?, ?)', ('Marcos', 25))
#comprometemos nossa altaração para o banco
conexao.commit()

#Fechamos a conexão do banco de dados 
conexao.close()