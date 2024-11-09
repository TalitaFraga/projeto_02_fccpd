import mysql.connector

db_config = {
    'host': 'db', 
    'user': 'app_user',
    'password': 'app_senha',
    'database': 'livraria'
}
def conectar():
    return mysql.connector.connect(**db_config)

def listar_pedidos(cliente_id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT Pedido.id_pedido, Pedido.data_pedido, Pedido.total, Pedido.status,
                   Livro.titulo AS livro, ItemPedido.quantidade, ItemPedido.preco_unitario
            FROM Pedido
            JOIN ItemPedido ON Pedido.id_pedido = ItemPedido.id_pedido
            JOIN Livro ON ItemPedido.id_livro = Livro.id_livro
            WHERE Pedido.id_cliente = %s
            ORDER BY Pedido.data_pedido DESC
        """, (cliente_id,))
        
        pedidos = cursor.fetchall()
        
        if pedidos:
            print("\nLista de Pedidos:")
            for pedido in pedidos:
                print(f"Pedido ID: {pedido['id_pedido']}, Data: {pedido['data_pedido']}, Total: {pedido['total']}, Status: {pedido['status']}")
                print(f"   Livro: {pedido['livro']}, Quantidade: {pedido['quantidade']}, Preço Unitário: {pedido['preco_unitario']}")
        else:
            print("Nenhum pedido encontrado para este cliente.")
    except mysql.connector.Error as err:
        print(f"Erro ao listar pedidos: {err}")
    finally:
        cursor.close()
        conn.close()


def adicionar_ao_carrinho(cliente_id):
    termo = input("Digite o nome ou parte do nome do livro: ")
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT id_livro, titulo, preco, estoque
            FROM Livro
            WHERE titulo LIKE %s
        """, (f"%{termo}%",))
        
        livros = cursor.fetchall()
        
        if livros:
            print("\nLivros encontrados:")
            for livro in livros:
                print(f"ID: {livro['id_livro']}, Título: {livro['titulo']}, Preço: {livro['preco']}")
            
            id_livro = input("\nDigite o ID do livro para adicionar ao carrinho: ")
            quantidade = int(input("Digite a quantidade: "))
            livro_escolhido = next((livro for livro in livros if livro['id_livro'] == int(id_livro)), None)

            if livro_escolhido:
                if quantidade > livro_escolhido['estoque']:
                    print("Quantidade solicitada excede o estoque disponível.")
                    return
                
                preco_unitario = livro_escolhido['preco']
                
                cursor.execute("SELECT id_pedido FROM Pedido WHERE id_cliente = %s AND status = 'aberto'", (cliente_id,))
                pedido = cursor.fetchone()
                
                if not pedido:
                    cursor.execute("INSERT INTO Pedido (id_cliente, data_pedido, total, status) VALUES (%s, NOW(), 0, 'aberto')", (cliente_id,))
                    conn.commit()
                    pedido_id = cursor.lastrowid
                else:
                    pedido_id = pedido['id_pedido']
                
                cursor.execute("""
                    INSERT INTO ItemPedido (id_pedido, id_livro, quantidade, preco_unitario)
                    VALUES (%s, %s, %s, %s)
                """, (pedido_id, id_livro, quantidade, preco_unitario))
                conn.commit()
                
                print("Item adicionado ao carrinho com sucesso.")
            else:
                print("Livro não encontrado com o ID informado.")
        else:
            print("Nenhum livro encontrado com esse nome.")
    
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar ao carrinho: {err}")
    finally:
        cursor.close()
        conn.close()


def finalizar_pedido(cliente_id):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT id_pedido FROM Pedido WHERE id_cliente = %s AND status = 'aberto'
        """, (cliente_id,))
        pedido = cursor.fetchone()
        
        if not pedido:
            print("Não há nenhum pedido em aberto para finalizar.")
            return
        
        pedido_id = pedido['id_pedido']
        
        cursor.execute("""
            SELECT SUM(quantidade * preco_unitario) AS total
            FROM ItemPedido
            WHERE id_pedido = %s
        """, (pedido_id,))
        
        total = cursor.fetchone()['total']

        cursor.execute("""
            SELECT id_livro, quantidade
            FROM ItemPedido
            WHERE id_pedido = %s
        """, (pedido_id,))

        itens = cursor.fetchall()
        for item in itens:
            cursor.execute("""
                UPDATE Livro
                SET estoque = estoque - %s
                WHERE id_livro = %s AND estoque >= %s
            """, (item['quantidade'], item['id_livro'], item['quantidade']))

        cursor.execute("""
            UPDATE Pedido
            SET total = %s, status = 'finalizado'
            WHERE id_pedido = %s
        """, (total, pedido_id))
        conn.commit()
        
        print(f"Compra finalizada com sucesso! Total: R$ {total:.2f}")
    
    except mysql.connector.Error as err:
        print(f"Erro ao finalizar compra: {err}")
    finally:
        cursor.close()
        conn.close()

def listar_todos_pedidos():
    """Lista todos os pedidos feitos por todos os clientes, com detalhes de cada pedido."""
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT Pedido.id_pedido, Pedido.data_pedido, Pedido.total, Pedido.status, 
                   Cliente.nome AS cliente_nome
            FROM Pedido
            JOIN Cliente ON Pedido.id_cliente = Cliente.id_cliente
            ORDER BY Pedido.data_pedido DESC
        """)
        
        pedidos = cursor.fetchall()
        
        if not pedidos:
            print("Nenhum pedido foi encontrado.")
            return
        
        for pedido in pedidos:
            print(f"\nPedido ID: {pedido['id_pedido']} | Cliente: {pedido['cliente_nome']} | Data: {pedido['data_pedido']}")
            print(f"Total: R$ {pedido['total']:.2f} | Status: {pedido['status']}")
            print("Itens do Pedido:")
            
            cursor.execute("""
                SELECT Livro.titulo, ItemPedido.quantidade, ItemPedido.preco_unitario
                FROM ItemPedido
                JOIN Livro ON ItemPedido.id_livro = Livro.id_livro
                WHERE ItemPedido.id_pedido = %s
            """, (pedido['id_pedido'],))
            
            itens = cursor.fetchall()
            for item in itens:
                print(f"   - Título: {item['titulo']}, Quantidade: {item['quantidade']}, Preço Unitário: R$ {item['preco_unitario']:.2f}")
        
    except mysql.connector.Error as err:
        print(f"Erro ao listar pedidos: {err}")
    finally:
        cursor.close()
        conn.close()
