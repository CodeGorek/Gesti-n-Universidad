

class Horarios:
    def __init__(self, cod_horario, sección, día):
        self.cod_horario = cod_horario
        self.sección = sección
        self.día = día
    
    def mostrar_info(self):
        print("--- Información del Horario ---")
        print(f"Codigo Horario: {self.cod_horario}")
        print(f"Sección: {self.sección}")
        print(f"Día: {self.día}")

    def __str__(self):
        return f"Horario ID: {self.cod_horario}, Sección: {self.sección}, Día: {self.día}"