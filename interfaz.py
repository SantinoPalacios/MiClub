import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
from pathlib import Path
from base_datos.base_datoss import (
    conectar,
    crear_tablas,
    guardar_socio,
    buscar_socio_por_usuario,
    listar_cuotas_de_socio,
    listar_actividades_de_socio
)
from modelo.socio import Socio

ROJO = "#6B0504"
BLANCO = "#F4F4F9"
GRIS = "#F2F2F2"
TEXTO = "#0B0A0A"

RUTA_DB = Path(__file__).parent / "club.db"

conexion_db = conectar(str(RUTA_DB))
crear_tablas(conexion_db)

root = tk.Tk()
root.title("River Plate | Sistema del Club")
root.geometry("950x650")
root.minsize(850, 550)
root.configure(bg=GRIS)

# Guarda el socio que inició sesión.
socio_actual = None

# Funciones

def limpiar_contenido():
    for elemento in contenido.winfo_children():
        elemento.destroy()


def cerrar_aplicacion():
    try:
        conexion_db.close()
    finally:
        root.destroy()


def crear_titulo(texto):
    tk.Label(
        contenido,
        text=texto,
        font=("Arial", 20, "bold"),
        bg=BLANCO,
        fg=ROJO
    ).pack(pady=(20, 15))


def crear_boton_padre(texto, funcion):
    tk.Button(
        menu,
        text=texto,
        command=funcion,
        font=("Arial", 11),
        bg=BLANCO,
        fg=TEXTO,
        activebackground=ROJO,
        activeforeground=BLANCO,
        relief="flat",
        anchor="w",
        padx=20,
        pady=12,
        cursor="hand2"
    ).pack(fill="x", padx=8, pady=3)


def mostrar_menu():
    # Oculta la pantalla de acceso.
    contenido.pack_forget()

    # Muestra el contenido a la derecha.
    contenido.pack(
        side="right",
        fill="both",
        expand=True,
        padx=12,
        pady=12
    )


def ocultar_menu():
    menu.pack_forget()
    contenido.pack_forget()

    contenido.pack(
        fill="both",
        expand=True
    )


# Pantalla Inicial

def mostrar_bienvenida():
    limpiar_contenido()
    ocultar_menu()

    tk.Label(
        contenido,
        text="RIVER PLATE",
        font=("Arial", 32, "bold"),
        bg=BLANCO,
        fg=ROJO
    ).pack(pady=(65, 10))

    tk.Label(
        contenido,
        text="CLUB ATLÉTICO RIVER PLATE",
        font=("Arial", 18, "bold"),
        bg=BLANCO,
        fg=TEXTO
    ).pack(pady=5)

    tk.Label(
        contenido,
        text="Sistema de gestión del club",
        font=("Arial", 12),
        bg=BLANCO,
        fg=TEXTO
    ).pack(pady=5)

    tk.Label(
        contenido,
        text="Socios | Actividades | Cuotas",
        font=("Arial", 11),
        bg=BLANCO,
        fg=TEXTO
    ).pack(pady=10)

    tk.Button(
        contenido,
        text="INICIAR SESIÓN",
        command=mostrar_login,
        bg=ROJO,
        fg=BLANCO,
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="flat",
        cursor="hand2"
    ).pack(pady=(30, 10))

    tk.Button(
        contenido,
        text="REGISTRAR CUENTA",
        command=mostrar_registro,
        bg=BLANCO,
        fg=ROJO,
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        relief="solid",
        bd=1, #borde fino.
        cursor="hand2"
    ).pack(pady=5)


# ==================================================
# REGISTRO DE CUENTA Y SOCIO
# ==================================================

