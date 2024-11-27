from app.models.producto import Producto
from app.models.pedido import Pedido

class CarritoController:
    def __init__(self):
        self.carrito = []
        self.total = 0.0

    def añadir_producto(self, producto_id, cantidad):
        producto_model = Producto()
        producto = producto_model.obtener_producto_por_id(producto_id)
        if producto:
            self.carrito.append({
                "producto_id": producto["id"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            })
            self.total += producto["precio"] * cantidad

    def eliminar_producto(self, producto_id):
        for item in self.carrito:
            if item["producto_id"] == producto_id:
                self.total -= item["precio"] * item["cantidad"]
                self.carrito.remove(item)
                break

    def vaciar_carrito(self):
        self.carrito = []
        self.total = 0.0

    def obtener_carrito(self):
        return self.carrito, self.total

    def confirmar_pedido(self, usuario_id):
        pedido_model = Pedido()
        pedido_id = pedido_model.crear_pedido(usuario_id, self.total, "Pendiente")
        for item in self.carrito:
            pedido_model.agregar_producto_a_pedido(pedido_id, item["producto_id"], item["cantidad"])
        self.vaciar_carrito()
        return pedido_id
