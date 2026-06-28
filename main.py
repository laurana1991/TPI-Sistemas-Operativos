# Monitor Sistema Linux
# Menu

from sistema import mostrar_informacion_sistema
from memoria import mostrar_memoria_ram
from disco import mostrar_espacio_disco
from procesos import mostrar_procesos
from servicios import mostrar_estado_servicio
from red import mostrar_informacion_red
from reporte import generar_reporte

def mostrar_menu():
    #Muestra el menú principal del programa

    print()
    print("=" * 50)
    print("        MONITOR DEL SISTEMA LINUX")
    print("=" * 50)
    print("1. Información del sistema")
    print("2. Memoria RAM")
    print("3. Espacio en disco")
    print("4. Procesos activos")
    print("5. Estado de un servicio")
    print("6. Información de la red")
    print("7. Generar reporte")
    print("8. Salir")
    print("=" * 50)


def validar_opcion():
    #Valida la opción ingresada por el usuario.

    while True:

        opcion = input("Seleccione una opción: ").strip()

        # Verifica que no esté vacía
        if opcion == "":
            print("Error: Debe ingresar una opción.")

        # Verifica que sea un número
        elif not opcion.isdigit():
            print("Error: Debe ingresar un número.")

        # Verifica que esté dentro del rango permitido
        elif int(opcion) < 1 or int(opcion) > 8:
            print("Error: La opción ingresada no existe.")

        else:
            return opcion



# Programa principal


while True:

    mostrar_menu()

    opcion = validar_opcion()

    if opcion == "1":
        mostrar_informacion_sistema()
        input("Presione Enter para volver al menú...")

    elif opcion == "2":
        mostrar_memoria_ram()
        input("Presione Enter para volver al menú...")

    elif opcion == "3":
        mostrar_espacio_disco()
        input("Presione Enter para volver al menú...")

    elif opcion == "4":
        mostrar_procesos()
        input("Presione Enter para volver al menú...")

    elif opcion == "5":
        mostrar_estado_servicio()
        input("Presione Enter para volver al menú...")

    elif opcion == "6":
        mostrar_informacion_red()
        input("Presione Enter para volver al menú...")

    elif opcion == "7":
        generar_reporte()
        input("Presione Enter para volver al menú...")

    elif opcion == "8":
        print("Gracias por utilizar el Monitor del Sistema.")
        break
