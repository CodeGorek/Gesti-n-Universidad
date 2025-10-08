class EstudianteCurso:
    def __init__(self, cod_estudiante_curso, matricula_estudiante, cod_curso):
        self.cod_estudiante_curso = cod_estudiante_curso
        self.matricula_estudiante = matricula_estudiante  # FK a Estudiante
        self.cod_curso = cod_curso                  # FK a Curso
        
    def mostrar_info(self):
        print("=== Información de Estudiante-Curso ===")
        print(f"ID: {self.cod_estudiante_curso}")
        print(f"Matrícula Estudiante: {self.matricula_estudiante}")
        print(f"Código Curso: {self.cod_curso}")
       

    def __str__(self):
        return f"Inscripción {self.cod_estudiante_curso} - Estudiante {self.matricula_estudiante} en {self.cod_curso}"
