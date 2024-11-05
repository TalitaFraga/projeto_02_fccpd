import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="user",
        password="userpassword",
        database="livraria"
    )
