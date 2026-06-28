import platform
import socket


def obtener_sistema_operativo():
    return platform.system()


def obtener_version_kernel():
    return platform.release()


def obtener_arquitectura():
    return platform.machine()


def obtener_nombre_equipo():
    return socket.gethostname()


def mostrar_informacion_sistema():
    print()
    print("=" * 50)
    print("INFORMACIÓN DEL SISTEMA")
    print("=" * 50)

    print(f"Sistema operativo : {obtener_sistema_operativo()}")
    print(f"Versión del kernel: {obtener_version_kernel()}")
    print(f"Arquitectura      : {obtener_arquitectura()}")
    print(f"Nombre del equipo : {obtener_nombre_equipo()}")

    print("=" * 50)
