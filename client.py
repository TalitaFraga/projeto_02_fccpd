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

def inserir_cliente():
    usuario = input("Digite o seu usuario: ")
    senha = input("Digite a senha: ")
    nome = input("Digite sue nome cliente: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    cpf = input("Digite seu CPF: ")
    rua = input("Digite sua rua: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite sua estado: ")
    numero = int(input("Digite o numero da sua residencia: "))
    cep = input("Digite seu CEP: (somente numeros) ")
    bairro = input("Digite seu Bairro: ")
    complemento = input("Digite seu complemento: ") or ""
    

    # Adicione os outros campos conforme necessário
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cliente (usuario, senha, cpf, nome, email, telefone, rua, cidade, estado, numero, cep, bairro, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (usuario, senha, cpf, nome, email, telefone, rua, cidade, estado, numero, cep, bairro, complemento))
    conn.commit()
    print("Cliente inserido com sucesso!")
    cursor.close()
    conn.close()

def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente")
    for cliente in cursor.fetchall():
        print(cliente)
    cursor.close()
    conn.close()

def remover_cliente():
    conn = conectar()
    cursor = conn.cursor()
    
    # Listar ID, Nome, e CPF dos clientes
    cursor.execute("SELECT id_cliente, nome, cpf FROM Cliente")
    clientes = cursor.fetchall()
    
    print("\nClientes disponíveis para remoção:")
    for cliente in clientes:
        print(f"ID: {cliente[0]}, Nome: {cliente[1]}, CPF: {cliente[2]}")
    
    # Solicitar o ID do cliente a ser removido
    id_cliente = int(input("\nDigite o ID do cliente a ser removido: "))
    decisao = input("Você tem certeza que deseja deletar o cliente? 1- Sim, 2- Nao ")
    if decisao == "1":
        # Executar remoção
        cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id_cliente,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print("Cliente removido com sucesso!")
        else:
            print("Cliente não encontrado.")
    else:
        print("Remoção cancelada.")
        
    cursor.close()
    conn.close()

def atualizar_cliente():
    conn = conectar()
    cursor = conn.cursor()
    
    # Listar ID, Nome, e CPF dos clientes
    cursor.execute("SELECT id_cliente, nome, cpf FROM Cliente")
    id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
    usuario = input("Digite o novo usuario: ")
    senha = input("Digite a nova senha: ")
    nome = input("Digite o novo nome: ")
    email = input("Digite o novo email: ")
    telefone = input("Digite o novo telefone: ")
    cpf = input("Digite o novo CPF: ")
    rua = input("Digite a nova rua: ")
    cidade = input("Digite a nova cidade: ")
    estado = input("Digite o novo estado: ")
    numero = int(input("Digite o novo número da residência: "))
    cep = input("Digite o novo CEP: (somente numeros) ")
    bairro = input("Digite o novo Bairro: ")
    complemento = input("Digite o novo complemento: ") or ""
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE Cliente SET usuario=%s, senha=%s, cpf=%s, nome=%s, email=%s, telefone=%s, rua=%s, 
        cidade=%s, estado=%s, numero=%s, cep=%s, bairro=%s, complemento=%s 
        WHERE id_cliente = %s
        """,
        (usuario, senha, cpf, nome, email, telefone, rua, cidade, estado, numero, cep, bairro, complemento, id_cliente)
    )
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Cliente atualizado com sucesso!")
    else:
        print("Cliente não encontrado.")
        
    cursor.close()
    conn.close()