def mostrar_registro():  # Muestra el formulario para registrar un socio.
    limpiar_contenido()  # Limpia los elementos de la pantalla.
    ocultar_menu()  # Oculta el menú lateral.
    crear_titulo("REGISTRAR NUEVO SOCIO")  # Muestra el título.

    tk.Label(contenido, text="Los campos marcados con * son obligatorios.", font=("Arial", 10), bg=BLANCO, fg=TEXTO).pack()  # Explica los campos obligatorios.

    formulario = tk.Frame(contenido, bg=BLANCO)  # Crea el contenedor del formulario.
    formulario.pack(pady=10)  # Coloca el formulario en la pantalla.

    campos = {}  # Guarda las entradas de texto.

    estructura_campos = [  # Define las etiquetas, claves y posiciones de los campos.
        ("Nombre completo *:", "nombre", 0, 0),
        ("Edad:", "edad", 0, 1),
        ("Tipo de identificación:", "tipo_id", 1, 0),
        ("Número de identificación:", "id_num", 1, 1),
        ("Nacionalidad:", "nacionalidad", 2, 0),
        ("Nombre de usuario *:", "usuario", 2, 1),
        ("Contraseña *:", "contrasenia", 3, 0)
    ]

    for etiqueta, clave, fila, columna in estructura_campos:  # Recorre los campos del formulario.
        campo_frame = tk.Frame(formulario, bg=BLANCO)  # Crea un contenedor para cada campo.
        campo_frame.grid(row=fila, column=columna, padx=12, pady=6, sticky="w")  # Ubica el campo.

        tk.Label(campo_frame, text=etiqueta, font=("Arial", 10, "bold"), bg=BLANCO, fg=TEXTO).pack(anchor="w")  # Muestra la etiqueta.

        if clave == "contrasenia":  # Comprueba si es el campo de contraseña.
            entrada = tk.Entry(campo_frame, font=("Arial", 11), width=22, show="*")  # Crea el campo con la contraseña oculta.
            entrada.pack(side="left", pady=3)  # Coloca el campo.

            boton_ojo = tk.Button(  # Crea el botón para mostrar u ocultar la contraseña.
                campo_frame,
                text="👁",
                bg=BLANCO,
                fg=TEXTO,
                relief="flat",
                cursor="hand2"
            )
            boton_ojo.pack(side="left", padx=5)  # Coloca el botón al lado del campo.

            def alternar_contrasenia(campo=entrada, boton=boton_ojo):  # Alterna la visibilidad de la contraseña.
                if campo.cget("show") == "*":  # Comprueba si está oculta.
                    campo.configure(show="")  # Muestra la contraseña.
                    boton.configure(text="🫣")  # Cambia el símbolo del botón.
                else:  # Si está visible.
                    campo.configure(show="*")  # Oculta la contraseña.
                    boton.configure(text="👁")  # Vuelve a mostrar el ojito.

            boton_ojo.configure(command=alternar_contrasenia)  # Asigna la función al botón.

        else:  # Para los campos que no son contraseñas.
            entrada = tk.Entry(campo_frame, font=("Arial", 11), width=25)  # Crea una entrada normal.
            entrada.pack(pady=3)  # Coloca la entrada debajo de la etiqueta.

        campos[clave] = entrada  # Guarda la entrada para recuperar su contenido.

    def procesar_guardado():  # Comprueba los datos y registra al socio.
        nombre = campos["nombre"].get().strip()  # Obtiene el nombre sin espacios sobrantes.
        edad_texto = campos["edad"].get().strip()  # Obtiene la edad ingresada.
        tipo_id = campos["tipo_id"].get().strip()  # Obtiene el tipo de identificación.
        identificacion = campos["id_num"].get().strip()  # Obtiene el número de identificación.
        nacionalidad = campos["nacionalidad"].get().strip()  # Obtiene la nacionalidad.
        usuario = campos["usuario"].get().strip()  # Obtiene el nombre de usuario.
        contrasenia = campos["contrasenia"].get()  # Obtiene la contraseña.

        if not nombre or not usuario or not contrasenia:  # Comprueba que los campos obligatorios estén completos.
            messagebox.showerror("Campos incompletos", "Completá el nombre, el usuario y la contraseña.")  # Muestra un error.
            return  # Detiene el registro.

        if len(contrasenia) < 6:  # Comprueba que la contraseña tenga al menos seis caracteres.
            messagebox.showwarning("Contraseña débil", "La contraseña debe tener al menos 6 caracteres.")  # Muestra una advertencia.
            return  # Detiene el registro.

        try:  # Intenta validar y guardar los datos.
            edad = int(edad_texto) if edad_texto else 0  # Convierte la edad en un número entero.

            if edad < 0:  # Comprueba que la edad no sea negativa.
                messagebox.showerror("Edad inválida", "La edad no puede ser negativa.")  # Muestra un error.
                return  # Detiene el registro.

            socio_existente = buscar_socio_por_usuario(conexion_db, usuario)  # Busca si el usuario ya existe.

            if socio_existente is not None:  # Comprueba si encontró una cuenta existente.
                messagebox.showerror("Usuario existente", "Ese nombre de usuario ya está registrado.")  # Informa que el usuario está ocupado.
                return  # Detiene el registro.

            nuevo_socio = Socio(  # Crea el objeto con los datos del nuevo socio.
                nombre_completo=nombre,
                edad=edad,
                tipo_identificacion=tipo_id,
                identificacion=identificacion,
                nacionalidad=nacionalidad,
                fecha_inscripcion=date.today(),
                estado_cuota="Activo",
                usuario=usuario,
                contrasenia=contrasenia,
                rol="socio"
            )

            guardar_socio(conexion_db, nuevo_socio)  # Guarda el socio en la base de datos.

            messagebox.showinfo("Registro exitoso", f"La cuenta de {nombre} se creó correctamente.\n\nAhora podés iniciar sesión.")  # Confirma el registro.
            mostrar_login()  # Abre la pantalla de inicio de sesión.

        except ValueError:  # Se ejecuta si la edad no es un número entero válido.
            messagebox.showerror("Edad inválida", "La edad debe ser un número entero.")  # Informa el error.

        except Exception as error:  # Captura otros errores durante el registro.
            messagebox.showerror("Error de registro", f"No se pudo registrar la cuenta:\n{error}")  # Muestra el error.

    tk.Button(contenido, text="CREAR CUENTA", command=procesar_guardado, bg=ROJO, fg=BLANCO, font=("Arial", 11, "bold"), width=22, cursor="hand2").pack(pady=12)  # Crea el botón para registrar la cuenta.
    tk.Button(contenido, text="Volver al inicio", command=mostrar_bienvenida, bg=BLANCO, fg=TEXTO, relief="flat", cursor="hand2").pack()  # Crea el botón para volver.


