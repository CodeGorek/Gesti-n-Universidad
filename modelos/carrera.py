
class Carrera():
    def __init__(self, cod_carrera, descripcion, creditos_max_semestre, semestre_duracion):
        self.cod_carrera = cod_carrera
        self.descripcion = descripcion
        self.creditos_max_semestre = creditos_max_semestre
        self.semestre_duracion = semestre_duracion
    
    def mostrar_info(self):
        print("--- Información de la Carrera ---")
        print(f"Código de Carrera: {self.cod_carrera}")
        print(f"Descripción: {self.descripcion}")
        print(f"Créditos Máximos por Semestre: {self.creditos_max_semestre}")
        print(f"Duración en Semestres: {self.semestre_duracion}")

    def __str__(self):
        return f"{self.cod_carrera} - {self.descripcion} ({self.semestre_duracion} semestres, {self.creditos_max_semestre} créditos max.)"
    