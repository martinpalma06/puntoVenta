from app.db import DBConnection

class Producto:
    def __init__(self):
        self.db = DBConnection()

    def obtener_productos(self):
        query = "SELECT * FROM productos"
        return self.db.fetch_all(query)

    def obtener_producto_por_id(self, producto_id):
        query = "SELECT * FROM productos WHERE id = %s"
        return self.db.fetch_one(query, (producto_id,))

    def agregar_producto(self, nombre, precio, descripcion, ingredientes):
        query = """
        INSERT INTO productos (nombre, precio, descripcion, ingredientes)
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (nombre, precio, descripcion, ingredientes))

    def actualizar_producto(self, producto_id, nombre, precio, descripcion, ingredientes):
        query = """
        UPDATE productos
        SET nombre = %s, precio = %s, descripcion = %s, ingredientes = %s
        WHERE id = %s
        """
        self.db.execute_query(query, (nombre, precio, descripcion, ingredientes, producto_id))

    def eliminar_producto(self, producto_id):
        query = "DELETE FROM productos WHERE id = %s"
        self.db.execute_query(query, (producto_id,))
