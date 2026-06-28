# Abre el archivo del sistema donde Linux almacena
# la información de la memoria RAM.


# Convierte un valor expresado en bytes a Gigabytes.
def convertir_bytes_a_gb(valor_bytes):

    return round(valor_bytes / (1024 ** 3), 2)


# Muestra por pantalla la información de la memoria RAM.
def mostrar_memoria_ram():

    print()
    print("=" * 50)
    print("               MEMORIA RAM")
    print("=" * 50)

    # Abre el archivo del sistema donde Linux almacena
    # la información de la memoria RAM.
    with open("/proc/meminfo", "r") as archivo:

        # Guarda todas las líneas del archivo en una lista.
        datos = archivo.readlines()

    # Obtiene la memoria RAM total instalada.
    memoria_total = int(datos[0].split()[1]) * 1024

    # Obtiene la memoria RAM libre.
    memoria_libre = int(datos[1].split()[1]) * 1024

    # Obtiene la memoria RAM disponible.
    memoria_disponible = int(datos[2].split()[1]) * 1024

    # Calcula la memoria RAM utilizada.
    memoria_usada = memoria_total - memoria_disponible

    # Muestra la información al usuario.
    print(f"RAM Total      : {convertir_bytes_a_gb(memoria_total)} GB")
    print(f"RAM Usada      : {convertir_bytes_a_gb(memoria_usada)} GB")
    print(f"RAM Libre      : {convertir_bytes_a_gb(memoria_libre)} GB")
    print(f"RAM Disponible : {convertir_bytes_a_gb(memoria_disponible)} GB")

    print("=" * 50)
