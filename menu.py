import mysql.connector
from client import inserir_cliente, listar_clientes, remover_cliente, atualizar_cliente, conectar
from livro import listar_livros, procurar_livros_por_categoria, pesquisar_livro_por_nome, excluir_livro, inserir_livro, atualizar_livro,cadastrar_categoria,cadastrar_editora,listar_livros_por_id
from pedidos import finalizar_pedido, adicionar_ao_carrinho, listar_pedidos, listar_todos_pedidos

usuario_logado = None

def menu_principal():
    global usuario_logado
    while True:
        print("\nBem-vindo à Livraria Online")
        print("1. Acessar como Cliente")
        print("2. Acessar como Administrador")
        print("3. Cadastrar-se")
        print("4. Ver Livros Disponíveis")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            usuario_logado = login_usuario()
            if usuario_logado:
                print(f"Bem-vindo(a), {usuario_logado['nome']}!")
                menu_cliente()
        elif opcao == '2':
            senha_admin = input("Digite a senha de administrador: ")
            if senha_admin == "senha_admin":
                print("Acesso concedido como Administrador.")
                menu_administrador()
            else:
                print("Senha incorreta.")
        elif opcao == '3':
            usuario_logado = inserir_cliente()
            print("Cadastro realizado com sucesso!")
            # menu_cliente()
        elif opcao == '4':
            listar_livros()
        elif opcao == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_cliente():
    while True:
        print("\nMenu do Cliente")
        print("1. Listar Livros")
        print("2. Procurar Livros por Categoria")
        print("3. Pesquisar Livro por Nome")
        print("4. Adicionar Livro ao Carrinho")
        print("5. Finalizar Compra")
        print("6. Ver Pedidos")
        print("7. Atualizar Dados")
        print("8. Excluir Conta")
        print("9. Sair para o Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_livros()
        elif opcao == '2':
            procurar_livros_por_categoria()
        elif opcao == '3':
            pesquisar_livro_por_nome()
        elif opcao == '4':
            adicionar_ao_carrinho(usuario_logado['id_cliente'])
        elif opcao == '5':
            finalizar_pedido(usuario_logado['id_cliente'])
        elif opcao == '6':
            listar_pedidos(usuario_logado['id_cliente'])
        elif opcao == '7':
            atualizar_cliente(usuario_logado['id_cliente'])
        elif opcao == '8':
            remover_cliente(usuario_logado['id_cliente'])
            break
        elif opcao == '9':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_administrador():
    while True:
        print("\nMenu do Administrador")
        print("1. Listar Clientes")
        print("2. Listar Todos os Pedidos")
        print("3. Listar Livros")
        print("4. Procurar Livros por Categoria")
        print("5. Pesquisar Livro por Nome")
        print("6. Cadastrar novo livro")
        print("7. Atualizar cadastro de livro")
        print("8. Excluir livro")
        print("9. Cadastrar nova categoria")
        print("10. Cadastrar nova editora")
        print("11. Sair para o Menu Principal")

        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_clientes()
        elif opcao == '2':
            listar_todos_pedidos()
        elif opcao == '3':
            listar_livros()
        elif opcao == '4':
            procurar_livros_por_categoria()
        elif opcao == '5':
            pesquisar_livro_por_nome()
        elif opcao == '6':
            inserir_livro()
        elif opcao == '7':
            listar_livros_por_id()
            atualizar_livro()
        elif opcao == '8':
            listar_livros_por_id()
            excluir_livro()
        elif opcao == '9':
            cadastrar_categoria()
        elif opcao == '10':
            cadastrar_editora()
        elif opcao == '11':
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def login_usuario():
    """Função para autenticação do usuário"""
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM Cliente WHERE cpf = %s AND senha = %s", (cpf, senha))
        usuario = cursor.fetchone()
        if usuario:
            return usuario 
        else:
            print("CPF ou senha incorretos.")
            return None
    except mysql.connector.Error as err:
        print(f"Erro ao fazer login: {err}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    menu_principal()