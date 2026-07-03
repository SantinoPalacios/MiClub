from club import Club

class ClubRecreativo(Club):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.__socios = []
        self.actividades = []
    
    def get_socios (self):
        return self.__socios

    def set_socios (self, socios):
        self.__socios = socios
    
    def registrar_socio(self,socio):
        self.__socios.append(socio)
        print("Se agregó un socio a la lista", self.__socios)
    
    def mostrar_cantidad(self):
        print("Cantidad de socios:", len(self.__socios))
    
    def agregar_actividad_deportiva(self,actividad):
        self.actividades.append(actividad)
        print("Se agregó una actividad a la lista", self.actividades)
    
    def mostrar_actividad_deportiva(self):
        print("Cantidad de actividades:",len(self.actividades))

mi_club_recreativo = ClubRecreativo("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo", "25/05/1901")
mi_club_recreativo.registrar_socio("Joaquin")
mi_club_recreativo.registrar_socio("Carlos")
mi_club_recreativo.mostrar_cantidad()
mi_club_recreativo.agregar_actividad_deportiva("Basquetball")
mi_club_recreativo.agregar_actividad_deportiva("Hockey")
mi_club_recreativo.agregar_actividad_deportiva("Voley")
mi_club_recreativo.mostrar_actividad_deportiva()
mi_club_recreativo.mostrar_cantidad()