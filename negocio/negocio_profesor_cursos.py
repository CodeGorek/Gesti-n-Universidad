from modelos.profesor_curso import Profesor_Curso
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable


def listado_profesores_cursos():
    tabla_profesor_curso = PrettyTable()
    tabla_profesor_curso.field_names = ['Cod_profesor_curso', 'Cod_curso', 'Cod_profesor']
    listado_profesor_curso = obtener_lista_objetos(Profesor_Curso)
    if listado_profesor_curso:
        for profesor_curso in listado_profesor_curso:
            tabla_profesor_curso.add_row(
                [profesor_curso.cod_profesor_curso, profesor_curso.cod_curso, profesor_curso.cod_profesor])
        print(tabla_profesor_curso)