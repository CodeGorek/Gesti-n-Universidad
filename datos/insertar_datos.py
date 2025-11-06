from datos.conexion import sesion
from datos.obtener_datos import obtener_lista_objetos
from modelos.curso import Curso
from modelos.profesor import Profesor
from modelos.estudiante import Estudiante





def insertar_objeto(objeto):
    sesion.add(objeto)
    try:
        sesion.commit()
        print("El objeto se ha insertado correctamente.")
    except Exception as e:
        sesion.rollback()
        print(f"Error al insertar el objeto: {e}")
    finally:
        sesion.close()
        

def insertar_curso():
    cod_curso = input('Ingrese código del curso: ')
    curso = input('Ingrese nombre del curso: ')
    creditos = input('Ingrese créditos del curso: ')
    cod_carrera = input('Ingrese código de la carrera: ')
    pre_requisitos = input('Ingrese pre requisitos del curso: ')

    respuesta = obtener_lista_objetos(Curso)
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
    respuesta = obtener_lista_objetos(Profesor)
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