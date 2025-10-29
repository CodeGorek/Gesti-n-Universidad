from modelos.carrera import Carrera
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable

def listado_carreras():
    tabla_carreras = PrettyTable()
    tabla_carreras.field_names = ['Cod_carrera', 'Nombre_Carrera', 'Creditos_max','Semestres']
    listado_carreras = obtener_lista_objetos(Carrera)
    if listado_carreras:
        for carrera in listado_carreras:
            tabla_carreras.add_row(
                [carrera.cod_carrera, carrera.nombre_carrera, carrera.creditos_max_semestre, carrera.semestre_duracion])
            # print(f'{carrera.cod_carrera} {carrera.descripcion} {carrera.creditos_max_semestre},{carrera.semestre_duracion}')
        print(tabla_carreras)