# ==================================================
# INICIO DE SESIÓN
# ==================================================

def mostrar_login():  # Muestra el formulario de inicio de sesión.
    limpiar_contenido()  # Limpia la pantalla.
    ocultar_menu()  # Oculta el menú lateral.
    crear_titulo("INICIAR SESIÓN")  # Muestra el título.

    tk.Label(contenido, text="Ingresá con tu cuenta de River Plate.", font=("Arial", 11), bg=BLANCO, fg=TEXTO).pack(pady=5)  # Muestra una indicación.

    formulario = tk.Frame(contenido, bg=BLANCO)  # Crea el contenedor del formulario.
    formulario.pack(pady=20)  # Coloca el formulario

        # Contenedor del campo de usuario.
    frame_usuario = tk.Frame(formulario, bg=BLANCO)
    frame_usuario.pack(pady=(5, 15), anchor="w")

# Etiqueta del usuario.
    tk.Label(
        formulario,
        text="Nombre de usuario:",
        font=("Arial", 11, "bold"),
        bg=BLANCO
        ).pack(anchor="w")

# Campo de usuario.
    entrada_usuario = tk.Entry(
    formulario,
    font=("Arial", 12),
    width=27
)
    entrada_usuario.pack(anchor="w", pady=(5, 15))

    tk.Label(formulario, text="Contraseña:", font=("Arial", 11, "bold"), bg=BLANCO).pack(anchor="w")

    # Crea un contenedor para la contraseña y el ojito.
    campo_frame = tk.Frame(formulario, bg=BLANCO)
    campo_frame.pack(pady=5, anchor="w")

    # Crea el campo de contraseña.
    entrada_contrasenia = tk.Entry(campo_frame, font=("Arial", 12), width=27, show="*")
    entrada_contrasenia.pack(side="left")

    # Crea el botón del ojito.
    boton_ojo = tk.Button(
        campo_frame,
        text="👁",
        bg=BLANCO,
        fg=TEXTO,
        relief="flat",
        cursor="hand2"
    )
    boton_ojo.pack(side="left", padx=5)

    # Alterna la visibilidad de la contraseña.
    def alternar_contrasenia(campo=entrada_contrasenia, boton=boton_ojo):
        if campo.cget("show") == "*":
            campo.configure(show="")
            boton.configure(text="🫣")
        else:
            campo.configure(show="*")
            boton.configure(text="👁")

    # Asigna la función al botón.
    boton_ojo.configure(command=alternar_contrasenia)

    def iniciar_sesion():  # Comprueba las credenciales del usuario.
        global socio_actual  # Permite modificar la variable global.

        usuario = entrada_usuario.get().strip()  # Obtiene el usuario ingresado.
        contrasenia = entrada_contrasenia.get()  # Obtiene la contraseña ingresada.

        if not usuario or not contrasenia:  # Comprueba que ambos campos estén completos.
            messagebox.showwarning("Campos incompletos", "Ingresá tu usuario y contraseña.")  # Muestra una advertencia.
            return  # Detiene el inicio de sesión.

        try:  # Intenta buscar y verificar al socio.
            socio = buscar_socio_por_usuario(conexion_db, usuario)  # Busca al socio en la base de datos.

            if socio is None:  # Comprueba si el usuario no existe.
                messagebox.showerror("Error de acceso", "El usuario o la contraseña son incorrectos.")  # Informa el error.
                return  # Detiene el inicio de sesión.

            if socio.get_contrasenia() != contrasenia:  # Comprueba si la contraseña es correcta.
                messagebox.showerror("Error de acceso", "El usuario o la contraseña son incorrectos.")  # Muestra un error.
                return  # Detiene el inicio de sesión.

            socio_actual = socio  # Guarda los datos del socio que inició sesión.
            mostrar_menu()  # Muestra el menú principal.
            mostrar_inicio()  # Muestra la pantalla de bienvenida al socio.

        except Exception as error:  # Captura errores durante el acceso.
            messagebox.showerror("Error", f"No se pudo iniciar sesión:\n{error}")  # Muestra el error.

    tk.Button(contenido, text="INGRESAR", command=iniciar_sesion, bg=ROJO, fg=BLANCO, font=("Arial", 12, "bold"), width=22, height=2, cursor="hand2").pack(pady=10)  # Crea el botón de acceso.
    tk.Button(contenido, text="Registrar una cuenta nueva", command=mostrar_registro, bg=BLANCO, fg=ROJO, relief="flat", cursor="hand2").pack(pady=5)  # Permite abrir el registro.
    tk.Button(contenido, text="Volver", command=mostrar_bienvenida, bg=BLANCO, fg=TEXTO, relief="flat", cursor="hand2").pack(pady=5)  # Permite volver a la bienvenida.


