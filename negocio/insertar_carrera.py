from modelos.carrera import Carrera
from datos.obtener_datos import obtener_lista_objetos

def insertar_carrera():
    cod_carrera = input('Ingrese el código de la carrera: ')
    carrera = input('Ingrese el nombre de la carrera: ')
    creditos_max_semestre = input('Ingrese creditos max semetre: ')
    semestre_duracion = input('Ingrese duración en semestres: ')
    respuesta = obtener_lista_objetos(Carrera)
    if len(respuesta) > 0:
        
        nueva_carrera = Carrera(cod_carrera=cod_carrera, nombre_carrera=carrera, creditos_max_semestre=creditos_max_semestre, semestre_duracion=semestre_duracion)




