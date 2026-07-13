from cuota import Cuota

class Socio(Cuota):
    def __init__(self, fecha_inscripcion, estado_cuota, usuario, contrasenia):
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado_cuota = estado_cuota
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def get_usuario (self):
        return self.__usuario

    def set_usuario (self, usuario):
        self.__usuario = usuario

    def get_contrasenia (self):
        return self.__contrasenia
    
    def set_contrasenia (self, contrasenia):
        self.__contrasenia = contrasenia
    
    # def mostrar_datos(self):
    #     print("Fecha de inscripción: ", self.fecha_inscripcion)
    #     print("Estado: ", self.estado)
    #     print("Usuario: ",self.get_usuario())
    #     print("Contraseña: ",self.get_contrasenia())


misocio = Socio("1/10/2021","activo","juanin","elmascapo456")
# misocio.mostrar_datos()