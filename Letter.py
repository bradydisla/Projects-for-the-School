import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Una nota para ti", mensaje)

# Mensaje que quieres mostrar
mensaje = (
    "Hola 😊\n\n"
    "Quería tomar un momento para decirte algo sincero:\n"
    "Estoy genuinamente interesado en conocerte. Me encantaría\n"
    "descubrir quién eres, escuchar tus historias y ver qué\n"
    "podemos construir juntos, con calma y autenticidad.\n\n"
    "Si estás abierta a eso, aquí estaré, con mente clara\n"
    "y corazón abierto.\n\n"
    "– Alguien con buenas intenciones"
)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Carta especial")
ventana.geometry("400x300")
ventana.configure(bg="#f0f8ff")

# Etiqueta de presentación
etiqueta = tk.Label(ventana, text="💌 Haz clic para leer una nota especial 💌",
                    bg="#f0f8ff", fg="#333", font=("Georgia", 14), wraplength=380)
etiqueta.pack(pady=60)

# Botón para mostrar el mensaje
boton = tk.Button(ventana, text="Abrir nota",
                  font=("Georgia", 12), bg="#ffffff", fg="#444",
                  relief="raised", command=mostrar_mensaje)
boton.pack()

# Ejecutar la ventana
ventana.mainloop()