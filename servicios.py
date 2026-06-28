import subprocess


# Muestra el estado de un servicio del sistema.
def mostrar_estado_servicio():

    print()
    print("=" * 50)
    print("          ESTADO DE UN SERVICIO")
    print("=" * 50)

    # Solicita al usuario el nombre del servicio.
    servicio = input("Ingrese el nombre del servicio: ").strip()

    # Verifica que el usuario haya ingresado un nombre.
    if servicio == "":
        print("\nError: Debe ingresar el nombre de un servicio.")
        return

    # Ejecuta el comando systemctl para consultar el estado.
    resultado = subprocess.run(
        ["systemctl", "is-active", servicio],
        capture_output=True,
        text=True
    )

    estado = resultado.stdout.strip()

    # Muestra el resultado.
    if estado == "active":
        print(f"\nEl servicio '{servicio}' está ACTIVO.")

    else:
        print(f"\nEl servicio '{servicio}' no está activo o no existe.")

    print("=" * 50)
