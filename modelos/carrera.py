
class Carrera():
    def __init__(self, cod_carrera, descripción, creditos_max_semestre, semestre_duración):
        self.cod_carrera = cod_carrera
        self.descripción = descripción
        self.creditos_max_semestre = creditos_max_semestre
        self.semestre_duración = semestre_duración
    
    def mostrar_info(self):
        print("--- Información de la Carrera ---")
        print(f"Código de Carrera: {self.cod_carrera}")
        print(f"Descripción: {self.descripción}")
        print(f"Créditos Máximos por Semestre: {self.creditos_max_semestre}")
        print(f"Duración en Semestres: {self.semestre_duración}")

    def __str__(self):
        return f"{self.cod_carrera} - {self.descripción} ({self.semestre_duración} semestres, {self.creditos_max_semestre} créditos max.)"
    