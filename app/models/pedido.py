from app.db import DBConnection

class Pedido:
    def __init__(self):
        self.db = DBConnection()

    def crear_pedido(self, usuario_id, total, estado):
        query = """
        INSERT INTO pedidos (usuario_id, total, estado)
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(query, (usuario_id, total, estado))
        return self.db.cursor.lastrowid

    def agregar_producto_a_pedido(self, pedido_id, producto_id, cantidad):
        query = """
        INSERT INTO inventario (producto_id, stock)
        VALUES (%s, %s)
        """
        self.db.execute_query(query, (producto_id, cantidad))

    def obtener_pedido_por_id(self, pedido_id):
        query = "SELECT * FROM pedidos WHERE id = %s"
        return self.db.fetch_one(query, (pedido_id,))

    def actualizar_estado_pedido(self, pedido_id, estado):
        query = "UPDATE pedidos SET estado = %s WHERE id = %s"
        self.db.execute_query(query, (estado, pedido_id))
