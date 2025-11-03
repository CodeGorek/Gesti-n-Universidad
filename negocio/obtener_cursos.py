from modelos.curso import Curso
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable

def listado_cursos():
    tabla_cursos = PrettyTable()
    tabla_cursos.field_names = ['Cod_curso', 'Nombre_Curso', 'Creditos','Pre_requisitos']
    listado_cursos = obtener_lista_objetos(Curso)
    if listado_cursos:
        for curso in listado_cursos:
            tabla_cursos.add_row(
                [curso.cod_curso, curso.nombre_curso, curso.creditos, curso.pre_requisitos])
            # print(f'{curso.cod_curso} {curso.nombre_curso} {curso.creditos},{curso.pre_requisito}')
        print(tabla_cursos)