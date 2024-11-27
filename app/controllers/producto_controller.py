# app/controllers/producto_controller.py
from app.db import obtener_conexion

class ProductoController:
    def __init__(self, vista_catalogo):
        self.vista_catalogo = vista_catalogo
        self.carrito = []

    def obtener_productos(self):
        """
        Obtiene los productos de la base de datos y los pasa a la vista.
        """
        connection = obtener_conexion()
        cursor = connection.cursor()
        
        query = "SELECT * FROM productos"
        cursor.execute(query)
        productos = cursor.fetchall()

        productos_lista = []
        for producto in productos:
            productos_lista.append({
                'id': producto[0],
                'nombre': producto[1],
                'precio': producto[2],
                'descripcion': producto[3],
                'ingredientes': producto[4]
            })

        cursor.close()
        connection.close()

        self.vista_catalogo.mostrar_catalogo(productos_lista)

    def agregar_al_carrito(self, producto):
        """
        Agrega un producto al carrito.
        """
        self.carrito.append(producto)
        print(f"Carrito: {self.carrito}")
