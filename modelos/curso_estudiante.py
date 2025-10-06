class EstudianteCurso:
    def __init__(self, id_estudiante_curso, matricula_estudiante, codigo_curso):
        self.id_estudiante_curso = id_estudiante_curso
        self.matricula_estudiante = matricula_estudiante  # FK a Estudiante
        self.codigo_curso = codigo_curso                  # FK a Curso
        self.nota_final = None
        self.estado = "Cursando"

    def registrar_nota(self, nota):
        if 1.0 <= nota <= 7.0:
            self.nota_final = nota
            self.estado = "Aprobado" if nota >= 4.0 else "Reprobado"
        else:
            print("Error: la nota debe estar entre 1.0 y 7.0")

    def mostrar_info(self):
        print("=== Información de Estudiante-Curso ===")
        print(f"ID: {self.id_estudiante_curso}")
        print(f"Matrícula Estudiante: {self.matricula_estudiante}")
        print(f"Código Curso: {self.codigo_curso}")
        print(f"Nota Final: {self.nota_final if self.nota_final else 'Sin nota'}")
        print(f"Estado: {self.estado}")

    def __str__(self):
        return f"Inscripción {self.id_estudiante_curso} - Estudiante {self.matricula_estudiante} en {self.codigo_curso}"
