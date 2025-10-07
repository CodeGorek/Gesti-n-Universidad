# ================================
#   Sistema de Gestión Universidad
# ================================

from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version
from modelos.carrera import Carrera
from modelos.curso import Curso
from modelos.estudiante import Estudiante
from modelos.profesor import Profesor
from modelos.recursos import Recursos
from modelos.horario import Horarios
from modelos.curso_estudiante import CursoEstudiante
from modelos.curso_profesor import CursoProfesor


# ------------------------------
#   MENÚ PRINCIPAL
# ------------------------------
def menu_principal():
    """Muestra el menú principal y retorna la opción seleccionada."""
    print(f'\n{nombre_aplicacion} v.{numero_version}')
    print('========== Bienvenido a Inacap ==========')
    print('[1] Admin')
    print('[2] Profesor')
    print('[3] Estudiante')
    print('[4] Invitado')
    print('[0] Salir')
    print('=========================================')
    opcion = input('Seleccione una opción: ')
    return opcion


# ------------------------------
#   CUENTAS DE USUARIO
# ------------------------------
def cuenta_admin():
    """Verifica el acceso del administrador."""
    print('\n=== Cuenta Admin ===')
    try:
        usuario = input('Ingrese su usuario: ')
        contrasena = input('Ingrese su contraseña: ')
        if usuario == 'admin' and contrasena == 'admin123':
            print('Acceso concedido. Bienvenido, Admin.')
            return True
        else:
            print('Acceso denegado. Usuario o contraseña incorrectos.')
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False


def cuenta_profesor():
    """Verifica el acceso del profesor."""
    print('\n=== Cuenta Profesor ===')
    try:
        usuario = input('Ingrese su usuario: ')
        contrasena = input('Ingrese su contraseña: ')
        if usuario == 'profesor' and contrasena == 'prof123':
            print('Acceso concedido. Bienvenido, Profesor.')
            return True
        else:
            print('Acceso denegado. Usuario o contraseña incorrectos.')
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False


def cuenta_estudiante():
    """Verifica el acceso del estudiante."""
    print('\n=== Cuenta Estudiante ===')
    try:
        usuario = input('Ingrese su usuario: ')
        contrasena = input('Ingrese su contraseña: ')
        if usuario == 'estudiante' and contrasena == 'est123':
            print('Acceso concedido. Bienvenido, Estudiante.')
            return True
        else:
            print('Acceso denegado. Usuario o contraseña incorrectos.')
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False


def cuenta_invitado():
    """Acceso libre para invitados."""
    print('\n👋 Acceso como Invitado. Bienvenido.')
    return True


# ------------------------------
#   SALIDA
# ------------------------------
def opcion_salir():
    print('\nSaliendo de la aplicación. Hasta luego!')
    exit(0)


# ------------------------------
#   PROGRAMA PRINCIPAL
# ------------------------------
if __name__ == "__main__":
    while True:
        opcion = menu_principal()

        if opcion == '1':
            cuenta_admin()
        elif opcion == '2':
            cuenta_profesor()
        elif opcion == '3':
            cuenta_estudiante()
        elif opcion == '4':
            cuenta_invitado()
        elif opcion == '0':
            opcion_salir()
        else:
            print('Opción inválida. Intente nuevamente.')
