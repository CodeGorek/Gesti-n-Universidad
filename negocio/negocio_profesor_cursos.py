from modelos.profesor_curso import Profesor_Curso
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
from iu.iu_profesor_curso import ingresar_cod_curso,ingresar_cod_profesor,ingresar_cod_profesor_curso
from modelos.profesor import Profesor
from modelos.curso import Curso
from auxiliares.normalizar_cadena import normalizar_cadena
from datos.insertar_datos import insertar_objeto
from datos.conexion import sesion

def listado_profesores_cursos():
    tabla_profesor_curso = PrettyTable()
    tabla_profesor_curso.field_names = ['Cod_profesor_curso', 'Cod_curso', 'Cod_profesor']
    listado_profesor_curso = obtener_lista_objetos(Profesor_Curso)
    if listado_profesor_curso:
        for profesor_curso in listado_profesor_curso:
            tabla_profesor_curso.add_row(
                [profesor_curso.cod_profesor_curso, profesor_curso.cod_curso, profesor_curso.cod_profesor])
        print(tabla_profesor_curso)

def obtener_cod_profesor(cod_profesor):
    listado_profesores = obtener_lista_objetos(Profesor)
    profesor_encontrado = None
    if listado_profesores:
        for profesor in listado_profesores:
            if normalizar_cadena(profesor.cod_profesor) == normalizar_cadena(cod_profesor):
                profesor_encontrado = profesor
                break
    return profesor_encontrado

def obtener_cod_curso(cod_curso):
    listado_cursos = obtener_lista_objetos(Curso)
    curso_encontrado = None
    if listado_cursos:
        for curso in listado_cursos:
            if normalizar_cadena(curso.cod_curso) == normalizar_cadena(cod_curso):
                curso_encontrado = curso
                break
    return curso_encontrado

def insertar_profesores_cursos():
    profesor = ingresar_cod_profesor()

    profesor_encontrado = obtener_cod_profesor(profesor)
    if profesor_encontrado is not None:
        buscar_cod_curso = ingresar_cod_curso()
        codigo_curso_encontrado = obtener_cod_curso(buscar_cod_curso)
        if codigo_curso_encontrado is not None:
            # INSTANCIA DE CLASE
            codigo_curso_profesor = ingresar_cod_profesor
            nuevo_profesor_curso = Profesor_Curso(cod_profesor_curso=codigo_curso_profesor,
                                cod_curso= buscar_cod_curso,
                                cod_profesor = profesor,
                                habilitado=True)
            insertar_objeto(nuevo_profesor_curso)
            print("Relación profesor-curso insertada correctamente.")
    else:
        print('Error al relacionar un profesor con un curso.')