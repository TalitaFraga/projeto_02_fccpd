# Use uma imagem Python como base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copie os arquivos menu.py, client.py, livro.py e pedidos.py para o contêiner
COPY menu.py client.py livro.py pedidos.py /app/

# Instale a biblioteca mysql-connector-python para conexão com o MySQL
RUN pip install mysql-connector-python

# Executa o script menu.py
CMD ["python", "menu.py"]
