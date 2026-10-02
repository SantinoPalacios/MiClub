"""Prueba de la capa de base de datos."""
from datetime import date
from pathlib import Path
from base_datos.base_datoss import (
    conectar, crear_tablas, guardar_socio, guardar_cuota,
    listar_cuotas_de_socio, buscar_socio_por_usuario
)
from modelo.socio import Socio
from modelo.cuota import Cuota

RUTA = Path(__file__).parent / "club.db"

# Empezar desde cero en cada corrida
if RUTA.exists():
    RUTA.unlink()

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# Tres socios
carlos = Socio("Carlos Ramos", 30, "DNI", "40322345", "Argentina",
            date(2026, 1, 1), "Activo", "carlos", "clave123", "socio")
ana = Socio("Ana Gómez", 28, "DNI", "38111222", "Argentina",
            date(2026, 2, 1), "Activo", "ana", "clave456", "socio")
uma = Socio("Uma Vega", 21, "DNI", "23090567", "Colombia",
            date(2026, 6, 16), "Activo", "uma", "clave557", "socio")
guardar_socio(conexion, carlos)
guardar_socio(conexion, ana)
guardar_socio(conexion, uma)
print("Socios guardados.")

# Cuotas
guardar_cuota(conexion, "carlos", Cuota("pendiente", date(2026, 8, 10), "Agosto"))
guardar_cuota(conexion, "carlos", Cuota("pagada", date(2026, 9, 10), "Septiembre"))
guardar_cuota(conexion, "ana", Cuota("pendiente", date(2026, 8, 10), "Agosto"))
guardar_cuota(conexion, "uma", Cuota("pagada", date(2026, 1, 2), "Octubre"))
print("Cuotas guardadas.")

# Listar las cuotas de cada socio
for usuario in ("carlos", "ana", "uma"):
    print(f"Cuotas de {usuario}:")
    for cuota in listar_cuotas_de_socio(conexion, usuario):
        print("  ", cuota.mostrar_datos())

# Buscar socios por usuario
encontrado = buscar_socio_por_usuario(conexion, "carlos")
print(encontrado.mostrar_datos())

inexistente = buscar_socio_por_usuario(conexion, "nadie")
print(inexistente)   # debería imprimir None

conexion.close()