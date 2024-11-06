import mysql.connector

# Configurações da conexão com o banco de dados
db_config = {
    'host': 'db',  # Ou 'db' se estiver usando Docker Compose
    'user': 'app_user',
    'password': 'app_senha',
    'database': 'livraria'
}

def conectar():
    return mysql.connector.connect(**db_config)

def listar_livros():
    """Lista todos os livros com detalhes específicos."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Livro.titulo, Autor.nome, Livro.genero, Livro.preco, Livro.data_publicacao
        FROM Livro
        JOIN Autor ON Livro.id_autor = Autor.id_autor
    """)
    
    livros = cursor.fetchall()
    print("\nLista de Livros Disponíveis:")
    for livro in livros:
        print(f"Nome: {livro[0]}, Autor: {livro[1]}, Gênero: {livro[2]}, Preço: {livro[3]}, Data de Publicação: {livro[4]}")
    
    cursor.close()
    conn.close()

def procurar_livros_por_categoria():
    """Lista as categorias disponíveis e permite procurar livros por uma categoria específica, mostrando detalhes."""
    conn = conectar()
    cursor = conn.cursor()

    # Listar as categorias disponíveis
    cursor.execute("SELECT id_categoria, nome FROM Categoria")
    categorias = cursor.fetchall()
    
    print("\nCategorias Disponíveis:")
    for categoria in categorias:
        print(f"ID: {categoria[0]}, Nome: {categoria[1]}")
    
    # Solicitar o ID da categoria
    categoria_id = int(input("\nDigite o ID da categoria para ver os livros: "))

    # Procurar livros pela categoria escolhida
    cursor.execute("""
        SELECT Livro.titulo, Autor.nome, Livro.genero, Livro.preco, Livro.data_publicacao
        FROM Livro
        JOIN Autor ON Livro.id_autor = Autor.id_autor
        WHERE Livro.id_categoria = %s
    """, (categoria_id,))
    
    livros = cursor.fetchall()
    if livros:
        print(f"\nLivros na Categoria {categoria_id}:")
        for livro in livros:
            print(f"Nome: {livro[0]}, Autor: {livro[1]}, Gênero: {livro[2]}, Preço: {livro[3]}, Data de Publicação: {livro[4]}")
    else:
        print("Nenhum livro encontrado nessa categoria.")
    
    cursor.close()
    conn.close()
