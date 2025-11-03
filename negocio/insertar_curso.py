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