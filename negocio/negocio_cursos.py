from modelos.curso import Curso
from datos.obtener_datos import obtener_lista_objetos
from prettytable import PrettyTable
from auxiliares.normalizar_cadena import normalizar_cadena
from datos.insertar_datos import insertar_objeto
from datos.modificar_datos import modificar_objeto
from datos.eliminar_datos import eliminar_objeto
from iu.iu_curso import ingresar_nombre_curso,ingresar_cod_curso,ingresar_creditos, ingresar_pre_requisitos, ingresar_nuevo_nombre_curso, ingresar_nuevo_cod_curso, ingresar_nuevos_creditos, ingresar_nuevos_pre_requisitos


def listado_cursos():
    tabla_cursos = PrettyTable()
    tabla_cursos.field_names = ['Cod_curso', 'Nombre_Curso', 'Creditos','Pre_requisitos']
    listado_cursos = obtener_lista_objetos(Curso)
    if listado_cursos:
        for curso in listado_cursos:
            tabla_cursos.add_row(
                [curso.cod_curso, curso.nombre_curso, curso.creditos, curso.pre_requisitos])
            # print(f'{curso.cod_curso} {curso.nombre_curso} {curso.creditos},{curso.pre_requisito}')
        print(tabla_cursos)


def obtener_nombre_curso(nombre_curso):
    listado_cursos = obtener_lista_objetos(Curso)
    curso_encontrado = None
    if listado_cursos:
        for curso in listado_cursos:
            if normalizar_cadena(curso.nombre_curso) == normalizar_cadena(nombre_curso):
                curso_encontrado = curso
                break
    return curso_encontrado

def obtener_cod_curso(cod_curso):
    listado_cursos = obtener_lista_objetos(Curso)
    curso_encontrado = None
    if listado_cursos:
        for curso in listado_cursos:
            if normalizar_cadena(curso.cod_curso) == normalizar_cadena(cod_curso):
                curso_encontrado = curso
                break
    return curso_encontrado

def insertar_curso():
    curso = ingresar_nombre_curso()

    curso_encontrado = obtener_nombre_curso(curso)
    if curso_encontrado == None:
        buscar_cod_curso = ingresar_cod_curso()
        cod_curso_encontrado = obtener_cod_curso(buscar_cod_curso)
        if cod_curso_encontrado == None:
            # INSTANCIA DE CLASE
            pre_requisitos = ingresar_pre_requisitos()
            creditos = ingresar_creditos()
            nuevo_curso = Curso(nombre_curso=curso,
                                cod_curso=buscar_cod_curso  ,
                                creditos = creditos,
                                pre_requisitos = pre_requisitos,
                                habilitado=True)
            insertar_objeto(nuevo_curso)
    else:
        print('Su curso YA existe en base de datos.')

def modificar_curso():
    curso = ingresar_nombre_curso()

    curso_encontrado = obtener_nombre_curso(curso)
    if curso_encontrado:
        nuevo_nombre_curso = ingresar_nuevo_nombre_curso()
        nuevos_creditos = ingresar_nuevos_creditos()
        nuevo_pre_requisito = ingresar_nuevos_pre_requisitos()
        if nuevo_nombre_curso != '':
            curso_encontrado.nombre_curso = nuevo_nombre_curso.title()
        if nuevos_creditos != '':
            curso_encontrado.creditos = nuevos_creditos
        if nuevo_pre_requisito != '':
            curso_encontrado.pre_requisito = nuevo_pre_requisito.title()
        modificar_objeto()


def eliminado_logico_curso():
    curso = ingresar_nombre_curso()
    curso_encontrado = obtener_nombre_curso(curso)

    if curso_encontrado:
        if curso_encontrado.habilitado:
            curso_encontrado.habilitado = False
            print(f"curso '{curso_encontrado.nombre_curso}' deshabilitado correctamente.")
        else:
            curso_encontrado.habilitado = True
            print(f"curso '{curso_encontrado.nombre_curso}' habilitado correctamente.") 
    
        modificar_objeto()
    else:
        print('curso NO existe, vuelva a intentarlo.')


def eliminado_fisico_curso():
    while True:
        curso = ingresar_nombre_curso()

        curso_encontrado = obtener_nombre_curso(curso)
        if curso_encontrado:
            eliminar_objeto(curso_encontrado)
            break
        else:
            print('Curso NO existe, vuelva a intentarlo.')