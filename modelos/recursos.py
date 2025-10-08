
class Recursos():
    def __init__(self, cod_recurso, cod_curso, cod_profesor, url, tipo_recurso, nombre_recurso):
        self.cod_recurso = cod_recurso  # PK
        self.cod_curso = cod_curso  # FK a Curso
        self.cod_profesor = cod_profesor  # FK a Profesor
        self.url = url
        self.tipo_recurso = tipo_recurso  # formato, 'video', 'documento'
        self.nombre_recurso = nombre_recurso

    def mostrar_info(self):
        print("=== Información del Recurso ===")
        print(f"Codigo del recurso: {self.cod_recurso}")
        print(f"Nombre del recurso: {self.nombre_recurso}")
        print(f"Tipo del recurso: {self.tipo_recurso}")
        print(f"link URL: {self.url}")
        print(f"Código del Curso: {self.cod_curso}")
        print(f"Código del Profesor: {self.cod_profesor}")

    
    def __str__(self):
        return f"Recurso {self.cod_recurso} - Curso {self.cod_curso} - Profesor {self.cod_profesor}"