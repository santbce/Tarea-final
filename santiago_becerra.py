# Configuracion de la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Recetas")
ventana.geometry("400x450")

# Etiqueta para el título
etiqueta_titulo = tk.Label(ventana, text="Registra Tu Receta", font=("Arial", 16))
etiqueta_titulo.pack(pady=10)

# Entrada para el nombre de la receta
etiqueta_nombre = tk.Label(ventana, text="Nombre de la receta:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

# Botón para registrar la receta
boton_registrar = tk.Button(ventana, text="Registrar Receta", command=registrar_receta)
boton_registrar.pack(pady=10)

# Separador
separador1 = tk.Label(ventana, text="--------------------")
separador1.pack()

# Sección para ver o eliminar por número
etiqueta_numero = tk.Label(ventana, text="Número de receta:")
etiqueta_numero.pack()
entrada_numero = tk.Entry(ventana, width=10)
entrada_numero.pack()

boton_ver = tk.Button(ventana, text="Ver receta por número", command=ver_receta_por_numero)
boton_ver.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Receta", command=eliminar_receta)
boton_eliminar.pack(pady=5)

# Etiqueta de mensaje para retroalimentación
etiqueta_mensaje = tk.Label(ventana, text="", fg="green")
etiqueta_mensaje.pack()

# Separador
separador2 = tk.Label(ventana, text="--------------------")
separador2.pack()

# Lista para mostrar todas las recetas
etiqueta_lista = tk.Label(ventana, text="Recetas:")
etiqueta_lista.pack()
lista_recetas = tk.Listbox(ventana, width=50)
lista_recetas.pack(pady=10)

# Llamar a mostrar_recetas() al inicio para mostrar las recetas si el archivo existe
mostrar_recetas()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
