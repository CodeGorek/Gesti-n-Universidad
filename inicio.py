from datos.conexion import Session
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

def listado_profesores():
    tabla_profesor = PrettyTable()
    tabla_profesor.field_names = ['cod_profesor, nombre_profesor, correo_profesor, especialidad']
    listado_profesores = obtener_lista_objetos()
    if listado_profesores:
        for profesor in listado_profesores:
            tabla_profesor.add_row(
                [profesor.cod_profesor, profesor.nombre_profesor, profesor.correo_profesor, profesor.especialidad])
            # print(f'{profesor.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_profesor)

def listado_estudiantes():
    tabla_estudiante = PrettyTable()
    tabla_estudiante.field_names = ['matricula_estudiante, nombre_estudiante, correo_estudiante, fecha_nacimiento, direccion_estudiante']
    listado_estudiantes = obtener_lista_objetos()
    if listado_estudiantes:
        for estudiante in listado_estudiantes:
            tabla_estudiante.add_row(
                [estudiante.matricula_estudiante, estudiante.nombre_estudiante, estudiante.correo_estudiante, estudiante.fecha_nacimiento, estudiante.direccion_estudiante])
            # print(f'{profesor.id} {marca.nombre_marca} {marca.pais_origen}')
        print(tabla_estudiante)


sesion = Session()


def insertar_carrera():
    carrera = input('Ingrese el nombre de la carrera: ')
    pais = input('Ingrese país de origen: ')

    respuesta = obtener_marca_nombre(marca)
    if respuesta == False:
        nueva_marca = Marca(nombre_marca=marca, pais_origen=pais)

        sesion.add(nueva_marca)
        try:
            sesion.commit()
            print("El objeto se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su marca YA existe en base de datos.')

def insertar_marca():
    marca = input('Ingrese nombre marca: ')
    pais = input('Ingrese país de origen: ')

    respuesta = obtener_marca_nombre(marca)
    if respuesta == False:
        nueva_marca = Marca(nombre_marca=marca, pais_origen=pais)

        sesion.add(nueva_marca)
        try:
            sesion.commit()
            print("El objeto se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su marca YA existe en base de datos.')

def insertar_marca():
    marca = input('Ingrese nombre marca: ')
    pais = input('Ingrese país de origen: ')

    respuesta = obtener_marca_nombre(marca)
    if respuesta == False:
        nueva_marca = Marca(nombre_marca=marca, pais_origen=pais)

        sesion.add(nueva_marca)
        try:
            sesion.commit()
            print("El objeto se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su marca YA existe en base de datos.')

def insertar_marca():
    marca = input('Ingrese nombre marca: ')
    pais = input('Ingrese país de origen: ')

    respuesta = obtener_marca_nombre(marca)
    if respuesta == False:
        nueva_marca = Marca(nombre_marca=marca, pais_origen=pais)

        sesion.add(nueva_marca)
        try:
            sesion.commit()
            print("El objeto se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su marca YA existe en base de datos.')


insertar_marca()