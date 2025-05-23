import sqlite3

conexao = sqlite3.connect('livros.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        genero TEXT NOT NULL,       
        nota REAL
    );
""")

conexao.close()
print("Tabela de livros de criada com sucesso!")