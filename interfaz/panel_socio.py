import tkinter as tk
from tkinter import ttk

class PanelSocio(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Socio")
        self.geometry("400x300")
        self.socio = socio

# meter los Widgets dentro de variables.
        ttk.Label(self, text=f"Bienvenido/a: {socio.nombre_completo}").pack(pady=20)
        ttk.Label(self, text=f"Usuario: {socio.get_usuario()}").pack()
        ttk.Label(self, text=f"Estado: {socio.estado_cuota}").pack()
        ttk.Label(self, text=f"Rol: {socio.rol}").pack(pady=10)
        
        ttk.Button(self, text="Cerrar", command=self.destroy).pack(pady=20)