import tkinter as tk
from tkinter import messagebox
from app.controllers.producto_controller import ProductoController
from app.db import obtener_conexion

class CatalogoView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Selección de Productos")
        self.root.geometry("400x300")

        self.productos = self.obtener_productos()  # Traemos la lista de productos desde la base de datos
        self.carrito = []  # Carrito vacío inicialmente
        self.botones_productos = []  # Guardamos los botones para evitar duplicados

    def obtener_productos(self):
        # Conexión a la base de datos para obtener los productos
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos

    def mostrar_productos(self):
        # Mostramos los productos en la interfaz
        print("Productos disponibles:")
        for producto in self.productos:
            nombre, precio_base, descripcion = producto[1], producto[3], producto[2]
            
            # Crear solo un botón por producto
            if not any(p[0] == producto[0] for p in self.botones_productos):
                boton_producto = tk.Button(self.root, text=f"{nombre} - ${precio_base}", command=lambda p=producto: self.seleccionar_ingredientes(p))
                boton_producto.pack()
                self.botones_productos.append(producto)  # Añadimos el producto a la lista de botones

        # Mostrar carrito y finalizar compra
        boton_carrito = tk.Button(self.root, text="Ver Carrito", command=self.mostrar_carrito)
        boton_carrito.pack()

        self.root.mainloop()

    def seleccionar_ingredientes(self, producto):
        # Crear una nueva ventana para seleccionar ingredientes
        ventana_ingredientes = tk.Toplevel(self.root)
        ventana_ingredientes.title(f"Seleccionar Ingredientes - {producto[1]}")
        ventana_ingredientes.geometry("300x250")
        
        # Obtener ingredientes disponibles
        ingredientes_disponibles = self.obtener_ingredientes_producto(producto[0])
        
        # Lista para guardar las opciones seleccionadas
        ingredientes_seleccionados = []
        precio_final = producto[3]  # Precio base del producto

        # Mostrar los ingredientes disponibles como checkboxes
        for ingrediente in ingredientes_disponibles:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(ventana_ingredientes, text=f"{ingrediente[0]} (+${ingrediente[1]:.2f})", variable=var)
            checkbox.pack()
            ingredientes_seleccionados.append((ingrediente[0], ingrediente[1], var))
        
        # Botón para confirmar la selección
        boton_confirmar = tk.Button(ventana_ingredientes, text="Confirmar", command=lambda p=producto, ingredientes=ingredientes_seleccionados, ventana=ventana_ingredientes: self.agregar_producto_con_ingredientes(p, ingredientes, ventana))
        boton_confirmar.pack()

    def obtener_ingredientes_producto(self, producto_id):
        # Obtiene los ingredientes para un producto específico desde la base de datos
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_ingrediente, precio_adicional FROM ingredientes WHERE producto_id = %s", (producto_id,))
        ingredientes = cursor.fetchall()
        cursor.close()
        conexion.close()
        return ingredientes

    def agregar_producto_con_ingredientes(self, producto, ingredientes_seleccionados, ventana):
        # Calcular el precio final sumando el precio base del producto y el costo adicional por los ingredientes seleccionados
        precio_final = producto[3]  # Precio base del producto
        ingredientes_finales = []

        for ingrediente, precio_adicional, var in ingredientes_seleccionados:
            if var.get():  # Si el ingrediente está seleccionado
                ingredientes_finales.append(ingrediente)
                precio_final += precio_adicional  # Añadimos el costo adicional del ingrediente
        
        # Agregar el producto con los ingredientes seleccionados y el precio final al carrito
        producto_con_ingredientes = (producto[1], precio_final, ingredientes_finales)
        
        # Evitar agregar duplicados al carrito
        if not any(p[0] == producto_con_ingredientes[0] and p[1] == producto_con_ingredientes[1] for p in self.carrito):
            self.carrito.append(producto_con_ingredientes)
            print(f"Producto {producto_con_ingredientes[0]} con ingredientes {', '.join(ingredientes_finales)} agregado al carrito. Precio final: ${precio_final:.2f}")
        else:
            print(f"El producto {producto_con_ingredientes[0]} ya está en el carrito.")
        
        # Cerrar la ventana de selección de ingredientes
        ventana.destroy()

    def mostrar_carrito(self):
        # Mostrar los productos en el carrito
        carrito_texto = "\n".join([f"{producto[0]} con ingredientes: {', '.join(producto[2])} - Precio: ${producto[1]:.2f}" for producto in self.carrito])
        messagebox.showinfo("Carrito", f"Productos en tu carrito:\n{carrito_texto}")
