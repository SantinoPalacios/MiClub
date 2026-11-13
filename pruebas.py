# """Prueba de la capa de base de datos."""
# from datetime import date
# from pathlib import Path
# from base_datos.base_datoss import (
#     conectar, crear_tablas, guardar_socio, guardar_cuota,
#     listar_cuotas_de_socio, buscar_socio_por_usuario, guardar_club, 
#     guardar_actividad, anotar_socio_actividad, desanotar_socio_actividad, 
#     listar_actividades_de_socio, obtener_club, asociar_socio_club
# )
# from modelo.socio import Socio
# from modelo.cuota import Cuota
# from modelo.actividad import Actividad
# from modelo.club import Club
# from servicios import servicio_autenticacion
# from servicios.servicio_autenticacion import (autenticar)

# RUTA = Path(__file__).parent / "club.db"

# # Empezar desde cero en cada corrida
# if RUTA.exists():
#     RUTA.unlink()

# conexion = conectar(str(RUTA))
# crear_tablas(conexion)

# brenda= Socio("Brenda Giselle Isabella", 26, "DNI", "34567890","Argentina",date(2026, 10, 26),"activo","brendu","racingclub","socio")
# guardar_socio(conexion, brenda)
# socio = autenticar("brendu", "racingclub")


# # Ejemplos de Autenticación Fallida
# # socio = autenticar("brendu", "riverplate")
# # socio = autenticar("brendo", "racingclub")
# # socio = autenticar("brendo", "riverplate")

# if socio is None:
#     print("El socio no existe o los datos son incorrectos.")
# else:
#     print("Nombre:", socio.nombre_completo)
#     print("Usuario:", socio.get_usuario())
#     print("Rol:", socio.rol)
#     print ("Socia guardada.")


# conexion.close()


# # # Tres socios
# # carlos = Socio("Carlos Ramos", 30, "DNI", "40322345", "Argentina",
# #             date(2026, 1, 1), "Activo", "carlos", "clave123", "socio")
# # ana = Socio("Ana Gómez", 28, "DNI", "38111222", "Argentina",
# #             date(2026, 2, 1), "Activo", "ana", "clave456", "socio")
# # uma = Socio("Uma Vega", 21, "DNI", "23090567", "Colombia",
# #             date(2026, 6, 16), "Activo", "uma", "clave557", "socio")
# # guardar_socio(conexion, carlos)
# # guardar_socio(conexion, ana)
# # guardar_socio(conexion, uma)
# # print("Socios guardados.")

# # # Cuotas
# # guardar_cuota(conexion, "carlos", Cuota("pendiente", date(2026, 8, 10), "Agosto"))
# # guardar_cuota(conexion, "carlos", Cuota("pagada", date(2026, 9, 10), "Septiembre"))
# # guardar_cuota(conexion, "ana", Cuota("pendiente", date(2026, 8, 10), "Agosto"))
# # guardar_cuota(conexion, "uma", Cuota("pagada", date(2026, 1, 2), "Octubre"))
# # print("Cuotas guardadas.")

# # # Listar las cuotas de cada socio
# # for usuario in ("carlos", "ana", "uma"):
# #     print(f"Cuotas de {usuario}:")
# #     for cuota in listar_cuotas_de_socio(conexion, usuario):
# #         print("  ", cuota.mostrar_datos())

# # # Buscar socios por usuario
# # encontrado = buscar_socio_por_usuario(conexion, "carlos")
# # print(encontrado.mostrar_datos())

# # inexistente = buscar_socio_por_usuario(conexion, "nadie")
# # print(inexistente)   # debería imprimir None
# # buscar_socio_por_usuario(conexion, "carlos")
# # listar_cuotas_de_socio(conexion, "ana")

# # # Crear y guardar club
# # river_plate = Club("river plate", "el más grande y millonario de rojo y blanco", "Buenos Aires", "Stéfano Di Carlo", date(1901, 5, 25))
# # guardar_club(conexion, river_plate)
# # cursor = conexion.cursor()
# # cursor.execute(
# #     "SELECT id_club FROM clubes WHERE nombre = ?",
# #     ("river plate",)
# # )
# # fila = cursor.fetchone()
# # club_id = fila[0]

