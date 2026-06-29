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

mi_club_recreativo = ClubRecreativo("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo", "25/05/1901")