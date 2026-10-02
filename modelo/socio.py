from modelo.persona import Persona


class Socio(Persona):
    def __init__(self, nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad,
                fecha_inscripcion, estado_cuota, usuario, contrasenia, rol):
        super().__init__(nombre_completo, edad, tipo_identificacion, identificacion, nacionalidad)
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
        datos_persona = super().mostrar_datos()
        return (f"{datos_persona}, "
                f"Fecha de inscripción: {self.fecha_inscripcion}, "
                f"Estado: {self.estado_cuota}, "
                f"Usuario: {self.get_usuario()}")

    def asociar_club(self, club):
        if club in self.clubes:
            return "Ya pertenece a este club"
        else:
            self.clubes.append(club)
            return f"El socio se asoció al club: {club}. Clubes actuales: {self.clubes}"

    def dejar_club(self, club):
        if club in self.clubes:
            self.clubes.remove(club)
            return f"El socio dejó el club: {club}. Clubes actuales: {self.clubes}"
        else:
            return "El socio no pertenece a ese club"

    def generar_cuota(self, periodo, monto):
        cuota = {
            "periodo": periodo,
            "monto": monto,
            "pagada": False
        }
        self.cuotas.append(cuota)
        return f"Se generó una nueva cuota: {cuota}"

    def pagar_cuota(self, periodo):
        for cuota in self.cuotas:
            if cuota["periodo"] == periodo and cuota["pagada"] == False:
                cuota["pagada"] = True
                return f"Se registró el pago de la cuota del período {periodo}"

        return f"No se encontró una cuota pendiente para el período {periodo}"

    def tiene_deudas(self):
        for cuota in self.cuotas:
            if cuota["pagada"] == False:
                return True

        return False

    def cantidad_cuotas_pendientes(self):
        cantidad = 0

        for cuota in self.cuotas:
            if cuota["pagada"] == False:
                cantidad = cantidad + 1

        return cantidad

    def suspender_socio(self):
        if self.estado_cuota == "suspendido":
            return "El socio se encuentra suspendido"
        else:
            self.estado_cuota = "suspendido"
            return "El socio está suspendido"

    def reactivar_socio(self):
        if self.estado_cuota == "activo":
            return "El socio se encuentra activo"
        else:
            self.estado_cuota = "activo"
            return "El socio está reactivado"

    def actualizar_contrasenia(self, contrasenia_actual, contrasenia_nueva):
        if contrasenia_actual == self.get_contrasenia():
            self.set_contrasenia(contrasenia_nueva)
            return "La contraseña se actualizó correctamente"
        else:
            return "La contraseña actual ingresada es incorrecta"

    def verificar_acceso(self, usuario_ingresado, contrasenia_ingresada):
        if usuario_ingresado == self.get_usuario() and contrasenia_ingresada == self.get_contrasenia():
            return True
        else:
            return False

    def es_admin(self):
        return self.rol == "admin"