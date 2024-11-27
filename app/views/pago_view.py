from tkinter import Toplevel, Label, Button, StringVar, Radiobutton

class PagoView:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_pago(self, pedido_id):
        ventana = Toplevel()
        ventana.title("Pago")

        Label(ventana, text="Seleccione un método de pago:").pack(pady=10)

        metodo_pago = StringVar(value="Tarjeta")
        Radiobutton(ventana, text="Tarjeta", variable=metodo_pago, value="Tarjeta").pack()
        Radiobutton(ventana, text="Efectivo", variable=metodo_pago, value="Efectivo").pack()

        Button(
            ventana,
            text="Procesar Pago",
            command=lambda: self.controlador.procesar_pago(pedido_id, metodo_pago.get())
        ).pack(pady=20)
