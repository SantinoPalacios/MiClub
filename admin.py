from datetime import date
from clubCategoria import ClubCategoria

class Administrador(ClubCategoria):
    def __init__(self, nombre, descripcion, ubicacion, presidente, fecha_fundacion, nombre_usuario, usuario, contrasenia):
        super().__init__(nombre, descripcion, ubicacion, presidente, fecha_fundacion)
        self.nombre_usuario = nombre_usuario
        self.__usuario = usuario
        self.__contrasenia = contrasenia

    def registrar_socio(self, socio):
        super().registrar_socio(socio)

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    def suspender_socio(self, nombre_socio):
        socio = self.buscar_socio(nombre_socio)
        if socio is None:
            print("No se encontró al socio", nombre_socio)
            return

        if socio["activo"] == False:
            print(nombre_socio, "ya se encuentra suspendido")
        else:
            socio["activo"] = False
            print(nombre_socio, "fue suspendido")

    def reactivar_socio(self, nombre_socio):
        socio = self.buscar_socio(nombre_socio)
        if socio is None:
            print("No se encontró al socio", nombre_socio)
            return

        if socio["activo"] == True:
            print(nombre_socio, "ya se encuentra activo")
        else:
            socio["activo"] = True
            print(nombre_socio, "fue reactivado")

    def listar_socios(self):
        socios = self.get_socios()
        if len(socios) == 0:
            print("El club no tiene socios registrados")
            return
        for socio in socios:
            print(socio)

    def verificar_credenciales(self, usuario, contrasenia):
        if usuario == self.get_usuario() and contrasenia == self.get_contrasenia():
            print("Acceso concedido")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False


miadministrador = Administrador("River Plate", "Millonario", "Buenos Aires", "Stefano Di Carlo", date(1901, 5, 25), "Santino", "Santy", "aguanteriver")
miadministrador.registrar_socio("Gaspar")
miadministrador.registrar_socio("Camila")
miadministrador.listar_socios()
miadministrador.suspender_socio("Gaspar")
miadministrador.reactivar_socio("Camila")
miadministrador.verificar_credenciales("micaela", "123")