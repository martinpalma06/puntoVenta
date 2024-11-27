from tkinter import Toplevel, Label, Button

class CarritoView:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_carrito(self, carrito, total):
        ventana = Toplevel()
        ventana.title("Carrito de Compras")

        for idx, item in enumerate(carrito):
            Label(ventana, text=f"{item['nombre']} - ${item['precio']} x {item['cantidad']}").grid(row=idx, column=0, padx=10, pady=5)
            Button(
                ventana,
                text="Eliminar",
                command=lambda p=item["producto_id"]: self.controlador.eliminar_del_carrito(p)
            ).grid(row=idx, column=1, padx=10)

        Label(ventana, text=f"Total: ${total:.2f}").grid(row=len(carrito), column=0, pady=10)
        Button(ventana, text="Confirmar Pedido", command=self.controlador.confirmar_pedido).grid(row=len(carrito) + 1, column=0, pady=10)
