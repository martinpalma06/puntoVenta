from app.db import DBConnection

class Pago:
    def __init__(self):
        self.db = DBConnection()

    def crear_pago(self, pedido_id, metodo, estado):
        query = """
        INSERT INTO pagos (pedido_id, metodo, estado)
        VALUES (%s, %s, %s)
        """
        self.db.execute_query(query, (pedido_id, metodo, estado))

    def obtener_pago_por_pedido(self, pedido_id):
        query = "SELECT * FROM pagos WHERE pedido_id = %s"
        return self.db.fetch_one(query, (pedido_id,))
