USE livraria;

-- Tabela Autor
CREATE TABLE IF NOT EXISTS Autor (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nacionalidade VARCHAR(100),
    data_nascimento DATE
);

-- Tabela Categoria
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Tabela Editora
CREATE TABLE IF NOT EXISTS Editora (
    id_editora INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

-- Tabela Livro
CREATE TABLE IF NOT EXISTS Livro (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    id_autor INT,
    genero VARCHAR(50),
    preco FLOAT NOT NULL,
    data_publicacao DATE,
    estoque INT NOT NULL,
    id_editora INT,
    id_categoria INT,
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor),
    FOREIGN KEY (id_editora) REFERENCES Editora(id_editora),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

-- Tabela Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14),
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    telefone VARCHAR(20),
    cidade VARCHAR(100),
    estado VARCHAR(50),
    rua VARCHAR(255),
    numero VARCHAR(10),
    cep VARCHAR(10),
    bairro VARCHAR(100),
    complemento VARCHAR(255),
    usuario VARCHAR(50),
    senha VARCHAR(255)
);

-- Tabela Pedido
CREATE TABLE IF NOT EXISTS Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    data_pedido DATE,
    total FLOAT,
    status VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela ItemPedido (ligação entre Pedido e Livro)
CREATE TABLE IF NOT EXISTS ItemPedido (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_livro INT,
    quantidade INT NOT NULL,
    preco_unitario FLOAT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_livro) REFERENCES Livro(id_livro)
);


-- Inserindo dados na tabela Autor
INSERT INTO Autor (nome, nacionalidade, data_nascimento) VALUES 
('J.R.R. Tolkien', 'Britânico', '1892-01-03'),
('George Orwell', 'Britânico', '1903-06-25'),
('Jane Austen', 'Britânica', '1775-12-16'),
('Isaac Asimov', 'Russo-Americano', '1920-01-02');

-- Inserindo dados na tabela Categoria
INSERT INTO Categoria (nome) VALUES 
('Ficção'), 
('Ciência'), 
('Romance'), 
('Fantasia');

-- Inserindo dados na tabela Editora
INSERT INTO Editora (nome) VALUES 
('HarperCollins'), 
('Penguin Books'), 
('Oxford University Press'), 
('Doubleday');

-- Inserindo dados na tabela Livro
INSERT INTO Livro (titulo, id_autor, genero, preco, data_publicacao, estoque, id_editora, id_categoria) VALUES 
('O Senhor dos Anéis', 1, 'Fantasia', 39.90, '1954-07-29', 10, 1, 4),
('1984', 2, 'Distopia', 25.90, '1949-06-08', 15, 2, 1),
('Orgulho e Preconceito', 3, 'Romance', 27.90, '1813-01-28', 10, 3, 3),
('Fundação', 4, 'Ficção Científica', 32.50, '1951-05-01', 8, 4, 2);

-- Inserindo dados na tabela Cliente
INSERT INTO Cliente (cpf, nome, email, telefone, cidade, estado, rua, numero, cep, bairro, complemento, usuario, senha) VALUES 
('111.222.333-44', 'Ana Silva', 'ana.silva@email.com', '99999-0001', 'Cidade X', 'Estado Y', 'Rua A', '101', '12345-678', 'Bairro Z', 'Apto 10', 'ana.silva', 'senha123'),
('555.666.777-88', 'Carlos Souza', 'carlos.souza@email.com', '99999-0002', 'Cidade W', 'Estado V', 'Rua B', '202', '87654-321', 'Bairro Q', '', 'carlos.souza', 'senha456');

-- Inserindo dados na tabela Pedido
INSERT INTO Pedido (id_cliente, data_pedido, total, status) VALUES 
(1, '2024-11-01', 79.80, 'Concluído'),
(2, '2024-11-02', 25.90, 'Pendente');

-- Inserindo dados na tabela ItemPedido
INSERT INTO ItemPedido (id_pedido, id_livro, quantidade, preco_unitario) VALUES 
(1, 1, 2, 39.90),
(2, 2, 1, 25.90);