# =========================
# FUNCIONES
# =========================
import os

def mostrar_menu():
    print("\n===== GPS AUTOMOTORES =====")
    print("1. Registrar vehículo")
    print("2. Ver vehículos disponibles")
    print("3. Buscar vehículo")
    print("4. Registrar venta")
    print("5. Ver vehículos vendidos")
    print("6. Salir")

def registrar_vehiculo(vehiculos):

    print("\n===== REGISTRAR VEHÍCULO =====")

    # ID automático
    id_vehiculo = len(vehiculos) 

    # Marca
    marca = input("Ingrese la marca: ").strip()

    while marca == "":
        print("La marca no puede estar vacía.")
        marca = input("Ingrese la marca: ").strip()

    # Modelo
    modelo = input("Ingrese el modelo: ").strip()

    while modelo == "":
        print("El modelo no puede estar vacío.")
        modelo = input("Ingrese el modelo: ").strip()

    # Año
    while True:
        try:
            año = int(input("Ingrese el año (2010 - 2026): "))

            if 2010 <= año <= 2026:
                break
            else:
                print("Ingrese un año válido.")

        except ValueError:
            print("Debe ingresar un número.")

    # Kilometraje
    while True:
        try:
            kilometraje = int(input("Ingrese el kilometraje: "))

            if kilometraje >= 0:
                break
            else:
                print("El kilometraje no puede ser negativo.")

        except ValueError:
            print("Debe ingresar un número.")

    # Combustible
    print("\nTipo de combustible:")
    print("1. Nafta")
    print("2. Diésel")
    print("3. Híbrido")
    print("4. Eléctrico")

    while True:

        opcion_combustible = input("Seleccione una opción: ")

        if opcion_combustible == "1":
            combustible = "Nafta"
            break

        elif opcion_combustible == "2":
            combustible = "Diésel"
            break

        elif opcion_combustible == "3":
            combustible = "Híbrido"
            break

        elif opcion_combustible == "4":
            combustible = "Eléctrico"
            break

        else:
            print("Opción inválida.")

    # Color
    color = input("\nIngrese el color: ").strip()

    while color == "":
        print("El color no puede estar vacío.")
        color = input("Ingrese el color: ").strip()

    # Moneda
    print("\nMoneda del precio:")
    print("1. Pesos argentinos (ARS)")
    print("2. Dólares estadounidenses (USD)")

    while True:

        opcion_moneda = input("Seleccione una opción: ")

        if opcion_moneda == "1":
            moneda = "ARS"
            break

        elif opcion_moneda == "2":
            moneda = "USD"
            break

        else:
            print("Opción inválida.")

    # Precio
    while True:

        try:
            precio = float(input(f"Ingrese el precio en {moneda}: "))

            if precio > 0:
                break
            else:
                print("El precio debe ser mayor a 0.")

        except ValueError:
            print("Debe ingresar un número.")

    # Crear vehículo
    vehiculo = {
        "id": id_vehiculo,
        "marca": marca,
        "modelo": modelo,
        "año": año,
        "kilometraje": kilometraje,
        "combustible": combustible,
        "color": color,
        "precio": precio,
        "moneda": moneda,
        "vendido": False
    }

    # Agregar vehículo a la lista
    vehiculos.append(vehiculo)

    print("\n================================")
    print(" VEHÍCULO REGISTRADO CORRECTAMENTE")
    print("================================")
    print("ID:", id_vehiculo)
    print("Marca:", marca)
    print("Modelo:", modelo)
    print("Precio:", moneda, precio)