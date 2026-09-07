class Actividad:
    def __init__(self, nombre, dia, horario):
        self.nombre = nombre
        self.dia = dia
        self.horario = horario

    def mostrarInfo(self):
        return f"Actividad: {self.nombre} , Día: {self.dia} , Horario: {self.horario}"