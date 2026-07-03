from clubCategoria import ClubRecreativo

class Administrador(ClubRecreativo):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion,nombre_usuario, usuario, contrasenia):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.nombre_usuario = nombre_usuario
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def registrar_nuevo_socio(self,socio):
            super().registrar_socio(socio)

    def get_usuario (self):
        return self.__usuario

    def set_usuario (self, usuario):
        self.__usuario = usuario

    def get_contrasenia (self):
        return self.__contrasenia
    
    def set_contrasenia (self, contrasenia):
        self.__contrasenia = contrasenia
    



miadministrador = Administrador("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo", "25/05/1901","Santino","Santy","aguanteriver")
miadministrador.registrar_nuevo_socio("Gaspar")