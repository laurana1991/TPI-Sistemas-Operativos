import socket
import subprocess


# Muestra información básica de red del sistema.
def mostrar_informacion_red():

    print()
    print("=" * 50)
    print("            INFORMACIÓN DE LA RED")
    print("=" * 50)

    # Obtiene el nombre del equipo.
    nombre_equipo = socket.gethostname()

    # Obtiene la dirección IP asociada al equipo.
    direccion_ip = socket.gethostbyname(nombre_equipo)

    print(f"Nombre del equipo : {nombre_equipo}")
    print(f"Dirección IP      : {direccion_ip}")

    print("\nInterfaces de red:")

    # Ejecuta el comando ip addr para mostrar interfaces de red.
    resultado = subprocess.run(
        ["ip", "addr"],
        capture_output=True,
        text=True
    )

    print(resultado.stdout)

    print("=" * 50)
