from negocio.negocio_estudiantes import obtener_matricula_estudiante
from modelos.estudiante_curso import Estudiante_Curso
from modelos.curso import Curso
from datos.obtener_datos import obtener_lista_objetos
from negocio.negocio_cursos import obtener_cod_curso
from datos.insertar_datos import insertar_objeto


def ver_cursos_estudiante():
    matricula = input("Ingrese la matrícula del estudiante: ").strip()
    estudiante = obtener_matricula_estudiante(matricula)
    if not estudiante:
        print("Estudiante no encontrado.")
        return

    inscripciones = obtener_lista_objetos(Estudiante_Curso)
    cursos_est = [i for i in inscripciones if i.matricula_estudiante == matricula]

    if not cursos_est:
        print("El estudiante no tiene cursos inscritos.")
        return

    print(f"\nCursos de {estudiante.nombre_estudiante}:")
    for i in cursos_est:
        curso = obtener_cod_curso(i.cod_curso)
        print(f"- {curso.cod_curso}: {curso.nombre_curso}")

def asignar_curso_a_estudiante():
    # Pedimos la matrícula del estudiante
    matricula = input("Ingrese la matrícula del estudiante: ").strip()
    estudiante = obtener_matricula_estudiante(matricula)

    if not estudiante:
        print("Estudiante no encontrado.")
        return

    # Obtenemos la lista actual de inscripciones
    inscripciones = obtener_lista_objetos(Estudiante_Curso)
    
    # Contamos cuántos cursos tiene actualmente el estudiante
    cursos_actuales = [i for i in inscripciones if i.matricula_estudiante == matricula]
    if len(cursos_actuales) >= 3:
        print(f" El estudiante {estudiante.nombre_estudiante} ya tiene 3 cursos inscritos. No puede tomar más.")
        return

    # Pedimos el código del curso
    cod_curso = input("Ingrese el código del curso: ").strip()
    curso = obtener_cod_curso(cod_curso)

    if not curso:
        print("Curso no encontrado.")
        return

    # Verificamos si ya está inscrito en ese curso
    ya_tiene = any(i.cod_curso == cod_curso for i in cursos_actuales)
    if ya_tiene:
        print("El estudiante ya está inscrito en este curso.")
        return

    # Creamos la relación
    nueva_inscripcion = Estudiante_Curso(matricula_estudiante=matricula, cod_curso=cod_curso)
    insertar_objeto(nueva_inscripcion)

    print(f"Estudiante {estudiante.nombre_estudiante} inscrito correctamente en el curso {curso.nombre_curso}.")
