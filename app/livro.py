from database import get_connection

class Livro:
    def inserir_livro(self, titulo, preco, estoque, id_categoria, id_autor):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Livro (titulo, preco, estoque, id_categoria, id_autor) VALUES (%s, %s, %s, %s, %s)", 
                       (titulo, preco, estoque, id_categoria, id_autor))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_livros(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT Livro.id, Livro.titulo, Livro.preco, Livro.estoque, Categoria.nome AS categoria, Autor.nome AS autor FROM Livro JOIN Categoria ON Livro.id_categoria = Categoria.id JOIN Autor ON Livro.id_autor = Autor.id")
        livros = cursor.fetchall()
        cursor.close()
        connection.close()
        return livros

