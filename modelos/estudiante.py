
class Estudiante:
    def __init__(self, matricula_estudiante, nombre_estudiante, correo_estudiante, fecha_nacimiento, dirección_estudiante):
        self.matricula_estudiante = matricula_estudiante
        self.nombre_estudiante = nombre_estudiante
        self.correo_estudiante = correo_estudiante
        self.fecha_nacimiento = fecha_nacimiento
        self.dirección_estudiante = dirección_estudiante

    def mostrar_info(self):
        print("=== Información del Estudiante ===")
        print(f"Matrícula: {self.matricula_estudiante}")
        print(f"Nombre: {self.nombre_estudiante}")
        print(f"Correo: {self.correo_estudiante}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Dirección: {self.dirección_estudiante}")

    def __str__(self):
        return f"{self.matricula_estudiante} - {self.nombre_estudiante}"