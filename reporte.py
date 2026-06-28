import platform
import socket
import shutil
import subprocess
from datetime import datetime


# Convierte bytes a Gigabytes.
def convertir_bytes_a_gb(valor_bytes):

    return round(valor_bytes / (1024 ** 3), 2)


# Genera un reporte del sistema en un archivo de texto.
def generar_reporte():

    nombre_archivo = "reporte_sistema.txt"

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    disco = shutil.disk_usage("/")

    with open("/proc/meminfo", "r") as archivo:
        datos_memoria = archivo.readlines()

    memoria_total = int(datos_memoria[0].split()[1]) * 1024
    memoria_disponible = int(datos_memoria[2].split()[1]) * 1024
    memoria_usada = memoria_total - memoria_disponible

    procesos = subprocess.run(
        ["ps", "-e"],
        capture_output=True,
        text=True
    )

    red = subprocess.run(
        ["ip", "addr"],
        capture_output=True,
        text=True
    )

    with open(nombre_archivo, "w") as archivo:

        archivo.write("REPORTE DEL SISTEMA LINUX\n")
        archivo.write("=" * 50 + "\n")
        archivo.write(f"Fecha de generación: {fecha_actual}\n\n")

        archivo.write("INFORMACIÓN DEL SISTEMA\n")
        archivo.write("-" * 50 + "\n")
        archivo.write(f"Sistema operativo : {platform.system()}\n")
        archivo.write(f"Versión del kernel: {platform.release()}\n")
        archivo.write(f"Arquitectura      : {platform.machine()}\n")
        archivo.write(f"Nombre del equipo : {socket.gethostname()}\n\n")

        archivo.write("MEMORIA RAM\n")
        archivo.write("-" * 50 + "\n")
        archivo.write(f"RAM Total : {convertir_bytes_a_gb(memoria_total)} GB\n")
        archivo.write(f"RAM Usada : {convertir_bytes_a_gb(memoria_usada)} GB\n")
        archivo.write(f"RAM Disponible : {convertir_bytes_a_gb(memoria_disponible)} GB\n\n")

        archivo.write("ESPACIO EN DISCO\n")
        archivo.write("-" * 50 + "\n")
        archivo.write(f"Disco Total : {convertir_bytes_a_gb(disco.total)} GB\n")
        archivo.write(f"Disco Usado : {convertir_bytes_a_gb(disco.used)} GB\n")
        archivo.write(f"Disco Libre : {convertir_bytes_a_gb(disco.free)} GB\n\n")

        archivo.write("PROCESOS ACTIVOS\n")
        archivo.write("-" * 50 + "\n")
        archivo.write(procesos.stdout + "\n")

        archivo.write("INFORMACIÓN DE RED\n")
        archivo.write("-" * 50 + "\n")
        archivo.write(red.stdout + "\n")

    print()
    print("=" * 50)
    print("REPORTE GENERADO CORRECTAMENTE")
    print("=" * 50)
    print(f"Archivo creado: {nombre_archivo}")
    print("=" * 50)
