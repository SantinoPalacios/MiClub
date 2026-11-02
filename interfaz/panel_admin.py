import tkinter as tk
from tkinter import ttk

class PanelAdmin(tk.Toplevel):
    def __init__(self, master, socio):
        super().__init__(master)
        self.title("Panel del Administrador")
        self.geometry("400x300")
        self.socio = socio
        
        ttk.Label(self, text=f"Administrador: {socio.nombre_completo}").pack(pady=20)
        ttk.Label(self, text="Panel de gestión de socios").pack()
        
        ttk.Button(self, text="Cerrar", command=self.destroy).pack(pady=20)