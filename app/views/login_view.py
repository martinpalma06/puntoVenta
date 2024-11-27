from tkinter import Toplevel, Label, Entry, Button

class LoginView:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_login(self):
        ventana = Toplevel()
        ventana.title("Iniciar Sesión")

        Label(ventana, text="Email:").grid(row=0, column=0, padx=10, pady=5)
        email_entry = Entry(ventana)
        email_entry.grid(row=0, column=1)

        Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        password_entry = Entry(ventana, show="*")
        password_entry.grid(row=1, column=1)

        Button(
            ventana,
            text="Iniciar Sesión",
            command=lambda: self.controlador.iniciar_sesion(email_entry.get(), password_entry.get())
        ).grid(row=2, column=0, columnspan=2, pady=10)

        Label(ventana, text="¿No tienes cuenta? Regístrate:").grid(row=3, column=0, columnspan=2)
        Button(
            ventana,
            text="Registrar",
            command=lambda: self.mostrar_registro()
        ).grid(row=4, column=0, columnspan=2, pady=5)

    def mostrar_registro(self):
        ventana = Toplevel()
        ventana.title("Registro de Usuario")

        Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        nombre_entry = Entry(ventana)
        nombre_entry.grid(row=0, column=1)

        Label(ventana, text="Dirección:").grid(row=1, column=0, padx=10, pady=5)
        direccion_entry = Entry(ventana)
        direccion_entry.grid(row=1, column=1)

        Label(ventana, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        email_entry = Entry(ventana)
        email_entry.grid(row=2, column=1)

        Label(ventana, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5)
        password_entry = Entry(ventana, show="*")
        password_entry.grid(row=3, column=1)

        Button(
            ventana,
            text="Registrar",
            command=lambda: self.controlador.registrar_usuario(
                nombre_entry.get(),
                direccion_entry.get(),
                email_entry.get(),
                password_entry.get()
            )
        ).grid(row=4, column=0, columnspan=2, pady=10)
