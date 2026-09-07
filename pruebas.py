# from modelo.persona import Persona

# mipersona = Persona("Micaela", 16, "DNI", "12345678", "Argentina")

# print(mipersona.mostrar_datos())
# print(mipersona.verificar_edad())
# print(mipersona.verificar_identificacion())

# from modelo.socio import Socio

# misocio = Socio("Juan Perez", 25, "DNI", "12345678", "Argentina", "1/10/2021", "activo", "juanin", "elmascapo456", "admin")

# print(misocio.mostrar_datos())
# print(misocio.asociar_club("Boca Juniors"))
# misocio.asociar_club("River Plate")
# misocio.dejar_club("Boca Juniors")
# misocio.dejar_club("Racing Club")
# misocio.generar_cuota("01/06/2026", 5000)
# misocio.generar_cuota("02/07/2026", 5000)
# misocio.generar_cuota("03/08/2026", 5500)
# misocio.tiene_deudas()
# misocio.cantidad_cuotas_pendientes()
# misocio.pagar_cuota("02/07/2026")
# misocio.tiene_deudas()
# misocio.cantidad_cuotas_pendientes()
# misocio.suspender_socio()
# misocio.reactivar_socio()
# misocio.actualizar_contrasenia("elmascapo456", "hola123")
# misocio.verificar_acceso("fede", "kiwi345")
# misocio.verificar_acceso("juanin", "kiwi345")
# misocio.verificar_acceso("fede", "hola123")
# misocio.verificar_acceso("juanin", "hola123")
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

from modelo.club import Club
from datetime import date

miclub = Club("River Plate", "Millonario", "Buenos Aires", "Jorge Brito", date(1901, 5, 25))

print(miclub.cambiar_presidente("Stéfano Di Carlo"))
print("Antigüedad:", miclub.mostrar_antiguedad(), "años")
print(miclub.mostrar_info())
print(miclub.mensaje_historico())