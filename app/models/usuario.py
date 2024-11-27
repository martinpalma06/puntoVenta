from app.db import DBConnection

class Usuario:
    def __init__(self):
        self.db = DBConnection()

    def obtener_usuario_por_email(self, email):
        query = "SELECT * FROM usuarios WHERE email = %s"
        return self.db.fetch_one(query, (email,))

    def crear_usuario(self, nombre, direccion, email, password):
        query = """
        INSERT INTO usuarios (nombre, direccion, email, password)
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (nombre, direccion, email, password))
