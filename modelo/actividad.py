class Actividad:
    def __init__(self, nombre, dia, horario, club_id):
        self.nombre = nombre
        self.dia = dia
        self.horario = horario
        self.club_id = club_id

    def mostrarInfo(self):
        return f"Actividad: {self.nombre} , Día: {self.dia} , Horario: {self.horario}"