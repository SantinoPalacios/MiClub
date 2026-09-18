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

from datetime import date
from pathlib import Path
from base_datos.base_datoss import conectar, crear_tablas, guardar_socio, guardar_cuota
from modelo.socio import Socio
from modelo.cuota import Cuota



RUTA = Path(__file__).parent / "club.db"

# Conectar y crear tablas
conexion = conectar(str(RUTA))
crear_tablas(conexion)

# Crear y guardar un socio
# carlos = Socio(
#     "Carlos Ramos ", 30, "DNI", "40322345", "Argentina",
#     date(2026, 1, 1), "Activo", "carlos", "clave123", "socio"
# )
# guardar_socio(conexion, carlos)
# print("Socio guardado.")

valentino = Socio(
    "Valentino ", 25, "DNI", "20234507", "Argentina",
    date(2025, 2, 3), "Activo", "valentino", "hola456", "socio"
)
guardar_socio(conexion, valentino)
print("Socio guardado.")

cuota1 = Cuota(
    "pendiente",date(2022,9,22),"22 días"
)
guardar_cuota(conexion, cuota1)
print("Cuota registrada.")


conexion.close()