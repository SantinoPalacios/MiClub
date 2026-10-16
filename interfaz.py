import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
from pathlib import Path
from base_datos.base_datoss import conectar, crear_tablas, guardar_socio, listar_cuotas_de_socio, listar_actividades_de_socio
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

def mostrar_inicio():
    limpiar_contenido()
    tk.Label(
        contenido,
        text="CLUB ATLÉTICO RIVER PLATE",
        font=("Arial", 24, "bold"),
        bg=BLANCO,
        fg=ROJO
    ).pack(pady=(70, 15))

    tk.Label(
        contenido,
        text="Sistema de gestión del club",
        font=("Arial", 16),
        bg=BLANCO,
        fg=TEXTO
    ).pack(pady=5)

    tk.Label(
        contenido,
        text="Socios | Actividades | Cuotas",
        font=("Arial", 12),
        bg=BLANCO,
        fg=TEXTO
    ).pack(pady=10)

def mostrar_socios():
    limpiar_contenido()
    
    tk.Label(
        contenido,
        text="REGISTRO DE NUEVO SOCIO",
        font=("Arial", 20, "bold"),
        bg=BLANCO,
        fg=ROJO
    ).pack(pady=(15, 20))

    form_frame = tk.Frame(contenido, bg=BLANCO)
    form_frame.pack(pady=5, padx=20)

    campos = {}

    estructura_campos = [
        ("Nombre Completo *:", "nombre", 0, 0),
        ("Edad:", "edad", 0, 1),
        ("Tipo Identificación:", "tipo_id", 1, 0),
        ("Número Identificación:", "id_num", 1, 1),
        ("Nacionalidad:", "nacionalidad", 2, 0),
        ("Usuario único *:", "usuario", 3, 0),
        ("Contraseña *:", "contrasenia", 3, 1)
    ]

    for label_text, key, row, col in estructura_campos:
        campo_frame = tk.Frame(form_frame, bg=BLANCO)
        campo_frame.grid(row=row, column=col, padx=15, pady=8, sticky="w")

        tk.Label(campo_frame, text=label_text, font=("Arial", 10, "bold"), bg=BLANCO, fg=TEXTO).pack(anchor="w")
        
        show_char = "*" if key == "contrasenia" else ""
        entry = tk.Entry(campo_frame, font=("Arial", 11), width=25, show=show_char, highlightthickness=1, highlightbackground="#CCCCCC")
        entry.pack(pady=3)
        campos[key] = entry

    def procesar_guardado():
        nombre = campos["nombre"].get().strip()
        edad_str = campos["edad"].get().strip()
        tipo_id = campos["tipo_id"].get().strip()
        identificacion = campos["id_num"].get().strip()
        nacionalidad = campos["nacionalidad"].get().strip()
        usuario = campos["usuario"].get().strip()
        contrasenia = campos["contrasenia"].get().strip()

        if not (nombre and usuario and contrasenia):
            messagebox.showerror("Error", "Nombre, Usuario y Contraseña son campos obligatorios.")
            return

        try:
            edad = int(edad_str) if edad_str else 0
            
            nuevo_socio = Socio(
                nombre_completo=nombre, edad=edad, tipo_identificacion=tipo_id,
                identificacion=identificacion, nacionalidad=nacionalidad,
                fecha_inscripcion=date.today(), estado_cuota="Activo",
                usuario=usuario, contrasenia=contrasenia, rol="socio"
            )

            guardar_socio(conexion_db, nuevo_socio)
            messagebox.showinfo("Éxito", f"¡Socio '{nombre}' registrado correctamente!")
            mostrar_socios()
            
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número válido.")
        except Exception as e:
            messagebox.showerror("Error en BD", f"No se pudo guardar el socio: {e}")

    tk.Button(
        contenido, text="Guardar Socio en BD", command=procesar_guardado,
        bg=ROJO, fg=BLANCO, font=("Arial", 12, "bold"), width=25, cursor="hand2"
    ).pack(pady=25)

