import mysql.connector
from client import inserir_cliente, listar_clientes, remover_cliente, atualizar_cliente

def menu():
    while True:
        print("\nMenu de Operações CRUD")
        print("1. Inserir Cliente")
        print("2. Listar Clientes")
        print("3. Remover Cliente")
        print("4. Atualizar Cliente")
        print("5. Sair")
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
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
