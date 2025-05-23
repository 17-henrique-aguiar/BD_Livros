import streamlit as st
import dados

st.title("Catálago de Livros")

titulo = st.text_input("Título do Livro")
autor = st.text_input("Autor")
ano = st.number_input("Ano de Publicação", min_value=1500, max_value=2025)
genero = st.selectbox("Gênero", ["Ficção", "Não Ficção", "Romance", "Suspense", "Terror", "Outros"])
nota = st.slider("Nota", 0.0, 10.0, 5.0)

if st.button("Adicionar Livro"):
    if titulo and autor:
        dados.inserir_livro(titulo, autor, ano, genero, nota)
        st.success("Livro adicionado com sucesso!")
    else:
        st.error("Preencha todos os campos obrigatórios.")

st.divider()

# Filtro por gênero
st.header("Lista de Livros")

generos = ["Todos"] + dados.listar_generos_unicos()
genero_filtro = st.selectbox("Filtrar por Gênero", generos)

if genero_filtro != "Todos":
    livros = dados.listar_por_generos(genero_filtro)
else:
    livros = dados.listar_livros()

st.table(livros)

# Remoção de livros
st.subheader("Remover Livro")
id_excluir = st.number_input("Informe o ID do livro a ser removido", min_value=1, step=1)
if st.button("Remover"):
    dados.deletar_livros(id_excluir)
    st.success("Livro removido com sucesso!")