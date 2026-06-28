import subprocess


# Muestra los procesos activos del sistema.
def mostrar_procesos():

    print()
    print("=" * 50)
    print("             PROCESOS ACTIVOS")
    print("=" * 50)

    # Ejecuta el comando "ps -e" para obtener
    # la lista de procesos del sistema.
    resultado = subprocess.run(
        ["ps", "-e"],
        capture_output=True,
        text=True
    )

    print(resultado.stdout)