# # # Tres actividades
# # basquetball = Actividad("basquetball", "viernes", "7PM", club_id)
# # futbol = Actividad("fútbol", "miércoles", "6PM", club_id)
# # ballet = Actividad("ballet","jueves","5PM", club_id)
# # guardar_actividad(conexion, basquetball)
# # guardar_actividad(conexion, futbol)
# # guardar_actividad(conexion, ballet)

# # # Anotar
# # anotar_socio_actividad(conexion, "uma", "ballet")
# # anotar_socio_actividad(conexion, "uma", "basquetball")
# # anotar_socio_actividad(conexion, "carlos", "fútbol")
# # anotar_socio_actividad(conexion, "carlos", "ballet")
# # anotar_socio_actividad(conexion, "ana" , "basquetball")
# # anotar_socio_actividad(conexion, "ana", "fútbol")

# # # Listar desanotar
# # desanotar_socio_actividad(conexion, "carlos", "fútbol")
# # desanotar_socio_actividad(conexion, "ana", "basquetball")

# # # Listar actividades
# # for usuario in ("uma", "ana", "carlos"):
# #     print(f"Actividades de {usuario}:")

# #     for actividad in listar_actividades_de_socio(conexion, usuario):
# #         print("  ", actividad.mostrarInfo())

# # club = obtener_club(conexion)
# # if club is not None:
# #     print("Nombre:", club.nombre)
# #     print("Descripción:", club.descripcion)
# #     print("Ubicación:", club.ubicacion)
# #     print("Presidente:", club.get_presidente())
# #     print("Fecha de fundación:", club.get_fecha_fundacion())

# # conexion.close()



from base_datos.base_datoss import conectar, crear_tablas
from pathlib import Path
from servicios.servicio_autenticacion import autenticar
from servicios.servicio_cuotas import listar_cuotas, pagar_cuota
from servicios.servicio_socios import (
    listar_clubes_de_socio,
    listar_socios,
    obtener_socio,
    reactivar_socio,
    registrar_socio,
)

RUTA = Path(__file__).parent / "club.db"


def preparar_base():
    if RUTA.exists():
        RUTA.unlink()
    conexion = conectar(str(RUTA))
    crear_tablas(conexion)
    conexion.close()


def main():
    preparar_base()
    print("Base de prueba creada.\n")

    socio = autenticar("isaias", "clave123")
    assert socio is not None and socio.rol == "socio"
    assert autenticar("isaias", "mala") is None
    assert autenticar("nadie", "clave123") is None
    print("UC-01 autenticación: OK")

    assert obtener_socio("isaias") is not None
    clubes = listar_clubes_de_socio("isaias")
    assert len(clubes) == 1 and clubes[0].nombre == "Racing"
    assert listar_clubes_de_socio("ana") == []
    print("UC-02 datos y clubes: OK")

    assert len(listar_cuotas("isaias")) == 2
    print("UC-03 listar cuotas: OK")

    assert "pagada" in pagar_cuota("isaias", "Agosto").lower()
    print("UC-04 pagar cuota: OK")

    assert len(listar_socios()) == 3
    print("UC-05 listar socios: OK")

    registrar_socio("Nuevo Socio", "20", "DNI", "99999999",
                    "Argentina", "nuevo", "clave999")
    assert obtener_socio("nuevo") is not None
    try:
        registrar_socio("Otro", "20", "DNI", "88888888",
                        "Argentina", "nuevo", "x")
        raise AssertionError("No debería permitir un usuario repetido")
    except ValueError:
        pass
    print("UC-06 registrar socio: OK")

    assert "suspendido" in suspender_socio("isaias").lower()
    assert obtener_socio("isaias").estado == "Suspendido"
    assert "suspendido" in suspender_socio("isaias").lower()
    assert "reactivado" in reactivar_socio("isaias").lower()
    assert obtener_socio("isaias").estado == "Activo"
    assert "reactivación" in reactivar_socio("isaias")
    print("UC-07 suspender/reactivar: OK")

    print("\nTodas las pruebas de servicios pasaron.")

if __name__ == "__main__":
    main()