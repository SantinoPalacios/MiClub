import sqlite3
from datetime import date
from modelo.cuota import Cuota


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