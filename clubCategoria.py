from datetime import date
from club import Club

class ClubCategoria(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []

    def get_socios(self):
        return self.__socios

    def set_socios(self, socios):
        self.__socios = socios

    def registrar_socio(self, nombre_socio, activo=True):
        socio = {"nombre": nombre_socio, "activo": activo}
        self.__socios.append(socio)
        print("Se agregó un socio a la lista", self.__socios)

    def eliminar_socio(self, nombre):
        socio = self.buscar_socio(nombre)
        if socio:
            self.__socios.remove(socio)
            print("Se eliminó al socio", socio, "de la lista")
        else:
            print("No se encontró al socio", nombre)

    def buscar_socio(self, nombre):
        for socio in self.__socios:
            if socio["nombre"].lower() == nombre.lower():
                return socio
        return None

    def mostrar_cantidad_socios(self):
        print("Cantidad de socios:", len(self.__socios))

    def agregar_actividad_deportiva(self, actividad):
        self.actividades.append(actividad)
        print("Se agregó una actividad a la lista", self.actividades)

    def eliminar_actividad_deportiva(self, actividad):
        if actividad in self.actividades:
            self.actividades.remove(actividad)
            print("Se eliminó la actividad", actividad, "de la lista")
        else:
            print("La actividad", actividad, "no se encuentra en la lista")

    def mostrar_actividad_deportiva(self):
        print("Cantidad de actividades:", len(self.actividades))
        print("La lista de actividades:", self.actividades)

    def calcular_porcentaje_socios(self):
        if len(self.__socios) == 0:
            print("No hay socios registrados")
            return 0
        cantidad_activos = 0
        for socio in self.__socios:
            if socio["activo"]:
                cantidad_activos = cantidad_activos + 1
        porcentaje = (cantidad_activos / len(self.__socios)) * 100
        print("Porcentaje de activos: ", porcentaje, "%")
        return porcentaje


mi_club_recreativo = ClubCategoria("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo", date(1901, 5, 25))
mi_club_recreativo.registrar_socio("Joaquin")
mi_club_recreativo.registrar_socio("Carlos")
mi_club_recreativo.mostrar_cantidad_socios()
mi_club_recreativo.agregar_actividad_deportiva("Basquetball")
mi_club_recreativo.agregar_actividad_deportiva("Hockey")
mi_club_recreativo.agregar_actividad_deportiva("Voley")
mi_club_recreativo.mostrar_actividad_deportiva()
mi_club_recreativo.calcular_porcentaje_socios()