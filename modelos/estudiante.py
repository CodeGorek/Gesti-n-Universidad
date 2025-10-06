
class Estudiante:
    def __init__(self, matricula_estudiante, nombre, correo):
        self.matricula_estudiante = matricula_estudiante
        self.nombre = nombre
        self.correo = correo

    def mostrar_info(self):
        print("=== Información del Estudiante ===")
        print(f"Matrícula: {self.matricula_estudiante}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")

    def __str__(self):
        return f"{self.matricula_estudiante} - {self.nombre}"