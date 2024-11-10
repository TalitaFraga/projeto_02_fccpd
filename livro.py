import mysql.connector
import time
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
        SELECT Livro.titulo, Autor.nome, Livro.genero, Editora.nome, Livro.preco, Livro.data_publicacao,Livro.estoque
        FROM Livro
        JOIN Autor ON Livro.id_autor = Autor.id_autor
        JOIN Editora ON Livro.id_editora = Editora.id_editora
    """)
    livros = cursor.fetchall()
    print("\nLista de Livros Disponíveis:")
    if livros:
        print("\nLista de Livros Disponíveis:")
        for livro in livros:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Gênero: {livro[2]}, Editora: {livro[3]}, Preço: {livro[4]}, Data de Publicação: {livro[5]}, Estoque: {livro[6]}")
    else:
        print("Nenhum livro encontrado.")
    cursor.close()
    conn.close()

def procurar_livros_por_categoria():
    """Lista as categorias disponíveis e permite procurar livros por uma categoria específica, mostrando detalhes."""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id_categoria, nome FROM Categoria")
    categorias = cursor.fetchall()
    
    print("\nCategorias Disponíveis:")
    for categoria in categorias:
        print(f"ID: {categoria[0]}, Nome: {categoria[1]}")
    
    categoria_id = int(input("\nDigite o ID da categoria para ver os livros: "))

    cursor.execute("""
        SELECT Livro.titulo, Autor.nome, Livro.genero, Livro.preco, Livro.data_publicacao,Livro.estoque
        FROM Livro
        JOIN Autor ON Livro.id_autor = Autor.id_autor
        WHERE Livro.id_categoria = %s
    """, (categoria_id,))
    
    livros = cursor.fetchall()
    if livros:
        print(f"\nLivros na Categoria {categoria_id}:")
        for livro in livros:
            print(f"Nome: {livro[0]}, Autor: {livro[1]}, Gênero: {livro[2]}, Preço: {livro[3]}, Data de Publicação: {livro[4]},estoque: {livro[5]}")
    else:
        print("Nenhum livro encontrado nessa categoria.")
    
    cursor.close()
    conn.close()

def listar_livros_por_id():
    """Lista todos os livros disponíveis ordenados pelo ID, incluindo o estoque."""
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT Livro.id_livro, Livro.titulo, Autor.nome, Livro.genero, Editora.nome, 
                   Livro.preco, Livro.data_publicacao, Livro.estoque
            FROM Livro
            JOIN Autor ON Livro.id_autor = Autor.id_autor
            JOIN Editora ON Livro.id_editora = Editora.id_editora
            ORDER BY Livro.id_livro
        """)
        
        livros = cursor.fetchall()
        
        if livros:
            print("\nLista de Livros por ID:")
            for livro in livros:
                print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}, "
                      f"Editora: {livro[4]}, Preço: {livro[5]}, Data de Publicação: {livro[6]}, Estoque: {livro[7]}")
        else:
            print("Nenhum livro encontrado.")
    except mysql.connector.Error as err:
        print(f"Erro ao listar livros: {err}")
    finally:
        cursor.close()
        conn.close()
    

def pesquisar_livro_por_nome():
    termo = input("Digite o nome ou parte do nome do livro: ")
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Livro.titulo, Autor.nome, Livro.genero, Editora.nome, Livro.preco, Livro.data_publicacao,Livro.estoque
        FROM Livro
        JOIN Autor ON Livro.id_autor = Autor.id_autor
        JOIN Editora ON Livro.id_editora = Editora.id_editora
        WHERE Livro.titulo LIKE %s
    """, (f"%{termo}%",))
    
    livros = cursor.fetchall()
    if livros:
        print("\nLivros encontrados:")
        for livro in livros:
            print(f"Título: {livro[0]}, Autor: {livro[1]}, Gênero: {livro[2]}, Editora: {livro[3]}, Preço: {livro[4]}, Data de Publicação: {livro[5]}, Estoque: {livro[6]}")
    else:
        print("Nenhum livro encontrado com esse nome.")

    cursor.close()
    conn.close()


def inserir_livro():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    try:
        nome_autor = input("Digite o nome do autor: ")
        nacionalidade = input("Digite a nacionalidade do autor: ")
        data_nascimento = input("Digite a data de nascimento do autor (YYYY-MM-DD): ")
        
        cursor.execute("""
            INSERT INTO Autor (nome, nacionalidade, data_nascimento)
            VALUES (%s, %s, %s)
        """, (nome_autor, nacionalidade, data_nascimento))
        conn.commit()
        
        id_autor = cursor.lastrowid 
        
        print(f"Autor '{nome_autor}' inserido com sucesso com ID {id_autor}.")

        titulo = input("Digite o título do livro: ")
        genero = input("Digite o gênero do livro: ")
        preco = float(input("Digite o preço do livro: "))
        data_publicacao = input("Digite a data de publicação do livro (YYYY-MM-DD): ")
        estoque = int(input("Digite a quantidade de estoque: "))
        

        cursor.execute("SELECT id_editora, nome FROM Editora")
        editoras = cursor.fetchall()
        
        if not editoras:
            print("Nenhuma editora encontrada. Cadastre editoras antes de adicionar livros.")
            return
        
        print("\nEditoras Disponíveis:")
        for editora in editoras:
            print(f"ID: {editora['id_editora']}, Nome: {editora['nome']}")
        
        id_editora = int(input("Digite o ID da editora: "))
        

        cursor.execute("SELECT id_categoria, nome FROM Categoria")
        categorias = cursor.fetchall()
        
        if not categorias:
            print("Nenhuma categoria encontrada. Cadastre categorias antes de adicionar livros.")
            return
        
        print("\nCategorias Disponíveis:")
        for categoria in categorias:
            print(f"ID: {categoria['id_categoria']}, Nome: {categoria['nome']}")
        
        id_categoria = int(input("Digite o ID da categoria: "))


        cursor.execute("""
            INSERT INTO Livro (titulo, id_autor, genero, preco, data_publicacao, estoque, id_editora, id_categoria)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (titulo, id_autor, genero, preco, data_publicacao, estoque, id_editora, id_categoria))
        
        conn.commit()
        print("Livro inserido com sucesso!")
    
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores corretos para os campos de ID, preço e estoque.")
    
    except mysql.connector.Error as err:
        print(f"Erro ao inserir livro: {err}")
    
    finally:
        cursor.close()
        conn.close()
