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