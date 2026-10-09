import sqlite3
from datetime import date
from modelo.cuota import Cuota
from modelo.actividad import Actividad


def conectar(ruta):
    """Abre una conexión a la base de datos en la ruta indicada.
    Si el archivo no existe, lo crea automáticamente."""
    conexion = sqlite3.connect(ruta)
    return conexion


def crear_tablas(conexion):
    """Crea las tablas necesarias si no existen."""
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo     TEXT NOT NULL,
            edad                INTEGER,
            tipo_identificacion TEXT,
            identificacion      TEXT,
            nacionalidad        TEXT,
            fecha_inscripcion   TEXT,
            estado              TEXT DEFAULT 'Activo',
            rol                 TEXT DEFAULT 'socio',
            usuario             TEXT UNIQUE NOT NULL,
            contrasenia         TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cuotas (
            id_cuota          INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_vencimiento TEXT,
            periodo           TEXT,
            estado            TEXT DEFAULT 'Pendiente',
            socio_id          INTEGER NOT NULL,
            FOREIGN KEY (socio_id) REFERENCES socios(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubes(
            id_club           INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre            TEXT,
            descripcion        TEXT,
            ubicacion         TEXT,
            presidente        TEXT,
            fecha_fundacion   TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS actividades(
            id_actividad      INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre            TEXT,
            dia               TEXT,
            horario           TEXT,
            club_id           INTEGER,
            FOREIGN KEY (club_id) REFERENCES clubes(id_club)
        )       
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socio_actividad (
            socio_id     INTEGER,
            actividad_id INTEGER,
            PRIMARY KEY (socio_id, actividad_id),
            FOREIGN KEY (socio_id) REFERENCES socios(id),
            FOREIGN KEY (actividad_id) REFERENCES actividades(id_actividad)
        )
    """)
    conexion.commit()


def guardar_socio(conexion, socio):
    """Recibe un objeto Socio y lo guarda en la tabla socios."""
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO socios (nombre_completo, edad, tipo_identificacion,
                            identificacion, nacionalidad, fecha_inscripcion,
                            estado, rol, usuario, contrasenia)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        socio.nombre_completo,
        socio.edad,
        socio.get_tipo_identificacion(),
        socio.get_identificacion(),
        socio.get_nacionalidad(),
        socio.fecha_inscripcion.isoformat(),
        socio.estado_cuota,
        socio.rol,
        socio.get_usuario(),
        socio.get_contrasenia(),
    ))
    conexion.commit()


def buscar_socio_por_usuario(conexion, usuario):
    """Devuelve el objeto Socio con ese usuario, o None si no existe."""
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, nombre_completo, edad, tipo_identificacion, identificacion,
            nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia
        FROM socios
        WHERE usuario = ?
    """, (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return None

    (_id, nombre_completo, edad, tipo_identificacion, identificacion,
    nacionalidad, fecha_inscripcion, estado, rol, usuario, contrasenia) = fila

    from modelo.socio import Socio
    return Socio(
        nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,
        date.fromisoformat(fecha_inscripcion), estado, usuario, contrasenia, rol
    )


def guardar_cuota(conexion, usuario, cuota):
    """Guarda una cuota asociada al socio con ese nombre de usuario."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        raise ValueError("El socio no existe")
    socio_id = fila[0]

    cursor.execute("""
        INSERT INTO cuotas (fecha_vencimiento, periodo, estado, socio_id)
        VALUES (?, ?, ?, ?)
    """, (
        cuota.fecha_vencimiento.isoformat(),
        cuota.periodo,
        cuota.get_estado(),
        socio_id,
    ))
    conexion.commit()


def listar_cuotas_de_socio(conexion, usuario):
    """Devuelve una lista de objetos Cuota del socio indicado."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return []
    socio_id = fila[0]

    cursor.execute(
        "SELECT periodo, estado, fecha_vencimiento FROM cuotas WHERE socio_id = ?",
        (socio_id,)
    )
    cuotas = []
    for periodo, estado, fecha_vencimiento in cursor.fetchall():
        cuota = Cuota(estado, date.fromisoformat(fecha_vencimiento), periodo)
        cuotas.append(cuota)
    return cuotas

def guardar_club(conexion, club):
    """Guarda el club en la tabla clubes (solo si no existe uno)."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id_club FROM clubes WHERE nombre = ?", (club.nombre,))
    fila = cursor.fetchone()
    if fila is not None:
        return fila[0]
    cursor.execute("""
        INSERT INTO clubes (nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        VALUES (?, ?, ?, ?, ?)
    """, (
        club.nombre,
        club.descripcion,
        club.ubicacion,
        club.get_presidente(),
        club.get_fecha_fundacion().isoformat()
    ))
    conexion.commit()

def guardar_actividad(conexion, actividad):
    """Guarda la actividad en la tabla actividades."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id_actividad FROM actividades WHERE nombre = ?", (actividad.nombre,))
    fila = cursor.fetchone()
    if fila is not None:
        return fila[0]
    cursor.execute("""
        INSERT INTO actividades (nombre, dia, horario, club_id)
        VALUES (?, ?, ?, ?)
    """, (
        actividad.nombre,
        actividad.dia,
        actividad.horario,
        actividad.club_id
    ))
    conexion.commit()

def anotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Anota al socio en la actividad indicada."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("SELECT id_actividad FROM actividades WHERE nombre = ?", (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre_actividad} no existe."
    actividad_id = fila[0]

    cursor.execute(
        "INSERT OR IGNORE INTO socio_actividad (socio_id, actividad_id) VALUES (?, ?)",
        (socio_id, actividad_id)
    )
    conexion.commit()
    return f"Te anotaste en {nombre_actividad}."

def desanotar_socio_actividad(conexion, usuario, nombre_actividad):
    """Desanota al socio en la actividad indicada."""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM socios WHERE usuario = ?", (usuario,))
    fila = cursor.fetchone()
    if fila is None:
        return "El socio no existe."
    socio_id = fila[0]

    cursor.execute("SELECT id_actividad FROM actividades WHERE nombre = ?", (nombre_actividad,))
    fila = cursor.fetchone()
    if fila is None:
        return f"La actividad {nombre_actividad} no existe."
    actividad_id = fila[0]

    cursor.execute(
        "DELETE FROM socio_actividad WHERE socio_id = ? AND actividad_id = ?",
        (socio_id, actividad_id)
    )
    conexion.commit()
    return f"Te desanotaste de {nombre_actividad}."


def listar_actividades_de_socio(conexion, usuario):
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id FROM socios WHERE usuario = ?",
        (usuario,)
    )
    fila = cursor.fetchone()

    if fila is None:
        return []

    socio_id = fila[0]

    cursor.execute("""
        SELECT actividades.nombre,
        actividades.dia,
        actividades.horario,
        actividades.club_id
        FROM actividades
        INNER JOIN socio_actividad
        ON actividades.id_actividad = socio_actividad.actividad_id
        WHERE socio_actividad.socio_id = ?
    """, (socio_id,))

    actividades = []

    # Crear un objeto Actividad con sus cuatro atributos
    for nombre, dia, horario, club_id in cursor.fetchall():
        actividad = Actividad(nombre, dia, horario, club_id)
        actividades.append(actividad)

    return actividades

def obtener_club(conexion):
    """Devuelve el objeto Club o None si no hay club cargado."""
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT nombre, descripcion, ubicacion, presidente, fecha_fundacion
        FROM clubes
        LIMIT 1
    """)
    fila = cursor.fetchone()
    if fila is None:
        return None
    nombre, descripcion, ubicacion, presidente, fecha_fundacion = fila
    from modelo.club import Club
    fecha_fundacion = date.fromisoformat(fecha_fundacion)
    return Club(nombre, descripcion, ubicacion, presidente, fecha_fundacion)