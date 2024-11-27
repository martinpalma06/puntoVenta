# app/controllers/login_controller.py
from app.db import obtener_conexion

class LoginController:
    def __init__(self):
        self.login_exitoso = False  # Inicializa el estado del login

    def validar_login(self, email, password):
        """
        Lógica para verificar el inicio de sesión con la base de datos.
        """
        conexion = obtener_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return False

        cursor = conexion.cursor()
        query = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        resultado = cursor.fetchone()

        if resultado:  # Si se encuentra un resultado, las credenciales son correctas
            self.login_exitoso = True
            return True
        else:
            self.login_exitoso = False
            return False
