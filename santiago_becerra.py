
# Santiago Jose Becerra Peñalosa
import tkinter as tk
import csv
import random
import math
import os

nombre_archivo = "recetas.csv"

# Función para registrar una nueva receta
def registrar_receta():
    nombre_receta = entrada_nombre.get()

    if nombre_receta == "":
        etiqueta_mensaje["text"] = "Ingresa el nombre de la receta."
        return

    tiempo_coccion_c = random.randint(15, 90)
    tiempo_coccion_f = math.floor(tiempo_coccion_c * 1.8 + 32)

    fila = [nombre_receta, tiempo_coccion_c, tiempo_coccion_f]

    existe_archivo = os.path.isfile(nombre_archivo)

    with open(nombre_archivo, "a", newline="") as f:
        escritor = csv.writer(f)
        if not existe_archivo:
            escritor.writerow(["Nombre de la receta", "Tiempo de cocción (C)", "Tiempo de cocción (F)"])
        escritor.writerow(fila)

    etiqueta_mensaje["text"] = "¡Receta registrada!"
    entrada_nombre.delete(0, tk.END)
    mostrar_recetas()

# Función para ver una receta específica por su número
def ver_receta_por_numero():
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
                receta = filas[numero]
                etiqueta_mensaje["text"] = "Receta: " + receta[0] + "\nTiempo: " + receta[1] + "°C / " + receta[2] + "°F"
            else:
                etiqueta_mensaje["text"] = "Ese número de receta no existe."
    else:
        etiqueta_mensaje["text"] = "No se encontró el archivo de recetas."
