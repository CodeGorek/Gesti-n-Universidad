

class Profesor:
    def __init__(self,cod_profesor, nombre_profesor, correo_profesor, especialidad):
        self.cod_profesor = cod_profesor  # PK
        self.nombre_profesor = nombre_profesor
        self.correo_profesor = correo_profesor
        self.especialidad = especialidad

    def mostrar_info(self):
        print("=== Información del Profesor ===")
        print(f"ID Profesor: {self.cod_profesor}")
        print(f"Nombre: {self.nombre_profesor}")
        print(f"Correo: {self.correo_profesor}")
        print(f"Especialidad: {self.especialidad}")

    def __str__(self):
        return f"{self.nombre_profesor} ({self.especialidad})"