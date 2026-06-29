class Cuota:
    def __init__(self, estado, fecha_vencimiento, periodo):
        self.__estado = estado
        self.fecha_vencimiento = fecha_vencimiento
        self.periodo = periodo
        
    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado
    
    # def mostrar_datos(self):
    #     print("Estado: ", self.get_estado())
    #     print("Fecha de vencimiento ", self.fecha_vencimiento)
    #     print("Periodo: ",self.periodo)

micuota = Cuota("pagada","20/05/2025","40 días")
# micuota.mostrar_datos()