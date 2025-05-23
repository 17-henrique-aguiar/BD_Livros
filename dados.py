import sqlite3

def conectar_db():
    return sqlite3.connect('livros.db')

def inserir_livro(titulo, autor, ano, genero, nota):
    con = conectar_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO livros (titulo, autor, ano, genero, nota)
        VALUES (?, ?, ?, ?, ?)
    """, (titulo, autor, ano, genero, nota))
    con.commit()
    con.close()

def listar_livros():
    con = conectar_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM livros")
    dados = cur.fetchall()
    con.close()
    return dados

def deletar_livros(id_livros):
    con = conectar_db()
    cur = con.cursor()
    cur.execute("DELETE FROM livros WHERE id_livros = ?", (id_livros))
    con.commit()
    con.close()

def listar_generos_unicos():
    con = conectar_db()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT genero FROM livros")
    generos = [g[0] for g in cur.fetchall()]
    con.close()
    return generos

def listar_por_generos(genero):
    con = conectar_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM livros WHERE genero = ?", (genero,))
    dados = cur.fetchall()
    con.close()
    return dados

