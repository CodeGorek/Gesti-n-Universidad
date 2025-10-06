

class Profesor:
    def __init__(self,id_profesor, nombre, correo, especialidad):
        self.nombre = nombre
        self.correo = correo
        self.especialidad = especialidad
        self.id_profesor = id_profesor  # PK

    def mostrar_info(self):
        print("=== Información del Profesor ===")
        print(f"ID Profesor: {self.id_profesor}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Especialidad: {self.especialidad}")

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"