DROP DATABASE IF EXISTS livraria;
create database livraria;
use livraria;

create table Funcionario (
	id_funcionario INT primary key auto_increment,
	cpf VARCHAR(11) NOT null UNIQUE,
	salario FLOAT NOT NULL,
	celular VARCHAR(15) NOT NULL,
	nome VARCHAR(200) NOT NULL,
	senha VARCHAR(255) NOT NULL,
	email_principal VARCHAR(200) NOT NULL,
	rua VARCHAR(200) NOT NULL,
	numero INT NOT NULL,
	cep varchar(8) NOT NULL,
	bairro VARCHAR(200)
	

);

create table Cliente(
	id_cliente int primary key auto_increment,
	usuario varchar(50) not null,
	senha varchar(255) not null,
	cpf VARCHAR(11) not null unique,
	nome varchar(255) not null,
	email varchar(255) not null,
	telefone varchar(11) not null,
	rua varchar(255) not null,
	cidade varchar(255) not null,
	estado varchar(255) not null,
	numero int not null,
	cep varchar(8) not null,
	bairro varchar(255) not null,
	complemento varchar(255) NULL
	
);

create table Autor(
	id_autor INT primary key AUTO_INCREMENT not null,
	nome VARCHAR(255) not null,
	nacionalidade VARCHAR(255) not null,
	data_nascimento date not null
	
);

create table Editora(
	id_editora INT primary key auto_increment,
	nome varchar(255) not null
);

create table Categoria(
	id_categoria int primary key AUTO_INCREMENT,
	nome varchar(255) not null
);

create table Livro(
	id_livro INT primary key AUTO_INCREMENT,
	titulo VARCHAR(255) not null,
	id_autor INT not null,
	genero VARCHAR(255) not null,
	preco FLOAT not null,
	data_publicacao date not null,
	estoque int not null,
	id_editora int not null,
	id_categoria int not null,
	
	foreign key (id_autor) REFERENCES Autor(id_autor),
	foreign key (id_editora) references Editora(id_editora),
	foreign key (id_categoria) references Categoria(id_categoria)

);


create table Pedido(
	id_pedido int primary key AUTO_INCREMENT,
	data_pedido date not null,
	total float not null,
	status varchar(255) not null,
	id_cliente int not null,
	foreign key (id_cliente) references Cliente(id_cliente)
);

create table ItemPedido(
	id_item int primary key auto_increment,
	id_pedido int not null,
	id_livro int not null,
	quantidade int not null,
	preco_unitario float not null,
	FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_livro) REFERENCES Livro(id_livro)

);


INSERT INTO Cliente (usuario, senha, cpf, nome, rua, cidade, estado, numero, cep, bairro, complemento, email, telefone) VALUES
('user1', 'senha123', '12345678901', 'Alice Silva', 'Rua das Flores', 'São Paulo', 'SP', 101, '01001001', 'Centro', 'Apt 12', 'AliceSilva@hotmail.com', '81994323291'),
('user2', 'senha456', '23456789012', 'Bruno Lima', 'Av. Paulista', 'Sao Paulo', 'SP', 102, '01002002', 'Paulista', 'Sala 45', 'BrunoLima@hotmail.com', '11984313274'),
('user3', 'senha789', '34567890123', 'Carlos Souza', 'Rua Verde', 'Rio de Janeiro', 'RJ', 103, '21010301', 'Laranjeiras', 'Casa', 'CarlosSouza@hotmail.com', '21987823291'),
('user4', 'senha321', '45678901234', 'Daniela Ramos', 'Rua das Palmeiras', 'Curitiba', 'PR', 104, '80030404', 'Centro Cívico', '', 'DanielaRamos@hotmail.com', '85932323291'),
('user5', 'senha654', '56789012345', 'Eduardo Torres', 'Rua Azul', 'Belo Horizonte', 'MG', 105, '30150505', 'Savassi', 'Apt 1001', 'EduardoTorres@hotmail.com', '81994325432'),
('user6', 'senha987', '67890123456', 'Fernanda Oliveira', 'Av. Brasil', 'Fortaleza', 'CE', 106, '60060606', 'Aldeota', 'Apt 202', 'FernandaOliveira@hotmail.com', '41934975291');



INSERT INTO Funcionario (cpf, salario, celular, nome, senha, email_principal, rua, numero, cep, bairro) VALUES
('12345678900', 3500.50, '(11) 91234-5678', 'Joao Martins', 'senhaadmin', 'joao.martins@livraria.com', 'Rua Principal', 1, '12345678', 'Centro');


INSERT INTO Categoria (nome) VALUES
('Romance'), ('Ficcao Cientifica'), ('Fantasia'), ('Biografia'), ('Historia'), ('Filosofia'),
('Autoajuda'), ('Tecnologia'), ('Negocios'), ('Literatura Brasileira'), ('Literatura Estrangeira'), ('Infantil');


INSERT INTO Autor (nome, nacionalidade, data_nascimento) VALUES
('Machado de Assis', 'Brasileiro', '1839-06-21'),
('George Orwell', 'Britanico', '1903-06-25'),
('J.K. Rowling', 'Britanica', '1965-07-31'),
('Isaac Asimov', 'Russo-Americano', '1920-01-02'),
('Clarice Lispector', 'Ucraniana-Brasileira', '1920-12-10'),
('Yuval Noah Harari', 'Israelense', '1976-02-24');

INSERT INTO Editora (nome) VALUES
('Editora Moderna'), ('Companhia das Letras'), ('HarperCollins');


INSERT INTO Livro (titulo, id_autor, genero, preco, data_publicacao, estoque, id_editora, id_categoria) VALUES
('Dom Casmurro', 1, 'Romance', 39.90, '1899-01-01', 50, 1, 10),
('1984', 2, 'Ficcao Cientifica', 29.90, '1949-06-08', 30, 2, 2),
('Harry Potter e a Pedra Filosofal', 3, 'Fantasia', 49.90, '1997-06-26', 40, 3, 3),
('Fundação', 4, 'Ficcao Cientifica', 34.90, '1951-01-01', 20, 1, 2),
('A Hora da Estrela', 5, 'Literatura Brasileira', 25.90, '1977-10-01', 45, 2, 10),
('Sapiens: Uma Breve História da Humanidade', 6, 'Historia', 59.90, '2011-01-01', 15, 3, 5);