# Inicio De Sistema

def mostrar_inicio():  # Muestra la pantalla principal del socio.
    limpiar_contenido()  # Limpia la pantalla anterior.
    nombre = socio_actual.nombre_completo  # Obtiene el nombre del socio conectado.

    tk.Label(contenido, text="CLUB ATLÉTICO RIVER PLATE", font=("Arial", 24, "bold"), bg=BLANCO, fg=ROJO).pack(pady=(70, 15))  # Muestra el nombre del club.
    tk.Label(contenido, text=f"¡Bienvenido/a, {nombre}!", font=("Arial", 16), bg=BLANCO, fg=TEXTO).pack(pady=5)  # Saluda al socio.
    tk.Label(contenido, text="Sistema de gestión del club", font=("Arial", 12), bg=BLANCO, fg=TEXTO).pack(pady=5)  # Describe el sistema.
    tk.Label(contenido, text="Desde el menú podés consultar socios, actividades y cuotas.", font=("Arial", 11), bg=BLANCO, fg=TEXTO, wraplength=500).pack(pady=15)  # Explica las opciones disponibles.


# Gestión De Socios

def mostrar_socios():  # Muestra el formulario para registrar un socio desde el menú.
    limpiar_contenido()  # Limpia la pantalla.
    crear_titulo("REGISTRO DE NUEVO SOCIO")  # Muestra el título.

    form_frame = tk.Frame(contenido, bg=BLANCO)  # Crea el contenedor del formulario.
    form_frame.pack(pady=5, padx=20)  # Coloca el formulario.

    campos = {}  # Guarda los campos de entrada.

    estructura_campos = [  # Define los campos y sus posiciones.
        ("Nombre completo *:", "nombre", 0, 0),
        ("Edad:", "edad", 0, 1),
        ("Tipo de identificación:", "tipo_id", 1, 0),
        ("Número de identificación:", "id_num", 1, 1),
        ("Nacionalidad:", "nacionalidad", 2, 0),
        ("Usuario único *:", "usuario", 3, 0),
        ("Contraseña *:", "contrasenia", 3, 1)
    ]

    for etiqueta, clave, fila, columna in estructura_campos:  # Recorre los campos definidos.
        campo_frame = tk.Frame(form_frame, bg=BLANCO)  # Crea el contenedor de cada campo.
        campo_frame.grid(row=fila, column=columna, padx=15, pady=8, sticky="w")  # Ubica el campo.

        tk.Label(campo_frame, text=etiqueta, font=("Arial", 10, "bold"), bg=BLANCO, fg=TEXTO).pack(anchor="w")  # Muestra la etiqueta.

        ocultar_contrasenia = "*" if clave == "contrasenia" else ""  # Oculta la contraseña.

        entrada = tk.Entry(campo_frame, font=("Arial", 11), width=25, show=ocultar_contrasenia)  # Crea la entrada.
        entrada.pack(pady=3)  # Coloca la entrada debajo de la etiqueta.
        campos[clave] = entrada  # Guarda la entrada en el diccionario.

    def procesar_guardado():  # Valida y guarda los datos del socio.
        nombre = campos["nombre"].get().strip()  # Obtiene el nombre.
        edad_texto = campos["edad"].get().strip()  # Obtiene la edad.
        tipo_id = campos["tipo_id"].get().strip()  # Obtiene el tipo de identificación.
        identificacion = campos["id_num"].get().strip()  # Obtiene el número de identificación.
        nacionalidad = campos["nacionalidad"].get().strip()  # Obtiene la nacionalidad.
        usuario = campos["usuario"].get().strip()  # Obtiene el usuario.
        contrasenia = campos["contrasenia"].get()  # Obtiene la contraseña.

        if not nombre or not usuario or not contrasenia:  # Comprueba los campos obligatorios.
            messagebox.showerror("Error", "Nombre, usuario y contraseña son obligatorios.")  # Muestra un error.
            return  # Detiene el registro.

        try:  # Intenta validar y guardar los datos.
            edad = int(edad_texto) if edad_texto else 0  # Convierte la edad en entero.

            if edad < 0:  # Comprueba que la edad no sea negativa.
                messagebox.showerror("Error", "La edad no puede ser negativa.")  # Muestra un error.
                return  # Detiene el registro.

            socio_existente = buscar_socio_por_usuario(conexion_db, usuario)  # Busca si el usuario ya está registrado.

            if socio_existente is not None:  # Comprueba si el usuario existe.
                messagebox.showerror("Error", "Ese usuario ya está registrado.")  # Informa que ya existe.
                return  # Detiene el registro.

            nuevo_socio = Socio(  # Crea el objeto del nuevo socio.
                nombre_completo=nombre,
                edad=edad,
                tipo_identificacion=tipo_id,
                identificacion=identificacion,
                nacionalidad=nacionalidad,
                fecha_inscripcion=date.today(),
                estado_cuota="Activo",
                usuario=usuario,
                contrasenia=contrasenia,
                rol="socio"
            )

            guardar_socio(conexion_db, nuevo_socio)  # Guarda el socio en la base de datos.
            messagebox.showinfo("Éxito", f"El socio '{nombre}' se registró correctamente.")  # Confirma el registro.
            mostrar_socios()  # Vuelve a mostrar el formulario.

        except ValueError:  # Se ejecuta si la edad no es un entero válido.
            messagebox.showerror("Error", "La edad debe ser un número entero.")  # Informa el error.

        except Exception as error:  # Captura otros errores.
            messagebox.showerror("Error en la base de datos", f"No se pudo guardar el socio:\n{error}")  # Muestra el error.

    tk.Button(contenido, text="Guardar socio en BD", command=procesar_guardado, bg=ROJO, fg=BLANCO, font=("Arial", 12, "bold"), width=25, cursor="hand2").pack(pady=20)  # Crea el botón para guardar.


