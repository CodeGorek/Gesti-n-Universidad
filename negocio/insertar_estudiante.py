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