
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
        print("Nombre completo: ", self.nombre_completo)
        print("Edad : ", self.edad)
        print("Tipo de Identificacion: ",self.get_tipo_identificacion())
        print("Identificacion: ",self.get_identificacion())
        print("Nacionalidad: ",self.get_nacionalidad())
        print("hola")
    
    def verificar_edad(self):
        if self.edad > 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")
    
    def verificar_identificacion(self,):
        if len(str(self.__identificacion)) == 8:
            print("la identificación es válida")
        else:
            print("la identificación no es válida")

mipersona = Persona("Micaela",16,"DNI","12345678","Argentina")
mipersona.mostrar_datos()
mipersona.verificar_edad()
mipersona.verificar_identificacion()

# Verificar que la identificación ingresada sea válida y no se encuentre vacía.