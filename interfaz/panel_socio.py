import tkinter as tk
from tkinter import messagebox, ttk

from interfaz.tema import (
    ESTADO_ACTIVO,
    ESTADO_PENDIENTE,
    ESTADO_SUSPENDIDO,
    ESTADO_VENCIDO,
    FILA_PAR,
    FUENTE,
    FUENTE_CHICA,
    FUENTE_NEGRITA,
    FUENTE_TITULO,
    PANEL,
    PRIMARIO,
    TEXTO,
)
from servicios.servicio_cuotas import listar_cuotas, pagar_cuota
from servicios.servicio_socios import listar_clubes_de_socio, obtener_socio


class PanelSocio(tk.Frame):
    """Pantallas que ve el socio dentro de la ventana principal."""

    def __init__(self, app, socio):
        super().__init__(app.contenido, bg=PANEL)
        self.app = app
        self.usuario = socio.get_usuario()
        self._periodos = []
        self.pack(fill="both", expand=True)

    def botones_menu(self):
        return [
            ("Inicio", self.mostrar_inicio),
            ("Mis datos", self.mostrar_datos),
            ("Mis clubes", self.mostrar_clubes),
            ("Mis cuotas", self.mostrar_cuotas),
            ("Cerrar sesión", self.app.cerrar_sesion),
        ]

    def _limpiar(self):
        for elemento in self.winfo_children():
            elemento.destroy()

    def _crear_titulo(self, texto):
        tk.Label(
            self,
            text=texto,
            font=FUENTE_TITULO,
            bg=PANEL,
            fg=PRIMARIO,
        ).pack(pady=(15, 10))

    def _etiqueta_estado(self, estado):
        if estado == "Suspendido":
            return ESTADO_SUSPENDIDO
        return ESTADO_ACTIVO

    # ── Pantallas ──────────────────────────────────────────────

    def mostrar_inicio(self):
        self._limpiar()
        socio = obtener_socio(self.usuario)

        if socio is None:
            messagebox.showerror("Error", "El socio ya no existe.")
            self.app.cerrar_sesion()
            return

        self._crear_titulo(f"¡Bienvenido/a, {socio.nombre_completo}!")

        cuotas = listar_cuotas(self.usuario)
        pendientes = [
            cuota for cuota in cuotas if cuota.get_estado() in ("Pendiente", "Vencida")
        ]

        tarjeta = tk.Frame(self, bg=PANEL)
        tarjeta.pack(pady=20)

        self._crear_tarjeta(tarjeta, "Estado", socio.estado,
                            self._etiqueta_estado(socio.estado)).grid(
            row=0, column=0, padx=12)

        self._crear_tarjeta(tarjeta, "Cuotas pendientes", str(len(pendientes)),
                            ESTADO_PENDIENTE).grid(row=0, column=1, padx=12)

        tk.Label(
            self,
            text="Usá el menú para ver tus datos, tus clubes y tus cuotas.",
            font=FUENTE,
            bg=PANEL,
            fg=TEXTO,
        ).pack(pady=15)

    def _crear_tarjeta(self, padre, titulo, valor, color):
        tarjeta = tk.Frame(padre, bg=PANEL, highlightbackground=FILA_PAR,
                        highlightthickness=1)
        tk.Label(
            tarjeta,
            text=str(valor),
            font=("Arial", 26, "bold"),
            bg=PANEL,
            fg=color,
        ).pack(padx=30, pady=(18, 2))
        tk.Label(
            tarjeta,
            text=titulo,
            font=FUENTE_CHICA,
            bg=PANEL,
            fg=TEXTO,
        ).pack(padx=30, pady=(0, 18))
        return tarjeta

    def mostrar_datos(self):
        self._limpiar()
        socio = obtener_socio(self.usuario)

        if socio is None:
            messagebox.showerror("Error", "El socio ya no existe.")
            self.app.cerrar_sesion()
            return

        self._crear_titulo("MIS DATOS")

        tabla = tk.Frame(self, bg=PANEL)
        tabla.pack(pady=10)

        valores = [
            ("Nombre completo", socio.nombre_completo),
            ("Edad", socio.edad),
            ("Identificación",
            f"{socio.get_tipo_identificacion()} {socio.get_identificacion()}"),
            ("Nacionalidad", socio.get_nacionalidad()),
            ("Fecha de inscripción", socio.fecha_inscripcion),
        ]

        for fila, (etiqueta, valor) in enumerate(valores):
            tk.Label(
                tabla,
                text=f"{etiqueta}:",
                font=FUENTE_NEGRITA,
                bg=PANEL,
                fg=TEXTO,
            ).grid(row=fila, column=0, sticky="e", padx=(0, 12), pady=4)

            tk.Label(
                tabla,
                text=valor,
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO,
            ).grid(row=fila, column=1, sticky="w", pady=4)

        tk.Label(
            tabla,
            text="Estado:",
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=TEXTO,
        ).grid(row=len(valores), column=0, sticky="e", padx=(0, 12), pady=4)

        tk.Label(
            tabla,
            text=socio.estado,
            font=FUENTE_NEGRITA,
            bg=PANEL,
            fg=self._etiqueta_estado(socio.estado),
        ).grid(row=len(valores), column=1, sticky="w", pady=4)

    def mostrar_clubes(self):
        self._limpiar()
        self._crear_titulo("MIS CLUBES")

        clubes = listar_clubes_de_socio(self.usuario)

        if not clubes:
            tk.Label(
                self,
                text="Sin clubes asociados",
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO,
            ).pack(pady=25)
            return

        for club in clubes:
            tk.Label(
                self,
                text=f"• {club.informacion()}",
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO,
                anchor="w",
            ).pack(fill="x", padx=60, pady=4)

    def mostrar_cuotas(self):
        self._limpiar()
        self._crear_titulo("MIS CUOTAS")

        columnas = ("periodo", "estado", "vencimiento")
        tabla = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            style="Club.Treeview",
            height=10,
        )
        tabla.heading("periodo", text="Período")
        tabla.heading("estado", text="Estado")
        tabla.heading("vencimiento", text="Fecha de vencimiento")
        tabla.column("periodo", width=170, anchor="center")
        tabla.column("estado", width=150, anchor="center")
        tabla.column("vencimiento", width=200, anchor="center")

        tabla.tag_configure("par", background=FILA_PAR)
        tabla.tag_configure("impar", background=PANEL)
        tabla.tag_configure("Pagada", foreground=ESTADO_ACTIVO)
        tabla.tag_configure("Pendiente", foreground=ESTADO_PENDIENTE)
        tabla.tag_configure("Vencida", foreground=ESTADO_VENCIDO)
        tabla.pack(fill="both", expand=True, padx=40, pady=(5, 10))

        boton_pagar = self.app.crear_boton(
            self,
            "PAGAR CUOTA SELECCIONADA",
            lambda: self._pagar(tabla),
            ancho=25,
        )
        boton_pagar.pack(pady=(0, 5))

        self._cargar_cuotas(tabla, boton_pagar)

    def _cargar_cuotas(self, tabla, boton_pagar):
        for fila in tabla.get_children():
            tabla.delete(fila)
        self._periodos = []

        cuotas = listar_cuotas(self.usuario)

        if not cuotas:
            tk.Label(
                self,
                text="Sin cuotas cargadas",
                font=FUENTE,
                bg=PANEL,
                fg=TEXTO,
            ).pack()
            boton_pagar.configure(state="disabled")
            return

        boton_pagar.configure(state="normal")
        for indice, cuota in enumerate(cuotas):
            rayado = "par" if indice % 2 == 0 else "impar"
            tabla.insert(
                "",
                "end",
                values=(cuota.periodo, cuota.get_estado(), cuota.fecha_vencimiento),
                tags=(rayado, cuota.get_estado()),
            )
            self._periodos.append(cuota.periodo)

    def _pagar(self, tabla):
        seleccion = tabla.selection()
        if not seleccion or not self._periodos:
            messagebox.showwarning("Aviso", "Seleccioná una cuota primero.")
            return

        indice = tabla.index(seleccion[0])
        periodo = self._periodos[indice]

        mensaje = pagar_cuota(self.usuario, periodo)
        messagebox.showinfo("Pagar cuota", mensaje)

        self.mostrar_cuotas()