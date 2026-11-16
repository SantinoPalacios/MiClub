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
from servicios.servicio_autenticacion import autenticar


class PantallaLogin(tk.Frame):
    """Formulario de ingreso. Al validar, avisa a la app principal."""

    def __init__(self, padre, app):
        super().__init__(padre, bg=PANEL)
        self.app = app
        self.pack(fill="both", expand=True)
        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(
            self,
            text="INICIAR SESIÓN",
            font=FUENTE_TITULO,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(40, 8))

        tk.Label(
            self,
            text=f"Ingresá con tu cuenta de {NOMBRE_CLUB}.",
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=5)

        formulario = tk.Frame(self, bg=PANEL)
        formulario.pack(pady=25)

        tk.Label(
            formulario,
            text="Usuario:",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=TEXTO,
        ).pack(anchor="w")

        self.entrada_usuario = tk.Entry(
            formulario,
            font=FUENTE,
            width=27,
        )
        self.entrada_usuario.pack(anchor="w", pady=(4, 15))

        tk.Label(
            formulario,
            text="Contraseña:",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=TEXTO,
        ).pack(anchor="w")

        fila_contrasenia = tk.Frame(formulario, bg=PANEL)
        fila_contrasenia.pack(anchor="w", pady=4)

        self.entrada_contrasenia = tk.Entry(
            fila_contrasenia,
            font=FUENTE,
            width=27,
            show="*",
        )
        self.entrada_contrasenia.pack(side="left")

        self.boton_ver = tk.Button(
            fila_contrasenia,
            text="Mostrar",
            font=FUENTE_CHICA,
            bg=PANEL,
            fg=TEXTO,
            relief="flat",
            cursor="hand2",
            command=self._alternar_contrasenia,
        )
        self.boton_ver.pack(side="left", padx=6)

        self.app.crear_boton(
            self,
            "INGRESAR",
            self._ingresar,
            ancho=22,
        ).pack(pady=(20, 10))

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

        self.entrada_usuario.focus()
        self.bind("<Return>", lambda evento: self._ingresar())

    def _alternar_contrasenia(self):
        if self.entrada_contrasenia.cget("show") == "*":
            self.entrada_contrasenia.configure(show="")
            self.boton_ver.configure(text="Ocultar")
        else:
            self.entrada_contrasenia.configure(show="*")
            self.boton_ver.configure(text="Mostrar")

    def _ingresar(self):
        usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contrasenia.get()

        if not usuario or not contrasenia:
            messagebox.showwarning(
                "Campos incompletos",
                "Completá el usuario y la contraseña.",
            )
            return

        socio = autenticar(usuario, contrasenia)
        if socio is None:
            messagebox.showerror(
                "Error de acceso",
                "Usuario o contraseña incorrectos.",
            )
            self.entrada_contrasenia.delete(0, tk.END)
            self.entrada_contrasenia.focus()
            return

        self.app.iniciar_sesion(socio)