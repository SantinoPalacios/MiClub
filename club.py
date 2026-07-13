from datetime import date

class Club:
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion):
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
        self.__fecha_fundacion = fecha_fundacion
    
    
    def mostrar_antiguedad(self):
        hoy = date.today()
        años = hoy.year - self.__fecha_fundacion.year

        if (hoy.month, hoy.day) < (self.__fecha_fundacion.month, self.__fecha_fundacion.day):
            años -= 1
        return años
    
    def es_historico(self):
        return self.mostrar_antiguedad() > 50

    def mostrar_info(self):
        print("Nombre del club : ", self.nombre)
        print("Descripción del club :",self.descripcion)
        print("Ubicación del club :",self.ubicacion)
        print("Presidente del club : ", self.get_presidente())
        print("Fecha de Fundación del club : ", self.get_fecha_fundacion())
        print("Antiguedad:", self.mostrar_antiguedad(), "años")

        if self.es_historico():
            print("El club es histórico")
        else:
            print("El club no es histórico")

miclub = Club("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo",  date(1901, 5, 25))
miclub.mostrar_antiguedad()
miclub.mostrar_info()