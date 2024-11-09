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

def remover_cliente(id_cliente):
    """Permite que o cliente logado remova sua própria conta após verificar a senha."""
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    senha = input("Digite sua senha para confirmar a remoção da conta: ")
    
    cursor.execute("SELECT senha FROM Cliente WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    
    if cliente and cliente['senha'] == senha:
        decisao = input("Você tem certeza que deseja deletar sua conta? (1- Sim, 2- Não): ")
        if decisao == "1":
            cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id_cliente,))
            conn.commit()
            
            if cursor.rowcount > 0:
                print("Conta removida com sucesso!")
            else:
                print("Erro ao remover a conta.")
        else:
            print("Remoção cancelada.")
    else:
        print("Senha incorreta. Remoção não autorizada.")
    
    cursor.close()
    conn.close()


def atualizar_cliente(id_cliente):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

            
    cursor.execute("SELECT * FROM Cliente WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    
    print("\nInformações atuais do cliente:")
    print(f"Id Cliente: {cliente['id_cliente']}")
    print(f"Usuário: {cliente['usuario']}")
    print(f"Senha: {cliente['senha']}")
    print(f"Nome: {cliente['nome']}")
    print(f"email: {cliente['email']}")
    print(f"Telefone: {cliente['telefone']}")
    print(f"cpf: {cliente['cpf']}")
    print(f"Rua: {cliente['rua']}")
    print(f"Cidade: {cliente['cidade']}")
    print(f"Estado: {cliente['estado']}")
    print(f"Numero: {cliente['numero']}")
    print(f"cep: {cliente['cep']}")
    print(f"Bairro: {cliente['bairro']}")
    print(f"Complemento: {cliente['complemento']}")


    # Listar ID, Nome, e CPF dos clientes
    usuario = input("Digite o novo usuario: ") or cliente['usuario']
    senha = input("Digite a nova senha: ") or cliente['senha']
    nome = input("Digite o novo nome: ") or cliente['nome']
    email = input("Digite o novo email: ") or cliente['email']
    telefone = input("Digite o novo telefone: ") or cliente['telefone']
    cpf = input("Digite o novo CPF: ") or cliente['cpf']
    rua = input("Digite a nova rua: ") or cliente['rua']
    cidade = input("Digite a nova cidade: ") or cliente['cidade']
    estado = input("Digite o novo estado: ") or cliente['estado']
    numero_input = (input("Digite o novo número da residência: ")) 
    numero = int(numero_input) if numero_input else cliente['numero']
    cep = input("Digite o novo CEP: (somente numeros) ")or cliente['cep']
    bairro = input("Digite o novo Bairro: ") or cliente['bairro']
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