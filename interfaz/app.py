import tkinter as tk
from tkinter import ttk

from interfaz.login import VentanaLogin
from interfaz.panel_admin import PanelAdmin
from interfaz.panel_socio import PanelSocio
from interfaz.tema import (
    ETIQUETA,
    FONDO,
    FUENTE,
    FUENTE_GRANDE,
    FUENTE_MENU,
    FUENTE_NEGRITA,
    FUENTE_SUBTITULO,
    FUENTE_TABLA,
    LEMA_CLUB,
    NOMBRE_CLUB,
    PANEL,
    PRIMARIO,
    PRIMARIO_HOVER,
    RUTA_LOGO,
    SUBTITULO,
    TEXTO,
    TEXTO_CLARO,
)


class ClubApp(tk.Tk):
    """Ventana única que arma el encabezado, el menú y las pantallas."""

    def __init__(self):
        super().__init__()
        self.socio_actual = None
        self.panel = None

        self.title(f"{NOMBRE_CLUB} | Sistema del club")
        self.geometry("950x650")
        self.minsize(850, 550)
        self.configure(bg=FONDO)

        self._estilizar_tablas()
        self._crear_encabezado()
        self._crear_cuerpo()
        self.mostrar_bienvenida()

        self.protocol("WM_DELETE_WINDOW", self.salir)

    # ── Armado general ─────────────────────────────────────────

    def _estilizar_tablas(self):
        """Aplica el tema del club a las tablas (ttk.Treeview)."""
        estilo = ttk.Style(self)
        estilo.configure(
            "Club.Treeview",
            background=PANEL,
            fieldbackground=PANEL,
            foreground=TEXTO,
            rowheight=28,
            font=FUENTE_TABLA,
        )
        estilo.configure(
            "Club.Treeview.Heading",
            background=PRIMARIO,
            foreground=TEXTO_CLARO,
            font=FUENTE_NEGRITA,
            relief="flat",
        )
        estilo.map(
            "Club.Treeview",
            background=[("selected", PRIMARIO_HOVER)],
            foreground=[("selected", TEXTO_CLARO)],
        )

    def _crear_encabezado(self):
        """Barra superior con el logo (o el nombre) del club."""
        encabezado = tk.Frame(self, bg=PRIMARIO, height=85)
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        self._logo = None
        if RUTA_LOGO.exists():
            self._logo = tk.PhotoImage(file=str(RUTA_LOGO))
            tk.Label(
                encabezado,
                image=self._logo,
                bg=PRIMARIO,
            ).pack(side="left", padx=25, pady=10)
        else:
            tk.Label(
                encabezado,
                text=NOMBRE_CLUB,
                font=FUENTE_SUBTITULO,
                bg=PRIMARIO,
                fg=TEXTO_CLARO,
            ).pack(side="left", padx=25, pady=15)

        tk.Label(
            encabezado,
            text=LEMA_CLUB,
            font=FUENTE_NEGRITA,
            bg=PRIMARIO,
            fg=TEXTO_CLARO,
        ).pack(side="right", padx=25)

    def _crear_cuerpo(self):
        """Contenedor central: menú a la izquierda, contenido a la derecha."""
        principal = tk.Frame(self, bg=FONDO)
        principal.pack(fill="both", expand=True)

        self.menu = tk.Frame(principal, bg=PANEL, width=210)
        self.menu.pack_propagate(False)

        self.contenido = tk.Frame(principal, bg=PANEL)

    # ── Utilidades de pantalla ─────────────────────────────────

    def limpiar_contenido(self):
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    def ocultar_menu(self):
        self.menu.pack_forget()
        self.contenido.pack_forget()
        self.contenido.pack(fill="both", expand=True)

    def mostrar_menu(self, panel):
        """Arma el menú lateral con los botones del panel actual."""
        for elemento in self.menu.winfo_children():
            elemento.destroy()

        tk.Label(
            self.menu,
            text="MENÚ PRINCIPAL",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(25, 15))

        for texto, comando in panel.botones_menu():
            self.crear_boton_menu(texto, comando)

        self.contenido.pack_forget()
        self.menu.pack(side="left", fill="y")
        self.contenido.pack(
            side="right",
            fill="both",
            expand=True,
            padx=12,
            pady=12,
        )

    def crear_boton_menu(self, texto, comando):
        tk.Button(
            self.menu,
            text=texto,
            command=comando,
            font=FUENTE_MENU,
            bg=PANEL,
            fg=TEXTO,
            activebackground=PRIMARIO,
            activeforeground=TEXTO_CLARO,
            relief="flat",
            anchor="w",
            padx=20,
            pady=12,
            cursor="hand2",
        ).pack(fill="x", padx=8, pady=3)

    def crear_boton(self, padre, texto, comando, ancho=25, borde=False):
        """Botón principal del club (color primario, sin relieve)."""
        return tk.Button(
            padre,
            text=texto,
            command=comando,
            bg=PRIMARIO,
            fg=TEXTO_CLARO,
            font=FUENTE_NEGRITA,
            width=ancho,
            relief="solid" if borde else "flat",
            bd=1 if borde else 0,
            cursor="hand2",
        )

    # ── Pantallas de entrada ───────────────────────────────────

    def mostrar_bienvenida(self):
        self.limpiar_contenido()
        self.ocultar_menu()

        if self._logo is not None:
            tk.Label(self.contenido, image=self._logo, bg=PANEL).pack(pady=(40, 10))

        tk.Label(
            self.contenido,
            text=NOMBRE_CLUB,
            font=FUENTE_GRANDE,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(65 if self._logo is None else 10, 10))

        tk.Label(
            self.contenido,
            text=f"CLUB {NOMBRE_CLUB}",
            font=FUENTE_SUBTITULO,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=5)

        tk.Label(
            self.contenido,
            text=SUBTITULO,
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=5)

        tk.Label(
            self.contenido,
            text=ETIQUETA,
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=10)

        self.crear_boton(
            self.contenido,
            "INICIAR SESIÓN",
            self.mostrar_login,
            ancho=25,
        ).pack(pady=(30, 10))

        boton_salir = self.crear_boton(
            self.contenido,
            "SALIR",
            self.salir,
            ancho=25,
            borde=True,
        )
        boton_salir.config(bg=PANEL, fg=PRIMARIO)
        boton_salir.pack(pady=5)

    def mostrar_login(self):
        self.limpiar_contenido()
        self.ocultar_menu()
        VentanaLogin(self.contenido, self)

    # ── Transiciones de sesión ─────────────────────────────────

    def iniciar_sesion(self, socio):
        """Guarda el socio autenticado y abre su panel según el rol."""
        self.limpiar_contenido()
        self.socio_actual = socio
        if socio.es_admin():
            self.panel = PanelAdmin(self, socio)
        else:
            self.panel = PanelSocio(self, socio)
        self.mostrar_menu(self.panel)
        self.panel.mostrar_inicio()

    def cerrar_sesion(self):
        self.socio_actual = None
        self.panel = None
        self.mostrar_bienvenida()

    def salir(self):
        self.destroy()