from app.db import DBConnection

class Inventario:
    def __init__(self):
        self.db = DBConnection()

    def verificar_disponibilidad(self, producto_id):
        query = "SELECT stock FROM inventario WHERE producto_id = %s"
        stock = self.db.fetch_one(query, (producto_id,))
        return stock["stock"] if stock else 0

    def actualizar_stock(self, producto_id, cantidad):
        query = "UPDATE inventario SET stock = stock - %s WHERE producto_id = %s"
        self.db.execute_query(query, (cantidad, producto_id))
