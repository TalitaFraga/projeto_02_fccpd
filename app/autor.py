from database import get_connection

class Autor:
    def listar_autores(self):
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nome FROM Autor")
        autores = cursor.fetchall()
        cursor.close()
        connection.close()
        return autores