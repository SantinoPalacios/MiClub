import tkinter as tk
from tkinter import messagebox

from interfaz.tema import (
    FUENTE,
    FUENTE_CHICA,
    FUENTE_NEGRITA,
    FUENTE_TITULO,
    NOMBRE_CLUB,
    PANEL,
    PRIMARIO,
    TEXTO,
)
from servicios.servicio_socios import registrar_socio

CAMPOS_REGISTRO = [
    ("Nombre completo *", "nombre", ""),
    ("Edad", "edad", ""),
    ("Tipo de identificación", "tipo_identificacion", ""),
    ("Identificación *", "identificacion", ""),
    ("Nacionalidad", "nacionalidad", ""),
    ("Usuario único *", "usuario", ""),
    ("Contraseña *", "contrasenia", "*"),
]


class PantallaRegistro(tk.Frame):
    """Formulario de alta de socio. Al guardar, vuelve al login."""

    def __init__(self, padre, app):
        super().__init__(padre, bg=PANEL)
        self.app = app
        self.pack(fill="both", expand=True)
        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(
            self,
            text="REGISTRAR NUEVO SOCIO",
            font=FUENTE_TITULO,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(30, 8))

        tk.Label(
            self,
            text=f"Creá tu cuenta de {NOMBRE_CLUB}. "
            "Los campos marcados con * son obligatorios.",
            font=FUENTE_CHICA,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=5)

        formulario = tk.Frame(self, bg=PANEL)
        formulario.pack(pady=15)

        campos = {}
        for fila, (etiqueta, clave, ocultar) in enumerate(CAMPOS_REGISTRO):
            tk.Label(
                formulario,
                text=f"{etiqueta}:",
                font=FUENTE_NEGRITA,
                bg=PANEL,
                fg=TEXTO,
            ).grid(row=fila, column=0, sticky="e", padx=(0, 12), pady=5)

            entrada = tk.Entry(
                formulario,
                font=FUENTE,
                width=26,
                show=ocultar,
            )
            entrada.grid(row=fila, column=1, pady=5)
            campos[clave] = entrada

        self.app.crear_boton(
            self,
            "CREAR CUENTA",
            lambda: self._guardar(campos),
            ancho=22,
        ).pack(pady=(10, 5))

        tk.Button(
            self,
            text="Volver al inicio",
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO,
            relief="flat",
            cursor="hand2",
            command=self.app.mostrar_bienvenida,
        ).pack(pady=5)

    def _guardar(self, campos):
        try:
            socio = registrar_socio(
                campos["nombre"].get(),
                campos["edad"].get(),
                campos["tipo_identificacion"].get(),
                campos["identificacion"].get(),
                campos["nacionalidad"].get(),
                campos["usuario"].get(),
                campos["contrasenia"].get(),
            )
        except ValueError as error:
            messagebox.showerror("Datos inválidos", str(error))
            return

        messagebox.showinfo(
            "Registro exitoso",
            f"La cuenta de '{socio.get_usuario()}' se creó correctamente.\n\n"
            "Ahora podés iniciar sesión.",
        )
        self.app.mostrar_login()
