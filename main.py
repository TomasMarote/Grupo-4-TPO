from Funciones import (
    mostrar_menu,
    registrar_vehiculo,
    mostrar_vehiculos,
    buscar_vehiculo,
    registrar_venta,
    mostrar_vendidos,
)


# Crea la lista y mantiene el menú activo hasta que el usuario elige salir.
def main():
    vehiculos = []
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            registrar_vehiculo(vehiculos)
        elif opcion == "2":
            mostrar_vehiculos(vehiculos)
        elif opcion == "3":
            buscar_vehiculo(vehiculos)
        elif opcion == "4":
            registrar_venta(vehiculos)
        elif opcion == "5":
            mostrar_vendidos(vehiculos)
        elif opcion == "6":
            continuar = False
            print("\nPrograma finalizado.")
        else:
            print("\nOpción inválida. Intente nuevamente.")


# Inicia el programa solo cuando se ejecuta este archivo directamente.
if __name__ == "__main__":
    main()
