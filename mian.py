from Funciones import * 
# =========================
# MAIN
# =========================

def main():

    vehiculos = []

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

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
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


# =========================
# INICIO DEL PROGRAMA
# =========================

if __name__ == "__main__":
    main()