# Consulta De Actividades

def mostrar_actividades():  # Muestra las actividades asociadas a un socio.
    limpiar_contenido()  # Limpia la pantalla.
    crear_titulo("ACTIVIDADES DEL CLUB")  # Muestra el título.

    buscar_frame = tk.Frame(contenido, bg=BLANCO)  # Crea el contenedor de búsqueda.
    buscar_frame.pack(pady=10)  # Coloca el contenedor.

    tk.Label(buscar_frame, text="Usuario del socio:", font=("Arial", 11), bg=BLANCO).pack(side="left", padx=5)  # Muestra la etiqueta.
    entry_usuario = tk.Entry(buscar_frame, font=("Arial", 11), width=18)  # Crea el campo para buscar al socio.
    entry_usuario.pack(side="left", padx=5)  # Coloca el campo.

    if socio_actual.rol == "socio":  # Comprueba si inició sesión un socio.
        entry_usuario.insert(0, socio_actual.usuario)  # Completa el usuario automáticamente.
        entry_usuario.configure(state="disabled")  # Impide modificar el usuario.

    tabla = ttk.Treeview(contenido, columns=("Nombre", "Día", "Horario"), show="headings", height=10)  # Crea la tabla de actividades.
    tabla.heading("Nombre", text="Actividad")  # Define el encabezado de actividad.
    tabla.heading("Día", text="Día")  # Define el encabezado del día.
    tabla.heading("Horario", text="Horario")  # Define el encabezado del horario.
    tabla.column("Nombre", width=220)  # Define el ancho de la columna.
    tabla.column("Día", width=130)  # Define el ancho de la columna.
    tabla.column("Horario", width=150)  # Define el ancho de la columna.
    tabla.pack(pady=15, fill="both", expand=True, padx=20)  # Muestra la tabla.

    def buscar_actividades():  # Busca las actividades del usuario.
        for fila in tabla.get_children():  # Recorre las filas de la tabla.
            tabla.delete(fila)  # Elimina cada fila anterior.

        usuario = entry_usuario.get().strip()  # Obtiene el usuario ingresado.

        if not usuario:  # Comprueba que el usuario no esté vacío.
            messagebox.showwarning("Atención", "Ingresá un usuario de socio.")  # Muestra una advertencia.
            return  # Detiene la búsqueda.

        try:  # Intenta consultar las actividades.
            lista = listar_actividades_de_socio(conexion_db, usuario)  # Obtiene las actividades de la base de datos.

            if not lista:  # Comprueba si no hay actividades.
                messagebox.showinfo("Información", f"No hay actividades registradas para '{usuario}'.")  # Informa que no hay resultados.
                return  # Detiene la búsqueda.

            for actividad in lista:  # Recorre las actividades encontradas.
                tabla.insert("", "end", values=(actividad.nombre, actividad.dia, actividad.horario))  # Agrega la actividad a la tabla.

        except Exception as error:  # Captura errores de consulta.
            messagebox.showerror("Error", f"No se pudieron consultar las actividades:\n{error}")  # Muestra el error.

    tk.Button(buscar_frame, text="Ver actividades", command=buscar_actividades, bg=ROJO, fg=BLANCO, font=("Arial", 10, "bold"), cursor="hand2").pack(side="left", padx=10)  # Crea el botón de búsqueda.

    if socio_actual.rol == "socio":  # Comprueba si el usuario es un socio.
        buscar_actividades()  # Busca automáticamente sus actividades.


