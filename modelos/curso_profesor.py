class ProfesorCurso:
    def __init__(self, id_profesor_curso, codigo_curso, correo_profesor):
        self.id_profesor_curso = id_profesor_curso
        self.codigo_curso = codigo_curso          # FK a Curso
        self.correo_profesor = correo_profesor    # FK a Profesor

    def mostrar_info(self):
        print("=== Información de Profesor-Curso ===")
        print(f"ID: {self.id_profesor_curso}")
        print(f"Código Curso: {self.codigo_curso}")
        print(f"Correo Profesor: {self.correo_profesor}")

    def __str__(self):
        return f"ProfesorCurso {self.id_profesor_curso} - Curso {self.codigo_curso}"