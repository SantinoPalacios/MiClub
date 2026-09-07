from modelo.persona import Persona

class Socio(Persona):
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad, fecha_inscripcion, estado_cuota, usuario, contrasenia,rol):
        super().__init__(nombre_completo,edad,tipo_identificacion,identificacion,nacionalidad)
        self.clubes = []
        self.cuotas = []
        self.fecha_inscripcion = fecha_inscripcion
        self.estado_cuota = estado_cuota
        self.__usuario = usuario
        self.__contrasenia = contrasenia
        self.rol = rol

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, contrasenia):
        self.__contrasenia = contrasenia

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Fecha de inscripción:", self.fecha_inscripcion)
        print("Estado:", self.estado_cuota)
        print("Usuario:", self.get_usuario())

    def asociar_club(self, club):
        if club in self.clubes:
            print("Ya pertenece a este club")
        else:
            self.clubes.append(club)
            print("El socio se asoció al club:", club)
            print("Clubes actuales:", self.clubes)

    def dejar_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            print("El socio dejó el club:", club)
            print("Clubes actuales:", self.clubes)
        else:
            print("El socio no pertenece a ese club")

    def generar_cuota(self, periodo, monto):
        cuota = {
            "periodo": periodo,
            "monto": monto,
            "pagada": False
        }
        self.cuotas.append(cuota)
        print("Se generó una nueva cuota:", cuota)

    def pagar_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota["periodo"] == periodo and cuota["pagada"] == False:
                cuota["pagada"] = True
                print("Se registró el pago de la cuota del período", periodo)
                return

        print("No se encontró una cuota pendiente para el período", periodo)

    def tiene_deudas(self):
        for cuota in self.cuotas:
            if cuota["pagada"] == False:
                print("El socio tiene cuotas sin abonar")
                return True

        print("El socio no tiene deudas")
        return False

    def cantidad_cuotas_pendientes(self):
        cantidad = 0

        for cuota in self.cuotas:
            if cuota["pagada"] == False:
                cantidad = cantidad + 1

        print("Cuotas pendientes de pago:", cantidad)

    def suspender_socio(self):
        if self.estado_cuota == "suspendido":
            print("El socio se encuentra suspendido")
        else:
            self.estado_cuota = "suspendido"
            print("El socio está suspendido")

    def reactivar_socio(self):
        if self.estado_cuota == "activo":
            print("El socio se encuentra activo")
        else:
            self.estado_cuota = "activo"
            print("El socio está reactivado")

    def actualizar_contrasenia(self, contrasenia_actual, contrasenia_nueva):
        if contrasenia_actual == self.get_contrasenia():
            self.set_contrasenia(contrasenia_nueva)
            print("La contraseña se actualizó correctamente")
        else:
            print("La contraseña actual ingresada es incorrecta")

    def verificar_acceso(self, usuario_ingresado, contrasenia_ingresada):
        if usuario_ingresado == self.get_usuario() and contrasenia_ingresada == self.get_contrasenia():
            print("Acceso concedido")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False
        
    def es_admin(self):
        return self.rol == "admin"