def cadastrar_categoria():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    try:
        nome_categoria= input("Digite o nome da nova categoria: ")
        cursor.execute("""
            INSERT INTO Categoria (nome)
            VALUES (%s)
        """, (nome_categoria,))
        conn.commit()
        print("Categoria ", nome_categoria,"inserida com sucesso!")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valor correto pro nome da categoria.")
    
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar categoria: {err}")
    
    finally:
        cursor.close()
        conn.close()
def cadastrar_editora():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    try:
        nome_editora= input("Digite o nome da nova editora: ")
        cursor.execute("""
            INSERT INTO Editora (nome)
            VALUES (%s)
        """, (nome_editora,))
        conn.commit()
        print("Editora ", nome_editora,"inserida com sucesso!")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valor correto pro nome da editora.")
    
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar editora: {err}")
    
    finally:
        cursor.close()
        conn.close()
def excluir_livro():
    id_livro = int(input("Digite o ID do livro que deseja excluir: "))
    
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT titulo FROM Livro WHERE id_livro = %s", (id_livro,))
        livro = cursor.fetchone()
        
        if livro:
            confirmacao = input(f"Quer excluir o livro '{livro[0]}'? (s/n): ").lower()
            if confirmacao == 's':
                cursor.execute("DELETE FROM Livro WHERE id_livro = %s", (id_livro,))
                conn.commit()
                
                if cursor.rowcount > 0:
                    print("Livro excluído com sucesso!")
                else:
                    print("Erro ao excluir o livro.")
            else:
                print("Exclusão cancelada.")
        else:
            print("Livro não encontrado.")
    
    except mysql.connector.Error as err:
        print(f"Erro ao excluir livro: {err}")
    
    finally:
        cursor.close()
        conn.close()


def atualizar_livro():
    try:
        id_livro = int(input("Digite o ID do livro que deseja atualizar: "))
        
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM Livro WHERE id_livro = %s", (id_livro,))
        livro = cursor.fetchone()
        
        if not livro:
            print("Livro não encontrado com o ID informado.")
            return
        
        print("\nInformações atuais do livro:")
        print(f"Título: {livro['titulo']}")
        print(f"Autor ID: {livro['id_autor']}")
        print(f"Gênero: {livro['genero']}")
        print(f"Preço: {livro['preco']}")
        print(f"Data de Publicação: {livro['data_publicacao']}")
        print(f"Estoque: {livro['estoque']}")
        print(f"Editora ID: {livro['id_editora']}")
        print(f"Categoria ID: {livro['id_categoria']}")

        titulo = input("Novo título (ou deixe vazio para manter): ") or livro['titulo']
        id_autor = input("Novo ID do autor (ou deixe vazio para manter): ") or livro['id_autor']
        genero = input("Novo gênero (ou deixe vazio para manter): ") or livro['genero']
        preco = input("Novo preço (ou deixe vazio para manter): ") or livro['preco']
        data_publicacao = input("Nova data de publicação (ou deixe vazio para manter): ") or livro['data_publicacao']
        estoque = input("Nova quantidade de estoque (ou deixe vazio para manter): ") or livro['estoque']
        id_editora = input("Novo ID da editora (ou deixe vazio para manter): ") or livro['id_editora']
        id_categoria = input("Novo ID da categoria (ou deixe vazio para manter): ") or livro['id_categoria']
        
        cursor.execute("""
            UPDATE Livro
            SET titulo = %s, id_autor = %s, genero = %s, preco = %s, data_publicacao = %s, 
                estoque = %s, id_editora = %s, id_categoria = %s
            WHERE id_livro = %s
        """, (titulo, int(id_autor), genero, float(preco), data_publicacao, int(estoque), int(id_editora), int(id_categoria), id_livro))
        
        conn.commit()
        
        if cursor.rowcount > 0:
            print("Livro atualizado com sucesso!")
        else:
            print("Nenhuma alteração foi feita.")
    
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números para campos de ID, preço e estoque.")
    
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar livro: {err}")
    
    finally:
        cursor.close()
        conn.close()

