

class Profesor:
    def __init__(self, nombre, correo, especialidad):
        self.nombre = nombre
        self.correo = correo
        self.especialidad = especialidad

    def mostrar_info(self):
        print("=== Información del Profesor ===")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Especialidad: {self.especialidad}")

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"