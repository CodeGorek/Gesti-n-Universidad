<<<<<<< HEAD
=======
from modelos.estudiante import Estudiante
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
>>>>>>> f48ecc4ae1222754bec3ef15dda8244016d1ba74



def listado_estudiantes():
    tabla_estudiante = PrettyTable()
    tabla_estudiante.field_names = ['matricula_estudiante, nombre_estudiante, correo_estudiante, fecha_nacimiento, direccion_estudiante']
    listado_estudiantes = obtener_lista_objetos(Estudiante)
    if listado_estudiantes:
        for estudiante in listado_estudiantes:
            tabla_estudiante.add_row(
                [estudiante.matricula_estudiante, estudiante.nombre_estudiante, estudiante.correo_estudiante, estudiante.fecha_nacimiento, estudiante.direccion_estudiante])
            # print(f'{profesor.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_estudiante)
