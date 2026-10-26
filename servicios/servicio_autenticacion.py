from base_datos.base_datoss import conectar, buscar_socio_por_usuario
from pathlib import Path

RUTA_DB = Path(__file__).parent.parent / "club.db"


def autenticar(usuario, contrasenia):
    conexion = conectar(str(RUTA_DB))

    socio = buscar_socio_por_usuario(conexion, usuario)

    conexion.close()

    if socio is None:
        return None

    if socio.get_contrasenia() == contrasenia:
        return socio

    return None