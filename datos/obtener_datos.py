from datos.conexion import sesion

def obtener_lista_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if listado_objetos:
        return listado_objetos
    