def mostrar_actividades():
    limpiar_contenido()
    tk.Label(contenido, text="ACTIVIDADES DEL CLUB", font=("Arial", 20, "bold"), bg=BLANCO, fg=ROJO).pack(pady=15)
    
    # Buscador rápido por usuario
    buscar_frame = tk.Frame(contenido, bg=BLANCO)
    buscar_frame.pack(pady=10)
    
    tk.Label(buscar_frame, text="Buscar por usuario de socio:", font=("Arial", 11), bg=BLANCO).pack(side="left", padx=5)
    entry_usuario = tk.Entry(buscar_frame, font=("Arial", 11), width=15)
    entry_usuario.pack(side="left", padx=5)

    # Tabla visual para mostrar las actividades
    tabla = ttk.Treeview(contenido, columns=("Nombre", "Día", "Horario"), show="headings", height=8)
    tabla.heading("Nombre", text="Actividad")
    tabla.heading("Día", text="Día")
    tabla.heading("Horario", text="Horario")
    tabla.pack(pady=15, fill="both", expand=True, padx=20)

    def buscar_actividades():
        # Limpiar filas anteriores de la tabla
        for fila in tabla.get_children():
            tabla.delete(fila)
            
        usuario = entry_usuario.get().strip()
        if not usuario:
            messagebox.showwarning("Atención", "Por favor, ingresá un usuario de socio (ej: carlos, uma, ana).")
            return
            
        lista = listar_actividades_de_socio(conexion_db, usuario)
        if not lista:
            messagebox.showinfo("Información", f"El socio '{usuario}' no está anotado en ninguna actividad.")
            return
            
        for act in lista:
            # Insertamos la información directo en las columnas de la pantalla
            tabla.insert("", "end", values=(act.nombre, act.dia, act.horario))

    tk.Button(
        buscar_frame, text="Ver Actividades", command=buscar_actividades,
        bg=ROJO, fg=BLANCO, font=("Arial", 10, "bold")
    ).pack(side="left", padx=10)

def mostrar_cuotas():
    limpiar_contenido()
    tk.Label(contenido, text="GESTIÓN DE CUOTAS", font=("Arial", 20, "bold"), bg=BLANCO, fg=ROJO).pack(pady=15)
    
    # Buscador rápido por usuario
    buscar_frame = tk.Frame(contenido, bg=BLANCO)
    buscar_frame.pack(pady=10)
    
    tk.Label(buscar_frame, text="Buscar por usuario de socio:", font=("Arial", 11), bg=BLANCO).pack(side="left", padx=5)
    entry_usuario = tk.Entry(buscar_frame, font=("Arial", 11), width=15)
    entry_usuario.pack(side="left", padx=5)

    # Tabla visual para mostrar las cuotas
    tabla = ttk.Treeview(contenido, columns=("Periodo", "Estado", "Vencimiento"), show="headings", height=8)
    tabla.heading("Periodo", text="Período")
    tabla.heading("Estado", text="Estado de Pago")
    tabla.heading("Vencimiento", text="Fecha Vencimiento")
    tabla.pack(pady=15, fill="both", expand=True, padx=20)

    def buscar_cuotas():
        for fila in tabla.get_children():
            tabla.delete(fila)
            
        usuario = entry_usuario.get().strip()
        if not usuario:
            messagebox.showwarning("Atención", "Por favor, ingresá un usuario de socio.")
            return
            
        lista = listar_cuotas_de_socio(conexion_db, usuario)
        if not lista:
            messagebox.showinfo("Información", f"No se encontraron cuotas para el usuario '{usuario}'.")
            return
            
        for cuota in lista:
            tabla.insert("", "end", values=(cuota.periodo, cuota.get_estado(), cuota.fecha_vencimiento.strftime('%d/%m/%Y')))

    tk.Button(
        buscar_frame, text="Ver Cuotas", command=buscar_cuotas,
        bg=ROJO, fg=BLANCO, font=("Arial", 10, "bold")
    ).pack(side="left", padx=10)

def limpiar_contenido():
    for elemento in contenido.winfo_children():
        elemento.destroy()

def salir():
    try:
        conexion_db.close()
    except:
        pass
    root.destroy()

encabezado = tk.Frame(root, bg=ROJO, height=85)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)

tk.Label(encabezado, text="RIVER PLATE", font=("Arial", 24, "bold"), bg=ROJO, fg=BLANCO).pack(side="left", padx=25, pady=15)
tk.Label(encabezado, text="SISTEMA DEL CLUB", font=("Arial", 12, "bold"), bg=ROJO, fg=BLANCO).pack(side="right", padx=25)

principal = tk.Frame(root, bg=GRIS)
principal.pack(fill="both", expand=True)

menu = tk.Frame(principal, bg=BLANCO, width=210)
menu.pack(side="left", fill="y")
menu.pack_propagate(False)

tk.Label(menu, text="MENÚ PRINCIPAL", font=("Arial", 13, "bold"), bg=BLANCO, fg=ROJO).pack(pady=(25, 15))

def crear_boton(texto, funcion):
    tk.Button(
        menu, text=texto, command=funcion, font=("Arial", 11), bg=BLANCO, fg=TEXTO,
        activebackground=ROJO, activeforeground=BLANCO, relief="flat", anchor="w", padx=20, pady=12
    ).pack(fill="x", padx=8, pady=3)

crear_boton("Inicio", mostrar_inicio)
crear_boton("Socios", mostrar_socios)
crear_boton("Actividades", mostrar_actividades)
crear_boton("Cuotas", mostrar_cuotas)
crear_boton("Salir", salir)

contenido = tk.Frame(principal, bg=BLANCO)
contenido.pack(side="right", fill="both", expand=True, padx=12, pady=12)

mostrar_inicio()
root.mainloop()