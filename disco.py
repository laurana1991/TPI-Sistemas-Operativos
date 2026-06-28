import shutil


# Convierte un valor expresado en bytes a Gigabytes.
def convertir_bytes_a_gb(valor_bytes):

    return round(valor_bytes / (1024 ** 3), 2)


# Muestra por pantalla la información del espacio en disco.
def mostrar_espacio_disco():

    print()
    print("=" * 50)
    print("              ESPACIO EN DISCO")
    print("=" * 50)

    # Obtiene la información del disco principal del sistema.
    disco = shutil.disk_usage("/")

    # Guarda los valores de almacenamiento.
    disco_total = disco.total
    disco_usado = disco.used
    disco_libre = disco.free

    # Muestra la información al usuario.
    print(f"Disco Total : {convertir_bytes_a_gb(disco_total)} GB")
    print(f"Disco Usado : {convertir_bytes_a_gb(disco_usado)} GB")
    print(f"Disco Libre : {convertir_bytes_a_gb(disco_libre)} GB")

    print("=" * 50)