# Consulta De Cuotas

def mostrar_cuotas():  # Muestra las cuotas del socio.
    limpiar_contenido()  # Limpia la pantalla.
    crear_titulo("GESTIÓN DE CUOTAS")  # Muestra el título.

    buscar_frame = tk.Frame(contenido, bg=BLANCO)  # Crea el contenedor de búsqueda.
    buscar_frame.pack(pady=10)  # Coloca el contenedor.

    tk.Label(buscar_frame, text="Usuario del socio:", font=("Arial", 11), bg=BLANCO).pack(side="left", padx=5)  # Muestra la etiqueta.
    entry_usuario = tk.Entry(buscar_frame, font=("Arial", 11), width=18)  # Crea el campo del usuario.
    entry_usuario.pack(side="left", padx=5)  # Coloca el campo.

    if socio_actual.rol == "socio":  # Comprueba si inició sesión un socio.
        entry_usuario.insert(0, socio_actual.usuario)  # Completa el usuario automáticamente.
        entry_usuario.configure(state="disabled")  # Impide cambiar el usuario.

    tabla = ttk.Treeview(contenido, columns=("Periodo", "Estado", "Vencimiento"), show="headings", height=10)  # Crea la tabla de cuotas.
    tabla.heading("Periodo", text="Período")  # Define el encabezado del período.
    tabla.heading("Estado", text="Estado de pago")  # Define el encabezado del estado.
    tabla.heading("Vencimiento", text="Fecha de vencimiento")  # Define el encabezado de vencimiento.
    tabla.column("Periodo", width=150)  # Define el ancho de la columna.
    tabla.column("Estado", width=150)  # Define el ancho de la columna.
    tabla.column("Vencimiento", width=200)  # Define el ancho de la columna.
    tabla.pack(pady=15, fill="both", expand=True, padx=20)  # Muestra la tabla.

    def buscar_cuotas():  # Busca las cuotas del socio.
        for fila in tabla.get_children():  # Recorre las filas existentes.
            tabla.delete(fila)  # Elimina las filas anteriores.

        usuario = entry_usuario.get().strip()  # Obtiene el usuario ingresado.

        if not usuario:  # Comprueba que el campo no esté vacío.
            messagebox.showwarning("Atención", "Ingresá un usuario de socio.")  # Muestra una advertencia.
            return  # Detiene la búsqueda.

        try:  # Intenta consultar las cuotas.
            lista = listar_cuotas_de_socio(conexion_db, usuario)  # Obtiene las cuotas de la base de datos.

            if not lista:  # Comprueba si no existen cuotas.
                messagebox.showinfo("Información", f"No se encontraron cuotas para '{usuario}'.")  # Informa que no hay cuotas.
                return  # Detiene la búsqueda.

            for cuota in lista:  # Recorre las cuotas encontradas.
                vencimiento = cuota.fecha_vencimiento  # Obtiene la fecha de vencimiento.

                if isinstance(vencimiento, str):  # Comprueba si la fecha es texto.
                    try:
                        vencimiento = date.fromisoformat(vencimiento)  # Convierte el texto en una fecha.
                    except ValueError:
                        pass  # Mantiene el valor original si no puede convertirlo.

                if isinstance(vencimiento, date):  # Comprueba si el vencimiento es una fecha.
                    vencimiento = vencimiento.strftime("%d/%m/%Y")  # Muestra la fecha en formato día/mes/año.

                tabla.insert("", "end", values=(cuota.periodo, cuota.get_estado(), vencimiento))  # Agrega la cuota a la tabla.

        except Exception as error:  # Captura errores durante la consulta.
            messagebox.showerror("Error", f"No se pudieron consultar las cuotas:\n{error}")  # Muestra el error.

    tk.Button(buscar_frame, text="Ver cuotas", command=buscar_cuotas, bg=ROJO, fg=BLANCO, font=("Arial", 10, "bold"), cursor="hand2").pack(side="left", padx=10)  # Crea el botón de búsqueda.

    if socio_actual.rol == "socio":  # Comprueba si inició sesión un socio.
        buscar_cuotas()  # Busca automáticamente sus cuotas.


