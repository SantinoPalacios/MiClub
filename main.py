from datetime import date
from pathlib import Path

from base_datos.base_datoss import (
    buscar_socio_por_usuario,
    conectar,
    crear_tablas,
    guardar_socio,
)
from interfaz.app import ClubApp
from modelo.socio import Socio

RUTA_BASE = Path(__file__).parent / "club.db"

USUARIO_ADMIN = "admin"
CONTRASENIA_ADMIN = "admin123"


def crear_admin_inicial():
    """Crea un usuario administrador si la base no tiene ninguno."""
    conexion = conectar(str(RUTA_BASE))
    try:
        if buscar_socio_por_usuario(conexion, USUARIO_ADMIN) is not None:
            return

        guardar_socio(conexion, Socio(
            "Administrador del club", 0, None, None, None,
            date.today(), "Activo", USUARIO_ADMIN, CONTRASENIA_ADMIN, "admin"
        ))
        print(
            f"Admin inicial creado. Usuario: {USUARIO_ADMIN} | "
            f"Contraseña: {CONTRASENIA_ADMIN}"
        )
    finally:
        conexion.close()


def main():
    conexion = conectar(str(RUTA_BASE))
    crear_tablas(conexion)
    conexion.close()

    crear_admin_inicial()

    ClubApp().mainloop()


if __name__ == "__main__":
    main()
