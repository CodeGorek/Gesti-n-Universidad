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
    cod_carrera = input('Ingrese el código de la carrera: ')
    carrera = input('Ingrese el nombre de la carrera: ')
    creditos_max_semestre = input('Ingrese creditos max semetre: ')
    semestre_duracion = input('Ingrese duración en semestres: ')
    respuesta = obtener_lista_objetos()
    if respuesta == False:
        nueva_carrera = Carrera(cod_carrera=cod_carrera, nombre_carrera=carrera, creditos_max_semestre=creditos_max_semestre, semestre_duracion=semestre_duracion)

        sesion.add(nueva_carrera)
        try:
            sesion.commit()
            print("El objeto(carrera) se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su carrera ya existe en base de datos.')

def insertar_curso():
    cod_curso = input('Ingrese código del curso: ')
    curso = input('Ingrese nombre del curso: ')
    creditos = input('Ingrese créditos del curso: ')
    cod_carrera = input('Ingrese código de la carrera: ')
    pre_requisitos = input('Ingrese pre requisitos del curso: ')

    respuesta = obtener_lista_objetos()
    if respuesta == False:
        nuevo_curso = Curso(nombre_curso=curso, cod_curso=cod_curso, creditos=creditos, cod_carrera=cod_carrera, pre_requisitos=pre_requisitos)

        sesion.add(nuevo_curso)
        try:
            sesion.commit()
            print("El objeto(curso) se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su curso ya existe en base de datos.')

def insertar_profesor():
    cod_profesor = input('Ingrese código del profesor: ')
    profesor = input('Ingrese nombre profesor: ')
    correo = input('Ingrese correo del profesor: ')
    especialidad = input('Ingrese especialidad del profesor: ')
    respuesta = obtener_lista_objetos()
    if respuesta == False:
        nuevo_profesor = Profesor(cod_profesor=cod_profesor, nombre_profesor=profesor, correo_profesor=correo, especialidad=especialidad)

        sesion.add(nuevo_profesor)
        try:
            sesion.commit()
            print("El objeto (profesor) se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su profesor ya existe en base de datos.')

def insertar_estudiante():
    matricula_estudiante = input('Ingrese matrícula del estudiante: ')
    estudiante = input('Ingrese nombre estudiante: ')
    correo = input('Ingrese correo del estudiante: ')
    fecha_nacimiento = input('Ingrese fecha de nacimiento del estudiante (YYYY-MM-DD): ')
    direccion = input('Ingrese dirección del estudiante: ')
    respuesta = obtener_lista_objetos()
    if respuesta == False:
        nuevo_estudiante = Estudiante(matricula_estudiante=matricula_estudiante, nombre_estudiante=estudiante, correo_estudiante=correo, fecha_nacimiento=fecha_nacimiento, direccion_estudiante=direccion)

        sesion.add(nuevo_estudiante)
        try:
            sesion.commit()
            print("El objeto (estudiante) se ha insertado correctamente.")
        except Exception as e:
            sesion.rollback()
            print(f"Error al insertar el objeto: {e}")
        finally:
            sesion.close()
    else:
        print('Su marca YA existe en base de datos.')


