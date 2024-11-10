# Livraria

Esta é uma aplicação para gerenciar uma livraria, desenvolvida em Python com banco de dados MySQL. A aplicação permite operações CRUD (Create, Read, Update, Delete) para gerenciar livros, clientes, e pedidos, incluindo funcionalidades de compra de livros.


## Tecnologias Utilizadas

- Python: Linguagem principal da aplicação.
- MySQL: Banco de dados relacional para armazenar informações de livros, clientes, pedidos e categorias.
- Docker: Utilizado para facilitar o ambiente de desenvolvimento, incluindo a configuração do banco de dados e da aplicação.

## Funcionalidades da Aplicação

A aplicação possui as seguintes funcionalidades:

1. Gerenciamento de Livros
- Listar Livros: Lista todos os livros disponíveis no banco de dados.
- Adicionar Livro: Adiciona um novo livro ao banco de dados.
- Remover Livro: Remove um livro específico pelo seu ID.
- Atualizar Livro: Atualiza as informações de um livro existente no banco de dados.
2. Gerenciamento de Clientes
- Cadastro de Cliente: Registra um novo cliente no sistema.
- Atualização de Cliente: Atualiza as informações de um cliente específico.
- Exclusão de Cliente: Remove um cliente do sistema pelo ID.
3. Gerenciamento de Pedidos
- Compra de Livro: Registra a compra de um livro pelo cliente e cria um pedido correspondente.
- Listar Pedidos: Exibe todos os pedidos feitos, mostrando o cliente, livros comprados, quantidade e status do pedido.
- Atualizar Pedido: Atualiza o status do pedido (ex.: “aberto”, “finalizado”).

## Como Executar a Aplicação

Pré-requisitos
- Docker e Docker Compose instalados na máquina.

##Passos para Executar
1. Clone o Repositório

```sh
https://github.com/TalitaFraga/projeto_02_fccpd.git
```
2. Configurar o Docker Compose
Verifique o arquivo docker-compose.yml para garantir que ele está configurado corretamente, incluindo o banco de dados e a aplicação.

3. Suba os Containers com Docker Compose
Este comando irá construir e iniciar o ambiente completo, incluindo a aplicação Python e o MySQL.
```sh
docker-compose up --build
```

4. Acessar a Aplicação
A aplicação pode ser acessada diretamente pelo terminal, onde você pode interagir com o menu para realizar operações CRUD em livros, clientes e pedidos.


#### Para iniciar o programa e acessar o menu principal, execute:
```sh
docker-compose exec app bash
python main.py
```


