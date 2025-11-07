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
        









