from datetime import datetime

class Cuota():
    def __init__(self, estado, fecha_vencimiento, periodo):
        self.__estado = estado
        self.fecha_vencimiento = fecha_vencimiento
        self.periodo = periodo

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def verificar_vencimiento(self, formato="%d/%m/%Y"):
        fecha_vencimiento = datetime.strptime(self.fecha_vencimiento, formato)
        fecha_actual = datetime.now()
        diferencia_dias = (fecha_actual.date() - fecha_vencimiento.date()).days

        if diferencia_dias > 0:
            return "vencida"
        elif diferencia_dias == 0:
            return "vence hoy"
        else:
            return "vigente"


    def dias_para_vencer(self, formato="%d/%m/%Y"): # Me devuelve un numero negativo hay un metodo abs de valor absoluto que modifica eso. 
        fecha_vencimiento = datetime.strptime(self.fecha_vencimiento, formato)
        fecha_actual = datetime.now()
        dias_restantes = (fecha_vencimiento.date() - fecha_actual.date()).days 

        if dias_restantes > 0:
            return f"Faltan {dias_restantes} días para el vencimiento."
        elif dias_restantes == 0:
            return "La cuota vence hoy."
        else:
            return f"La cuota venció hace {dias_restantes} días"

    def mostrar_datos(self):
        print("Estado: ", self.get_estado())
        print("Fecha de vencimiento: ", self.fecha_vencimiento)
        print("Periodo: ", self.periodo)
    
    def registrar_cuota_pagada(self):
        if self.get_estado() == "pagada":
            print("Esta cuota ya estaba pagada")
        else:
            self.set_estado("pagada")
            print("Se registró el pago de la cuota del período", self.periodo)
    
    def actualizar_estado(self): # esta funcion tira un bug pisa los valores de la variable entonces hay que retornar para que la funcion corte ahí.
        print("La cuota ya está pagada, no hace falta actualizar el estado")
        
        resultado = self.verificar_vencimiento()
        if resultado == "vencida":
            self.set_estado("vencida")
            print("La cuota pasó a estado: vencida")
        else:
            self.set_estado("pendiente")
            print("La cuota se mantiene en estado: pendiente")
    
    def renovar_cuota(self, nuevo_periodo, nueva_fecha_vencimiento):
        self.periodo = nuevo_periodo
        self.fecha_vencimiento = nueva_fecha_vencimiento
        self.set_estado("pendiente")
        print("Se renovó la cuota para el período", nuevo_periodo)
        print("Nueva fecha de vencimiento:", nueva_fecha_vencimiento)


micuota = Cuota("pagada", "20/05/2025", "40 días")

micuota.mostrar_datos()
print("Verificación:", micuota.verificar_vencimiento())
print(micuota.dias_para_vencer())
micuota.registrar_cuota_pagada()
micuota.mostrar_datos()
micuota.actualizar_estado()
micuota.mostrar_datos()
micuota.renovar_cuota("Junio 2025", "20/06/2025")
micuota.mostrar_datos()