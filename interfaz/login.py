import tkinter as tk
from tkinter import messagebox
from interfaz.panel_admin import PanelAdmin
from interfaz.panel_socio import PanelSocio
from servicios.servicio_autenticacion import autenticar


ROJO = "#6B0504"
BLANCO = "#F4F4F9"
GRIS = "#F2F2F2"
TEXTO = "#0B0A0A"


class VentanaLogin(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("River Plate | Inicio de sesión")
        self.geometry("950x650")
        self.minsize(850, 550)
        self.configure(bg=GRIS)

        # Encabezado.
        encabezado = tk.Frame(self, bg=ROJO, height=85)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="RIVER PLATE",
            font=("Arial", 24, "bold"),
            bg=ROJO,
            fg=BLANCO
        ).pack(side="left", padx=25, pady=15)

        tk.Label(
            encabezado,
            text="SISTEMA DEL CLUB",
            font=("Arial", 12, "bold"),
            bg=ROJO,
            fg=BLANCO
        ).pack(side="right", padx=25)

        # Contenedor principal.
        self.contenido = tk.Frame(self, bg=BLANCO)
        self.contenido.pack(fill="both", expand=True, padx=12, pady=12)

        self.crear_login()

        # Permite ingresar presionando Enter.
        self.bind("<Return>", lambda event: self.iniciar_sesion())

    def crear_login(self):

        tk.Label(
            self.contenido,
            text="INICIAR SESIÓN",
            font=("Arial", 20, "bold"),
            bg=BLANCO,
            fg=ROJO
        ).pack(pady=(60, 15))

        tk.Label(
            self.contenido,
            text="Ingresá con tu cuenta de River Plate.",
            font=("Arial", 11),
            bg=BLANCO,
            fg=TEXTO
        ).pack(pady=5)

        formulario = tk.Frame(self.contenido, bg=BLANCO)
        formulario.pack(pady=20)

        # Nombre de usuario.
        tk.Label(
            formulario,
            text="Nombre de usuario:",
            font=("Arial", 11, "bold"),
            bg=BLANCO,
            fg=TEXTO
        ).pack(anchor="w")

        self.entrada_usuario = tk.Entry(
            formulario,
            font=("Arial", 12),
            width=27
        )
        self.entrada_usuario.pack(anchor="w", pady=(5, 15))

        # Contraseña.
        tk.Label(
            formulario,
            text="Contraseña:",
            font=("Arial", 11, "bold"),
            bg=BLANCO,
            fg=TEXTO
        ).pack(anchor="w")

        campo_frame = tk.Frame(formulario, bg=BLANCO)
        campo_frame.pack(pady=5, anchor="w")

        self.entrada_contrasenia = tk.Entry(
            campo_frame,
            font=("Arial", 12),
            width=27,
            show="*"
        )
        self.entrada_contrasenia.pack(side="left")

        # Botón para mostrar u ocultar la contraseña.
        self.boton_ojo = tk.Button(
            campo_frame,
            text="👁",
            bg=BLANCO,
            fg=TEXTO,
            relief="flat",
            cursor="hand2",
            command=self.alternar_contrasenia
        )
        self.boton_ojo.pack(side="left", padx=5)

        # Botón de ingreso.
        tk.Button(
            self.contenido,
            text="INGRESAR",
            command=self.iniciar_sesion,
            bg=ROJO,
            fg=BLANCO,
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            cursor="hand2"
        ).pack(pady=15)

        self.entrada_usuario.focus()

    def alternar_contrasenia(self):

        if self.entrada_contrasenia.cget("show") == "*":
            self.entrada_contrasenia.configure(show="")
            self.boton_ojo.configure(text="🫣")

        else:
            self.entrada_contrasenia.configure(show="*")
            self.boton_ojo.configure(text="👁")

    def iniciar_sesion(self):

        usuario = self.entrada_usuario.get().strip()
        contrasenia = self.entrada_contrasenia.get()

        # Validar que los campos no estén vacíos.
        if not usuario or not contrasenia:
            messagebox.showwarning(
                "Campos vacíos",
                "Debe completar todos los campos",
                parent=self
            )
            return

        try:
            # Autenticar mediante el servicio.
            socio = autenticar(usuario, contrasenia)

            # Comprobar si las credenciales son incorrectas.
            if socio is None:
                messagebox.showerror(
                    "Error de acceso",
                    "El usuario o la contraseña son incorrectos.",
                    parent=self
                )
                return

            # Abrir el panel correspondiente según el rol.
            if socio.rol == "admin":
                PanelAdmin(self, socio)

            elif socio.rol == "socio":
                PanelSocio(self, socio)

            else:
                messagebox.showerror(
                    "Error",
                    "El rol del usuario no es válido.",
                    parent=self
                )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"No se pudo iniciar sesión:\n{error}",
                parent=self
            )


if __name__ == "__main__":
    app = VentanaLogin()
    app.mainloop()