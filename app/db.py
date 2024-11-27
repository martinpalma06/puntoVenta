# app/db.py
import mysql.connector

def obtener_conexion():
    try:
        # Intentamos establecer la conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Tu usuario de MySQL
            password="12345678",  # Tu contraseña de MySQL
            database="comida_db"  # Nombre de la base de datos
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar con la base de datos: {err}")
        return None
