from modelos.carreras_cursos import Carrera_cursos
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable


def listado_carreras_cursos():
    tabla_carrera_cursos = PrettyTable()
    tabla_carrera_cursos.field_names = ['Cod_carrera_curso', 'Cod_curso', 'Cod_carrera']
    listado_carrera_cursos = obtener_lista_objetos(Carrera_cursos)
    if listado_carrera_cursos:
        for carreras_cursos in listado_carrera_cursos:
            tabla_carrera_cursos.add_row(
                [carreras_cursos.cod_carrera_curso, carreras_cursos.cod_curso, carreras_cursos.cod_carrera])
        print(tabla_carrera_cursos)