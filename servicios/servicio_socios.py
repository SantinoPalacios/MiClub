from datetime import date
from pathlib import Path

from base_datos.base_datoss import (
    buscar_socio_por_usuario,
    conectar,
    guardar_socio,
    listar_clubes_de_socio as listar_clubes_en_bd,
    listar_socio
)
from modelo.socio import Socio

RUTA_DB = Path(__file__).parent.parent / "club.db"


def listar_socios():
    """Devuelve una lista con todos los socios."""
    conexion = conectar(str(RUTA_DB))
    try:
        return listar_socio(conexion)
    finally:
        conexion.close()


def listar_clubes_de_socio(usuario):
    """Devuelve una lista de los clubes del socio."""
    conexion = conectar(str(RUTA_DB))
    try:
        return listar_clubes_en_bd(conexion, usuario)
    finally:
        conexion.close()


def registrar_socio(nombre, edad, tipo_identificacion, identificacion, nacionalidad, usuario, contrasenia):
    """Valida los datos y registra un nuevo socio."""

    # Limpiar los campos de texto
    nombre = nombre.strip()
    usuario = usuario.strip()
    identificacion = identificacion.strip()

    # Validación campos obligatorios
    if not nombre or not usuario or not contrasenia or not identificacion:
        raise ValueError("Completá todos los campos obligatorios.")

    # Validación de edad
    try:
        edad = int(edad)
    except (TypeError, ValueError):
        raise ValueError("La edad debe ser un número entero.")

    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    socio = Socio(nombre,edad,(tipo_identificacion or "").strip() or None, 
    identificacion,(nacionalidad or "").strip() or None,date.today(),"Activo",usuario,contrasenia,"socio"
    )

    # Verificar identificación
    if not socio.verificar_identificacion():
        raise ValueError("La identificación no puede estar vacía.")

    conexion = conectar(str(RUTA_DB))
    try:
        guardar_socio(conexion, socio)
    finally:
        conexion.close()

    return socio