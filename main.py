# main.py
from app.controllers.login_controller import LoginController
from app.views.main_view import MainView

def main():
    controlador_login = LoginController()  # Inicializamos el controlador de login
    vista_login = MainView(controlador_login)  # Pasamos el controlador a la vista
    vista_login.mostrar_formulario_login()  # Mostramos el formulario de login

if __name__ == "__main__":
    main()
