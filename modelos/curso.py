
class Curso():
    def __init__(self, cod_curso, nombre, creditos, cod_carrera, pre_requisito, cod_horarios):
        self.cod_curso = cod_curso
        self.nombre = nombre
        self.creditos = creditos
        self.cod_carrera = cod_carrera # FK a carrera
        self.pre_requisito = pre_requisito
        self.cod_horarios = cod_horarios # FK a horarios
    
    def mostrar_info(self):
        print("--- Información del Curso ---")
        print(f"Código del Curso: {self.cod_curso}")
        print(f"Nombre: {self.nombre}")
        print(f"Créditos: {self.creditos}")
        print(f"Código de Carrera: {self.cod_carrera}")
        print(f"Pre-requisito: {self.pre_requisito if self.pre_requisito else 'Ninguno'}")
        print(f"ID Horarios: {self.cod_horarios}")

    def __str__(self):
        return f"{self.cod_curso} - {self.nombre} ({self.creditos} créditos)"
    