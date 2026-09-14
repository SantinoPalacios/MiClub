from datetime import date

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
        if not isinstance(fecha_fundacion, date):
            raise TypeError("fecha_fundacion debe ser un objeto date, no un str")

        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.__presidente = presidente
        self.__fecha_fundacion = fecha_fundacion

    def get_presidente(self):
        return self.__presidente

    def set_presidente(self, presidente):
        self.__presidente = presidente

    def get_fecha_fundacion(self):
        return self.__fecha_fundacion

    def set_fecha_fundacion(self, fecha_fundacion):
        if not isinstance(fecha_fundacion, date):
            raise TypeError("fecha_fundacion debe ser un objeto date, no un str")
        self.__fecha_fundacion = fecha_fundacion

    def cambiar_presidente(self, nuevo_presidente):
        anterior_presidente = self.__presidente
        self.__presidente = nuevo_presidente
        return f"Cambio de autoridades en {self.nombre}. Presidente anterior: {anterior_presidente}, Nuevo presidente: {self.__presidente}"

    def mostrar_antiguedad(self):
        fecha_fundacion = self.__fecha_fundacion
        hoy = date.today()
        años = hoy.year - fecha_fundacion.year
        if (hoy.month, hoy.day) < (fecha_fundacion.month, fecha_fundacion.day):
            años -= 1
        return años

    def es_historico(self):
        return self.mostrar_antiguedad() > 50

    def mostrar_info(self):
        return (f"Nombre del club: {self.nombre}, "
            f"Descripción del club: {self.descripcion}, "
            f"Ubicación del club: {self.ubicacion}, "
            f"Presidente del club: {self.get_presidente()}, "
            f"Fecha de Fundación del club: {self.get_fecha_fundacion()}, "
            f"Antigüedad: {self.mostrar_antiguedad()} años")

    def mensaje_historico(self):
        if self.es_historico():
            return "El club es histórico"
        else:
            return "El club no es histórico"