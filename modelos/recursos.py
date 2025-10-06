
class Recursos():
    def __init__(self, id_recurso, codigo_curso, id_profesor, url):
        self.id_recurso = id_recurso  # PK
        self.codigo_curso = codigo_curso  # FK a Curso
        self.id_profesor = id_profesor  # FK a Profesor
        self.url = url

    def mostrar_info(self):
        print("=== Información del Recurso ===")
        print(f"ID Recurso: {self.id_recurso}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"URL: {self.url}")
    
    def __str__(self):
        return f"Recurso {self.id_recurso} - Curso {self.codigo_curso} - Profesor {self.id_profesor}"