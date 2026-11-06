from base_datos.base_datoss import (
    conectar, 
    listar_cuotas_de_socio, 
    pagar_cuota as pagar_cuota_bd
)
from pathlib import Path

RUTA_DB = Path(__file__).resolve().parent.parent / "club.db"


def listar_cuotas(usuario):
    """Devuelve las cuotas del socio indicado."""
    conexion = conectar(RUTA_DB)
    cuotas = listar_cuotas_de_socio(conexion, usuario)
    conexion.close()
    return cuotas


def pagar_cuota(usuario, periodo):
    """Paga la cuota del período indicado."""
    conexion = conectar(RUTA_DB)
    mensaje = pagar_cuota_bd(conexion, usuario, periodo)
    conexion.close()
    return mensaje