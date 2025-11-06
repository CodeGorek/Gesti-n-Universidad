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
        

<<<<<<< HEAD
def insertar_curso():
    cod_curso = input('Ingrese código del curso: ')
    curso = input('Ingrese nombre del curso: ')
    creditos = input('Ingrese créditos del curso: ')
    cod_carrera = input('Ingrese código de la carrera: ')
    pre_requisitos = input('Ingrese pre requisitos del curso: ')

    respuesta = obtener_lista_objetos(Curso)
    if respuesta == False:
        nuevo_curso = Curso(nombre_curso=curso, cod_curso=cod_curso, creditos=creditos, cod_carrera=cod_carrera, pre_requisitos=pre_requisitos)
=======





>>>>>>> f48ecc4ae1222754bec3ef15dda8244016d1ba74


<<<<<<< HEAD
def insertar_profesor():
    cod_profesor = input('Ingrese código del profesor: ')
    profesor = input('Ingrese nombre profesor: ')
    correo = input('Ingrese correo del profesor: ')
    especialidad = input('Ingrese especialidad del profesor: ')
    respuesta = obtener_lista_objetos(Profesor)
    if respuesta == False:
        nuevo_profesor = Profesor(cod_profesor=cod_profesor, nombre_profesor=profesor, correo_profesor=correo, especialidad=especialidad)
=======
>>>>>>> f48ecc4ae1222754bec3ef15dda8244016d1ba74

