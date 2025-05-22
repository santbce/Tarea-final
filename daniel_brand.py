
# Daniel Alexander Brand Garcia
import tkinter as tk
import csv
import os

# Función para mostrar todas las recetas en la interfaz
def mostrar_recetas():
    lista_recetas.delete(0, tk.END)

    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, "r", newline="") as f:
            lector = csv.reader(f)
            filas = list(lector)

            if len(filas) > 1:
                for i in range(1, len(filas)):
                    receta = filas[i]
                    texto_mostrar = str(i) + ". " + receta[0] + " - " + receta[1] + "°C - " + receta[2] + "°F"
                    lista_recetas.insert(tk.END, texto_mostrar)
            else:
                lista_recetas.insert(tk.END, "No hay recetas registradas aún.")
    else:
        lista_recetas.insert(tk.END, "No hay recetas registradas aún.")

# Función para eliminar una receta por su número
def eliminar_receta():
    texto_numero = entrada_numero.get()
    if texto_numero == "" or not texto_numero.isdigit():
        etiqueta_mensaje["text"] = "Ingresa un número de receta válido."
        return
    numero = int(texto_numero)

    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, "r", newline="") as f:
            lector = csv.reader(f)
            filas = list(lector)

        if len(filas) > 1 and 1 <= numero < len(filas):
            del filas[numero]
            with open(nombre_archivo, "w", newline="") as f:
                escritor = csv.writer(f)
                escritor.writerows(filas)
            etiqueta_mensaje["text"] = "Receta eliminada."
            mostrar_recetas()
        else:
            etiqueta_mensaje["text"] = "Ese número de receta no existe."
    else:
        etiqueta_mensaje["text"] = "No se encontró el archivo de recetas."

# Interfaz gráfica (GUI)
ventana = tk.Tk()
ventana.title("Registro de Recetas")
ventana.geometry("400x450")

etiqueta_titulo = tk.Label(ventana, text="Registra Tu Receta", font=("Arial", 16))
etiqueta_titulo.pack(pady=10)

etiqueta_nombre = tk.Label(ventana, text="Nombre de la receta:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack()

boton_registrar = tk.Button(ventana, text="Registrar Receta", command=registrar_receta)
boton_registrar.pack(pady=10)

separador1 = tk.Label(ventana, text="--------------------")
separador1.pack()

etiqueta_numero = tk.Label(ventana, text="Número de receta:")
etiqueta_numero.pack()
entrada_numero = tk.Entry(ventana, width=10)
entrada_numero.pack()

boton_ver = tk.Button(ventana, text="Ver receta por número", command=ver_receta_por_numero)
boton_ver.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Receta", command=eliminar_receta)
boton_eliminar.pack(pady=5)

etiqueta_mensaje = tk.Label(ventana, text="", fg="green")
etiqueta_mensaje.pack()

separador2 = tk.Label(ventana, text="--------------------")
separador2.pack()

etiqueta_lista = tk.Label(ventana, text="Recetas:")
etiqueta_lista.pack()
lista_recetas = tk.Listbox(ventana, width=50)
lista_recetas.pack(pady=10)

mostrar_recetas()
ventana.mainloop()
