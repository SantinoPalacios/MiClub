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
        
    def mostrar_info(self):
        print("Nombre del club : ", self.nombre)
        print("Descripción del club :",self.descripcion)
        print("Ubicación del club :",self.ubicacion)
        print("Presidente del club : ", self.get_presidente())
        print("Fecha de Fundación del club : ",self.get_fecha_fundacion())


miclub = Club("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo", "25/05/1901")
miclub.mostrar_info()