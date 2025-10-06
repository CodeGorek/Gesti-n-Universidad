

class Horarios:
    def __init__(self, id_horario, seccion, dia):
        self.id_horario = id_horario
        self.seccion = seccion
        self.dia = dia
    
    def mostrar_info(self):
        print("--- Información del Horario ---")
        print(f"ID Horario: {self.id_horario}")
        print(f"Sección: {self.seccion}")
        print(f"Día: {self.dia}")

    def __str__(self):
        return f"Horario ID: {self.id_horario}, Sección: {self.seccion}, Día: {self.dia}"