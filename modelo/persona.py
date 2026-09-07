class Persona:
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.__tipo_identificacion = tipo_identificacion
        self.__identificacion = identificacion
        self.__nacionalidad = nacionalidad


    def get_tipo_identificacion (self):
        return self.__tipo_identificacion

    def set_tipo_identificacion (self, tipo_identificacion):
        self.__tipo_identificacion = tipo_identificacion

    
    def get_identificacion (self):
        return self.__identificacion

    def set_identificacion (self, identificacion):
        self.__identificacion = identificacion

    def get_nacionalidad (self):
        return self.__nacionalidad

    def set_nacionalidad (self, nacionalidad):
        self.__nacionalidad = nacionalidad


    def mostrar_datos(self):
        return (f"Nombre completo: {self.nombre_completo}, "
            f"Edad: {self.edad}, "
            f"Tipo de Identificación: {self.get_tipo_identificacion()}, "
            f"Identificación: {self.get_identificacion()}, "
            f"Nacionalidad: {self.get_nacionalidad()}")

    def verificar_edad(self):
        if self.edad >= 18:
            return "La persona es mayor de edad"
        else:
            return "La persona es menor de edad"
    
    def verificar_identificacion(self,):
        if len(str(self.__identificacion)) == 8:
            return "la identificación es válida"
        else:
            return "la identificación no es válida"
