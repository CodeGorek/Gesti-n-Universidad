from negocio.negocio_estudiantes import obtener_matricula_estudiante
from modelos.estudiante_curso import EstudianteCurso
from modelos.curso import Curso
from datos.obtener_datos import obtener_lista_objetos
from negocio.negocio_cursos import obtener_cod_curso
from datos.insertar_datos import insertar_objeto
from datos.conexion import sesion
from modelos.estudiante import Estudiante
from auxiliares.normalizar_cadena import normalizar_cadena
from iu.iu_curso import ingresar_nombre_curso
from datos.modificar_datos import modificar_objeto



def obtener_cod_curso(cod_curso):
    listado_cursos = obtener_lista_objetos(EstudianteCurso)
    curso_encontrado = None
    if listado_cursos:
        for curso in listado_cursos:
            if normalizar_cadena(curso.cod_curso) == normalizar_cadena(cod_curso):
                curso_encontrado = curso
                break
    return curso_encontrado

def ver_cursos_estudiante():
    matricula = input("Ingrese la matrícula del estudiante: ").strip()
    
    estudiante = sesion.query(Estudiante).filter_by(matricula_estudiante=matricula, habilitado=True).first()
    if not estudiante:
        print("Estudiante no encontrado o deshabilitado.")
        return

    # Obtenemos todas las inscripciones habilitadas del estudiante
    cursos_est = sesion.query(EstudianteCurso).filter_by(matricula_estudiante=matricula, habilitado=True).all()

    if not cursos_est:
        print(f"El estudiante {estudiante.nombre_estudiante} no tiene cursos inscritos.")
        return

    print(f"\nCursos inscritos de {estudiante.nombre_estudiante}:")
    for inscripcion in cursos_est:
        curso = sesion.query(Curso).filter_by(cod_curso=inscripcion.cod_curso, habilitado=True).first()
        if curso:
            print(f"- {curso.cod_curso}: {curso.nombre_curso}")

def asignar_curso_a_estudiante():
    matricula = input("Ingrese la matrícula del estudiante: ").strip()
    estudiante = sesion.query(Estudiante).filter_by(matricula_estudiante=matricula, habilitado=True).first()
    
    if not estudiante:
        print("Estudiante no encontrado o deshabilitado.")
        return

    nombre_estudiante = estudiante.nombre_estudiante

    # Contamos cuántos cursos tiene actualmente
    cursos_actuales = sesion.query(EstudianteCurso).filter_by(matricula_estudiante=matricula, habilitado=True).all()
    if len(cursos_actuales) >= 3:
        print(f"El estudiante {nombre_estudiante} ya tiene 3 cursos inscritos. No puede tomar más.")
        return

    cod_curso = input("Ingrese el código del curso: ").strip()
    curso = sesion.query(Curso).filter_by(cod_curso=cod_curso, habilitado=True).first()

    if not curso:
        print("Curso no encontrado o deshabilitado.")
        return

    # Verificamos duplicados
    ya_tiene = sesion.query(EstudianteCurso).filter_by(matricula_estudiante=matricula, cod_curso=cod_curso, habilitado=True).first()
    if ya_tiene:
        print(f"El estudiante {nombre_estudiante} ya está inscrito en el curso {curso.nombre_curso}.")
        return

    #Creo variable para guardar nombre antes de el commit
    nombre_curso_print = curso.nombre_curso

    # Creamos la inscripción
    nueva_inscripcion = EstudianteCurso(
        matricula_estudiante=matricula,
        cod_curso=cod_curso,
        habilitado=True
    )
    insertar_objeto(nueva_inscripcion)

    print(f"Estudiante {nombre_estudiante} inscrito correctamente en el curso {nombre_curso_print}.")

def eliminado_logico_curso():
    curso = ingresar_nombre_curso()
    curso_encontrado = obtener_cod_curso(curso)

    if curso_encontrado:
        if curso_encontrado.habilitado:
            curso_encontrado.habilitado = False
            print(f"curso '{curso_encontrado.nombre_curso}' deshabilitado correctamente.")
        else:
            curso_encontrado.habilitado = True
            print(f"curso '{curso_encontrado.nombre_curso}' habilitado correctamente.") 
    
        modificar_objeto()
    else:
        print('curso NO existe, vuelva a intentarlo.')