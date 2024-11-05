from flask import Flask, request, jsonify
from livro import Livro  # Outros DAOs podem ser importados conforme necessário
from autor import Autor 
app = Flask(__name__)
livro = Livro()
autor = Autor()

@app.route('/')
def index():
    return jsonify({"mensagem": "Bem-vindo à API da Livraria"})

# Rota para listar livros
@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = livro.listar_livros()
    return jsonify(livros)

#Rota para listar autores
@app.route('/autores', methods=['GET'])
def listar_autores():
    autores = autor.listar_autores()
    return jsonify(autores)

# Rota para adicionar um livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    dados = request.json
    livro.inserir_livro(
        titulo=dados['titulo'],
        preco=dados['preco'],
        estoque=dados['estoque'],
        id_categoria=dados['id_categoria'],
        id_autor=dados['id_autor']
    )
    return jsonify({"mensagem": "Livro adicionado com sucesso"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
