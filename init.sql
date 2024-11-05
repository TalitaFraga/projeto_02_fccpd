USE livraria;

-- Tabela Categoria
CREATE TABLE IF NOT EXISTS Categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Tabela Autor
CREATE TABLE IF NOT EXISTS Autor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Tabela Livro
CREATE TABLE IF NOT EXISTS Livro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    preco FLOAT NOT NULL,
    estoque INT NOT NULL,
    id_categoria INT,
    id_autor INT,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id),
    FOREIGN KEY (id_autor) REFERENCES Autor(id)
);

-- Tabela Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(20)
);

-- Tabela Pedido
CREATE TABLE IF NOT EXISTS Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    data_pedido DATE,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
);

-- Tabela de ligação entre Pedido e Livro (Pedido_Livro)
CREATE TABLE IF NOT EXISTS Pedido_Livro (
    id_pedido INT,
    id_livro INT,
    quantidade INT NOT NULL,
    PRIMARY KEY (id_pedido, id_livro),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_livro) REFERENCES Livro(id)
);

-- Inserindo dados iniciais nas tabelas
INSERT INTO Categoria (nome) VALUES ('Ficção'), ('Ciência'), ('Romance'), ('Fantasia');
INSERT INTO Autor (nome) VALUES ('J.R.R. Tolkien'), ('George Orwell'), ('Jane Austen'), ('Isaac Asimov');

INSERT INTO Livro (titulo, preco, estoque, id_categoria, id_autor) VALUES 
('O Senhor dos Anéis', 39.90, 10, 4, 1),
('1984', 25.90, 15, 1, 2),
('Orgulho e Preconceito', 27.90, 10, 3, 3),
('Fundação', 32.50, 8, 2, 4);

INSERT INTO Cliente (nome, email, telefone) VALUES 
('Ana Silva', 'ana.silva@email.com', '99999-0001'),
('Carlos Souza', 'carlos.souza@email.com', '99999-0002');

INSERT INTO Pedido (id_cliente, data_pedido) VALUES 
(1, '2024-11-01'),
(2, '2024-11-02');

INSERT INTO Pedido_Livro (id_pedido, id_livro, quantidade) VALUES 
(1, 1, 2),
(2, 2, 1);
