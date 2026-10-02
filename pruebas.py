# from modelo.persona import Persona

# mipersona = Persona("Micaela", 16, "DNI", "12345678", "Argentina")

# print(mipersona.mostrar_datos())
# print(mipersona.verificar_edad())
# print(mipersona.verificar_identificacion())

# from modelo.socio import Socio

# misocio = Socio("Juan Perez", 25, "DNI", "12345678", "Argentina", "1/10/2021", "activo", "juanin", "elmascapo456", "admin")

# print(misocio.mostrar_datos())
# print(misocio.asociar_club("Boca Juniors"))
# print (misocio.asociar_club("River Plate"))
# print (misocio.dejar_club("Boca Juniors"))
# print (misocio.dejar_club("Racing Club"))
# print (misocio.generar_cuota("01/06/2026", 5000))
# print (misocio.generar_cuota("02/07/2026", 5000))
# print (misocio.generar_cuota("03/08/2026", 5500))
# print (misocio.tiene_deudas())
# print (misocio.cantidad_cuotas_pendientes())
# print (misocio.pagar_cuota("02/07/2026"))
# print (misocio.tiene_deudas())
# print (misocio.cantidad_cuotas_pendientes())
# print (misocio.suspender_socio())
# print (misocio.reactivar_socio())
# print (misocio.actualizar_contrasenia("elmascapo456", "hola123"))
# print (misocio.verificar_acceso("fede", "kiwi345"))
# print (misocio.verificar_acceso("juanin", "kiwi345"))
# print (misocio.verificar_acceso("fede", "hola123"))
# print (misocio.verificar_acceso("juanin", "hola123"))
# print(misocio.es_admin())

# from modelo.actividad import Actividad

# futbol = Actividad("Fútbol juvenil", "Martes y Jueves", "17:00 a 18:30")
# print(futbol.mostrarInfo())

# from modelo.cuota import Cuota

# micuota = Cuota("pagada", "20/05/2025", "40 días")

# print(micuota.mostrar_datos())
# print("Verificación:", micuota.verificar_vencimiento())
# print(micuota.dias_para_vencer())
# print(micuota.registrar_cuota_pagada())
# print(micuota.mostrar_datos())
# print(micuota.actualizar_estado())
# print(micuota.mostrar_datos())
# print(micuota.renovar_cuota("Junio 2025", "20/06/2025"))
# print(micuota.mostrar_datos())

# from modelo.club import Club
# from datetime import date

# miclub = Club("River Plate", "Millonario", "Buenos Aires", "Jorge Brito", date(1901, 5, 25))

# print(miclub.cambiar_presidente("Stéfano Di Carlo"))
# print("Antigüedad:", miclub.mostrar_antiguedad(), "años")
# print(miclub.mostrar_info())
# print(miclub.mensaje_historico())

"""Prueba de la capa de base de datos."""
from datetime import date
from pathlib import Path
from base_datos.base_datoss import (conectar, crear_tablas, guardar_socio, guardar_cuota, listar_cuotas_de_socio
)
from modelo.socio import Socio
from modelo.cuota import Cuota

RUTA = Path(__file__).parent / "club.db"

# Empezar desde cero en cada corrida
if RUTA.exists():
    RUTA.unlink() # borra club.db antes de empezar, así cada corrida arranca con la base vacía

conexion = conectar(str(RUTA))
crear_tablas(conexion)

# Dos socios
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

# Tres cuotas
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

conexion.close()