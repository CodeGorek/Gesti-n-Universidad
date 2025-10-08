class ProfesorCurso:
    def __init__(self, cod_profesor_curso, cod_curso, cod_profesor):
        self.cod_profesor_curso = cod_profesor_curso
        self.cod_curso = cod_curso          # FK a Curso  
        self.cod_profesor = cod_profesor            # FK a Profesor

    def mostrar_info(self):
        print("=== Información de Profesor-Curso ===")
        print(f"ID: {self.cod_profesor_curso}")
        print(f"Código Curso: {self.cod_curso}")
        print(f"Código Profesor: {self.cod_profesor}")

    def __str__(self):
        return f"ProfesorCurso {self.cod_profesor_curso} - Curso {self.cod_curso}"
    
    