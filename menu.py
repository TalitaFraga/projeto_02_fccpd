import mysql.connector
from client import inserir_cliente, listar_clientes, remover_cliente, atualizar_cliente
from livro import listar_livros, procurar_livros_por_categoria



def menu():
    while True:
        print("\nMenu de Operações CRUD")
        print("1. Inserir Cliente")
        print("2. Listar Clientes")
        print("3. Remover Cliente")
        print("4. Atualizar Cliente")
        print("5. Listar Livros")
        print("6. Procurar Livros por Categoria")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            remover_cliente()
        elif opcao == '4':
            atualizar_cliente()
        elif opcao == '5':
            listar_livros()
        elif opcao == '6':
            procurar_livros_por_categoria()
        elif opcao == '7':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
