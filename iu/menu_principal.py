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
from modelos.estudiante_curso import EstudianteCurso
from modelos.profesor_curso import ProfesorCurso
import json
import os
import sys
import getpass
import hashlib
import binascii
import logging
from datetime import datetime

# ------------------------------
#   MENÚ PRINCIPAL
# ------------------------------
def menu_principal():
    """Muestra el menú principal y retorna la opción seleccionada."""
    print(f'\n{nombre_aplicacion} v.{numero_version}')
    print('========== Bienvenidos ==========')
    print('[1] Admin')
    print('[2] Profesor')
    print('[3] Estudiante')
    print('[4] Invitado')
    print('[0] Salir')
    print('=========================================')
    opcion = input('Seleccione una opción: ')
    return opcion




# -------------------------------
# CONFIGURACIÓN LOGGING
# -------------------------------
LOG_FILE = "registro.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# -------------------------------
# FUNCIONES DE UTILIDAD
# -------------------------------

def log_event(usuario, tipo, mensaje):
    """Registra un evento en el archivo de log."""
    logging.info(f"Usuario: {usuario} | Tipo: {tipo} | {mensaje}")

def hash_password(password):
    """Genera un hash encriptado con salt PBKDF2."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    pwdhash = hashlib.pbkdf2_hmac("sha512", password.encode("utf-8"), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode("ascii")

def verify_password(stored_password, provided_password):
    """Verifica si la contraseña ingresada coincide con el hash almacenado."""
    salt = stored_password[:64]
    stored_hash = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac("sha512", provided_password.encode("utf-8"), salt.encode("ascii"), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")
    return pwdhash == stored_hash

def cargar_datos(nombre_archivo, por_defecto):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as f:
            return json.load(f)
    else:
        return por_defecto

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

# -------------------------------
# BASE DE DATOS SIMPLIFICADA
# -------------------------------
usuarios = cargar_datos("usuarios.json", {
    "admin": {"rol": "admin", "password": hash_password("admin123")},
    "profesor": {"rol": "profesor", "password": hash_password("prof123")},
    "estudiante": {"rol": "estudiante", "password": hash_password("est123")},
    "invitado": {"rol": "invitado", "password": ""}
})

cursos = cargar_datos("cursos.json", [])
feriados = cargar_datos("feriados.json", [])

guardar_datos("usuarios.json", usuarios)

# -------------------------------
# MENÚS DE CUENTAS
# -------------------------------

def menu_admin():
    while True:
        print("\n=== MENÚ ADMIN ===")
        print("1. Ver profesores")
        print("2. Agregar profesor")
        print("3. Eliminar profesor")
        print("4. Agregar estudiante")
        print("5. Eliminar estudiante")
        print("6. Agregar curso")
        print("7. Borrar curso")
        print("8. Agregar feriado")
        print("9. Ver feriados")
        print("0. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            for u, d in usuarios.items():
                if d["rol"] == "profesor":
                    print(f"- {u}")
        elif opcion == "2":
            nombre = input("Nombre de profesor: ")
            contrasena = getpass.getpass("Contraseña: ")
            usuarios[nombre] = {"rol": "profesor", "password": hash_password(contrasena)}
            guardar_datos("usuarios.json", usuarios)
            print("Profesor agregado.")
        elif opcion == "3":
            nombre = input("Profesor a eliminar: ")
            if nombre in usuarios and usuarios[nombre]["rol"] == "profesor":
                del usuarios[nombre]
                guardar_datos("usuarios.json", usuarios)
                print("Eliminado.")
        elif opcion == "4":
            nombre = input("Nombre del estudiante: ")
            contrasena = getpass.getpass("Contraseña: ")
            usuarios[nombre] = {"rol": "estudiante", "password": hash_password(contrasena)}
            guardar_datos("usuarios.json", usuarios)
            print("Estudiante agregado.")
        elif opcion == "5":
            nombre = input("Estudiante a eliminar: ")
            if nombre in usuarios and usuarios[nombre]["rol"] == "estudiante":
                del usuarios[nombre]
                guardar_datos("usuarios.json", usuarios)
                print("Eliminado.")
        elif opcion == "6":
            nombre = input("Nombre del curso: ")
            dia = input("Día (Lunes-Viernes): ")
            turno = input("Turno (Diurno/Vespertino): ")
            cursos.append({"curso": nombre, "dia": dia, "turno": turno})
            guardar_datos("cursos.json", cursos)
            print("Curso agregado.")
        elif opcion == "7":
            nombre = input("Curso a eliminar: ")
            cursos[:] = [c for c in cursos if c["curso"] != nombre]
            guardar_datos("cursos.json", cursos)
            print("Curso eliminado.")
        elif opcion == "8":
            dia = input("Ingrese día feriado (YYYY-MM-DD): ")
            feriados.append(dia)
            guardar_datos("feriados.json", feriados)
            print("Feriado agregado.")
        elif opcion == "9":
            print("Días feriados:")
            for f in feriados:
                print(f"- {f}")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

def menu_profesor(usuario):
    print(f"\n=== MENÚ PROFESOR ({usuario}) ===")
    print("1. Ver cursos asignados (demo)")
    print("2. Ver días libres")
    print("0. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print("Cursos asignados (demo): Matemáticas, Historia")
    elif opcion == "2":
        print("Días feriados/no clases:")
        for f in feriados:
            print(f"- {f}")

def menu_estudiante(usuario):
    while True:
        print(f"\n=== MENÚ ESTUDIANTE ({usuario}) ===")
        print("1. Ver cursos disponibles")
        print("2. Tomar curso")
        print("3. Ver mis cursos")
        print("4. Ver días libres")
        print("0. Salir")
        opcion = input("Opción: ")

        user_file = f"{usuario}_cursos.json"
        mis_cursos = cargar_datos(user_file, [])

        if opcion == "1":
            for c in cursos:
                print(f"- {c['curso']} ({c['dia']}, {c['turno']})")
        elif opcion == "2":
            curso = input("Nombre del curso: ")
            if any(c["curso"] == curso for c in cursos):
                mis_cursos.append(curso)
                guardar_datos(user_file, mis_cursos)
                print("Curso agregado.")
            else:
                print("No existe ese curso.")
        elif opcion == "3":
            print("Mis cursos:")
            for c in mis_cursos:
                print(f"- {c}")
        elif opcion == "4":
            print("Días feriados/no clases:")
            for f in feriados:
                print(f"- {f}")
        elif opcion == "0":
            break

def menu_invitado():
    print("\n=== MENÚ INVITADO ===")
    print("Cursos disponibles:")
    for c in cursos:
        print(f"- {c['curso']} ({c['dia']}, {c['turno']})")

# -------------------------------
# LOGIN GENERAL
# -------------------------------
def login():
    print("\n=== INICIO DE SESIÓN ===")
    usuario = input("Usuario: ")

    if usuario not in usuarios:
        print("Usuario no existe.")
        log_event(usuario, "ERROR", "Usuario inexistente en intento de login")
        return None

    rol = usuarios[usuario]["rol"]
    password_hash = usuarios[usuario]["password"]

    intentos = 0
    while intentos < 3:
        if rol == "invitado":
            print("Acceso libre como invitado.")
            log_event(usuario, "INFO", "Ingreso como invitado")
            return usuario, rol
        contrasena = getpass.getpass("Contraseña: ")

        if verify_password(password_hash, contrasena):
            print(f"Acceso concedido. Bienvenido, {usuario}.")
            log_event(usuario, "LOGIN", "Acceso exitoso")
            return usuario, rol
        else:
            intentos += 1
            log_event(usuario, "ERROR", f"Contraseña incorrecta. Intento {intentos}/3")
            if intentos == 2:
                print("Último intento antes de bloqueo.")
            elif intentos == 3:
                print("Demasiados intentos fallidos.")
                return None

# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------
def menu_principal():
    while True:
        print("\n=== SISTEMA DE MATRÍCULA ===")
        print("1. Iniciar sesión")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            result = login()
            if result:
                usuario, rol = result
                if rol == "admin":
                    menu_admin()
                elif rol == "profesor":
                    menu_profesor(usuario)
                elif rol == "estudiante":
                    menu_estudiante(usuario)
                elif rol == "invitado":
                    menu_invitado()
        elif opcion == "0":
            print("Hasta luego.")
            sys.exit()
        else:
            print("Opción inválida.")

# -------------------------------
# EJECUCIÓN
# -------------------------------
if __name__ == "__main__":
    menu_principal()
