from datos.conexion import sesion


def obtener_lista_objetos(modelo):
    """
    Devuelve una lista de todos los objetos de un modelo dado.
    Nunca devuelve None: si hay error o no hay datos, devuelve una lista vacía [].
    """
    try:
        objetos = sesion.query(modelo).all()
        return objetos if objetos is not None else []
    except Exception as e:
        print(f"Error al obtener objetos de {modelo.__name__}: {e}")
        return []


