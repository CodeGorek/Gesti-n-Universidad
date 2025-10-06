
class Curso():
    def __init__(self, codigo_curso, nombre, creditos_suma, cod_carrera, pre_requisito, id_horarios):
        self.codigo_curso = codigo_curso
        self.nombre = nombre
        self.creditos_suma = creditos_suma
        self.cod_carrera = cod_carrera # FK a carrera
        self.pre_requisito = pre_requisito
        self.id_horarios = id_horarios # FK a horarios
    
    def mostrar_info(self):
        print("--- Información del Curso ---")
        print(f"Código del Curso: {self.codigo_curso}")
        print(f"Nombre: {self.nombre}")
        print(f"Créditos: {self.creditos_suma}")
        print(f"Código de Carrera: {self.cod_carrera}")
        print(f"Pre-requisito: {self.pre_requisito if self.pre_requisito else 'Ninguno'}")
        print(f"ID Horarios: {self.id_horarios}")

    def __str__(self):
        return f"{self.codigo_curso} - {self.nombre} ({self.creditos_suma} créditos)"
    