# Cerrar Seción

def cerrar_sesion():  # Cierra la sesión actual.
    global socio_actual  # Permite modificar la variable global.
    socio_actual = None  # Elimina la referencia al socio conectado.
    mostrar_bienvenida()  # Regresa a la pantalla de bienvenida.


# Encabezado

encabezado = tk.Frame(root, bg=ROJO, height=85)  # Crea el encabezado de la ventana.
encabezado.pack(fill="x")  # Hace que ocupe todo el ancho.
encabezado.pack_propagate(False)  # Mantiene la altura establecida.

tk.Label(encabezado, text="RIVER PLATE", font=("Arial", 24, "bold"), bg=ROJO, fg=BLANCO).pack(side="left", padx=25, pady=15)  # Muestra el nombre del club.
tk.Label(encabezado, text="SISTEMA DEL CLUB", font=("Arial", 12, "bold"), bg=ROJO, fg=BLANCO).pack(side="right", padx=25)  # Muestra el nombre del sistema.


# Contenedor Principal

principal = tk.Frame(root, bg=GRIS)  # Crea el contenedor principal.
principal.pack(fill="both", expand=True)  # Ocupa el espacio restante.

menu = tk.Frame(principal, bg=BLANCO, width=210)  # Crea el menú lateral.
menu.pack_propagate(False)  # Mantiene el ancho del menú.

tk.Label(menu, text="MENÚ PRINCIPAL", font=("Arial", 13, "bold"), bg=BLANCO, fg=ROJO).pack(pady=(25, 15))  # Muestra el título del menú.

crear_boton_padre("Inicio", mostrar_inicio)  # Crea el botón Inicio.
crear_boton_padre("Socios", mostrar_socios)  # Crea el botón Socios.
crear_boton_padre("Actividades", mostrar_actividades)  # Crea el botón Actividades.
crear_boton_padre("Cuotas", mostrar_cuotas)  # Crea el botón Cuotas.
crear_boton_padre("Cerrar sesión", cerrar_sesion)  # Crea el botón para cerrar sesión.


contenido = tk.Frame(principal, bg=BLANCO)

# Mostrar primero la pantalla de bienvenida.
mostrar_bienvenida()

# Cerrar la conexión al cerrar la ventana.
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

root.mainloop()