from app.models.pago import Pago

class PagoController:
    def __init__(self):
        self.pago_model = Pago()

    def procesar_pago(self, pedido_id, metodo_pago):
        if metodo_pago not in ["Tarjeta", "Efectivo"]:
            return False
        self.pago_model.crear_pago(pedido_id, metodo_pago, "Procesado")
        return True
