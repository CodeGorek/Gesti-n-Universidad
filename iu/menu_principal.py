#   Sistema de Gestión Universidad
from auxiliares.version import numero_version
from negocio.negocio_carreras import insertar_carrera
from negocio.negocio_cursos import modificar_curso, eliminado_logico_curso, insertar_curso, eliminado_fisico_curso, listado_cursos
from negocio.negocio_profesores import insertar_profesor, modificar_profesor, eliminado_logico_profesor, eliminado_fisico_profesor, listado_profesores
from negocio.negocio_estudiantes import insertar_estudiante, modificar_estudiante, eliminado_logico_estudiante, eliminado_fisico_estudiante, listado_estudiantes
from auxiliares.info_aplicacion import nombre_aplicacion
from negocio.negocio_estudiante_curso import ver_cursos_estudiante
from negocio.negocio_estudiante_curso import asignar_curso_a_estudiante
from negocio.negocio_carreras import modificar_carrera, eliminado_logico_carrera, eliminado_fisico_marca, listado_carreras


# #   MENÚ PRINCIPAL

def menu_principal():
#"""Muestra el menú principal y retorna la opción seleccionada."""
    print(f'\n{nombre_aplicacion} v.{numero_version}')
    print('========== Bienvenidos ==========')
    print('[1] Admin')
    print('[2] Estudiante')
    print('[0] Salir')
    print('=========================================')
    opcion = input('Seleccione una opción:').strip()
    return opcion
    
def menu_admin():
    while True:
        print("\n=== MENÚ ADMIN ===")
        print("1. Curso")
        print("2. Profesor")
        print("3. estudiante")
        print("4. Carrera")
        print("0. Salir")
        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            while True:
                print("\n--- Gestión de Cursos ---")
                print("1. Insertar curso")
                print("2. Modificar curso")
                print("3. Habilitar/Deshabilitar curso")
                print("4. Eliminar curso")
                print("5. Listado de cursos")
                print("0. Volver")
            
                sub_opcion = input("Seleccione alguna opción: ").strip()
                if sub_opcion == "1":
                    insertar_curso()
                elif sub_opcion == "2":
                    modificar_curso()
                elif sub_opcion == "3":
                    eliminado_logico_curso()
                elif sub_opcion == "4":
                    eliminado_fisico_curso()
                elif sub_opcion == "5":
                    listado_cursos()
                elif sub_opcion == "0":
                    break

        elif opcion == "2":
            while True:
                    
                print("\n--- Gestión de Profesores ---")
                print("1. Insertar profesor")
                print("2. Modificar profesor")
                print("3. Habilitar/Deshabilitar profesor")
                print("4. Eliminar profesor")
                print("5. Listado de profesores")
                print("0. Menú anterior")

                sub_opcion = input("Elija una opción: ").strip()   
                if sub_opcion == "1":
                    insertar_profesor()
                elif sub_opcion == "2":
                    modificar_profesor()
                elif sub_opcion == "3":
                    eliminado_logico_profesor()
                elif sub_opcion == "4":
                    eliminado_fisico_profesor()
                elif sub_opcion == "5":
                    listado_profesores()
                elif sub_opcion == "0":
                    break
    
        elif opcion == "3":
            while True:
                print("\n--- Gestión de Estudiantes ---")
                print("1. Insertar estudiante")
                print("2. Modificar estudiante")
                print("3. Habilitar/Deshabilitar estudiante")
                print("4. Eliminar estudiante")
                print("5. Listado de estudiantes")
                print("0. Volver al menú anterior")

                sub_opcion = input("Seleccione una opción: ").strip()
                if sub_opcion == "1":
                    insertar_estudiante()
                elif sub_opcion == "2":
                    modificar_estudiante()
                elif sub_opcion == "3":
                    eliminado_logico_estudiante()
                elif sub_opcion == "4":
                    eliminado_fisico_estudiante()
                elif sub_opcion == "5":
                    listado_estudiantes()
                elif sub_opcion == "0":
                    break
            
        elif opcion == "4":
            while True:
                print("\n--- Gestión de Carreras ---")
                print("1. Insertar carrera")
                print("2. Modificar carrera")
                print("3. Habilitar/Deshabilitar carrera")
                print("4. Eliminar carrera")
                print("5. Listado de carreras")
                print("0. Volver al menú anterior")

                sub_opcion = input("Seleccione una opción: ").strip()
                if sub_opcion == "1":
                    insertar_carrera()
                elif sub_opcion == "2": 
                    modificar_carrera()
                elif sub_opcion == "3": 
                    eliminado_logico_carrera()
                elif sub_opcion == "4": 
                    eliminado_fisico_marca()
                elif sub_opcion == "5": 
                    listado_carreras()
                elif sub_opcion == "0":
                    break
        elif opcion == "0":
            break
def menu_estudiante():
    while True:
        print("\n=== MENÚ ESTUDIANTE ===")  
        print("1. Ver cursos inscritos")
        print("2. Inscribir cursos")
        print("0. Salir") 
        opcion = input("Seleccione opción: ").strip()
        if opcion == "1":
            ver_cursos_estudiante()
        elif opcion == "2":
            asignar_curso_a_estudiante()
        elif opcion == "0":
            break   

def main():
    while True:
        opcion = menu_principal()

        if opcion == "1":
            menu_admin()
        elif opcion == "2":
            menu_estudiante()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()      

