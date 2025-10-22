from iu.menu_principal import menu_principal
from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version
from modelos.profesor import Profesor
from modelos.estudiante import Estudiante
from modelos.carrera import Carrera
from modelos.curso import Curso
from modelos.estudiante_curso import EstudianteCurso
from modelos.profesor_curso import ProfesorCurso
# ------------------------------
#   INICIO DE LA APLICACIÓN
# ------------------------------

from modelos.carrera import Carrera
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
from modelos.carrera import Carrera


def listado_carreras():
    tabla_carreras = PrettyTable()
    tabla_carreras.field_names = ['Cod_carrera', 'Descripcion', 'Creditos_max','Semestres']
    listado_carreras = obtener_lista_objetos()
    if listado_carreras:
        for carrera in listado_carreras:
            tabla_carreras.add_row(
                [carrera.cod_carrera, carrera.descripcion, carrera.creditos_max_semestre, carrera.semestre_duracion])
            # print(f'{carrera.cod_carrera} {carrera.descripcion} {carrera.creditos_max_semestre},{carrera.semestre_duracion}')
        print(tabla_carreras)

listado_carreras()