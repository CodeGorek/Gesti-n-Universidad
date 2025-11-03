def insertar_profesor():
    cod_profesor = input('Ingrese código del profesor: ')
    profesor = input('Ingrese nombre profesor: ')
    correo = input('Ingrese correo del profesor: ')
    especialidad = input('Ingrese especialidad del profesor: ')
    respuesta = obtener_lista_objetos()
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