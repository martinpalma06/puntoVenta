# app/views/main_view.py
import tkinter as tk
from tkinter import messagebox
from app.controllers.login_controller import LoginController
from app.controllers.producto_controller import ProductoController  # Importamos el controlador de productos
from app.views.catalogo_view import CatalogoView  # Vista para seleccionar productos

class MainView:
    def __init__(self, controlador_login):
        self.controlador_login = controlador_login
        self.root = tk.Tk()
        self.root.title("Sistema de Venta")
        self.root.geometry("400x300")

    def mostrar_formulario_login(self):
        print("Formulario de login mostrado.")
        self.label_email = tk.Label(self.root, text="Email")
        self.label_email.pack()

        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()

        self.label_password = tk.Label(self.root, text="Contraseña")
        self.label_password.pack()

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        boton_login = tk.Button(self.root, text="Iniciar sesión", command=self.login)
        boton_login.pack()

        self.root.mainloop()

    def login(self):
        email_ingresado = self.entry_email.get()
        password_ingresada = self.entry_password.get()

        # Validamos el login
        if self.controlador_login.validar_login(email_ingresado, password_ingresada):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            self.root.quit()  # Cerramos la ventana de login
            self.mostrar_seleccion_productos()
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos.")

    def mostrar_seleccion_productos(self):
        # Ahora que el login es exitoso, mostramos la vista de selección de productos
        self.catalogo_view = CatalogoView()
        self.catalogo_view.mostrar_productos()
