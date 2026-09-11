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
def mostrar_vehiculos(vehiculos):
     print("\n========== VEHÍCULOS DISPONIBLES ==========")

    disponibles = False

    for vehiculo in vehiculos:

        if vehiculo["vendido"] == False:

            disponibles = True

            print("\n╔══════════════════════════════════════╗")
            print(f"║          VEHÍCULO #{vehiculo['id']:<15}║")
            print("╠══════════════════════════════════════╣")
            print(f"║ Marca:       {vehiculo['marca']:<20}║")
            print(f"║ Modelo:      {vehiculo['modelo']:<20}║")
            print(f"║ Año:         {vehiculo['año']:<20}║")
            print(f"║ Kilometraje: {vehiculo['kilometraje']:<20}║")
            print(f"║ Combustible: {vehiculo['combustible']:<20}║")
            print(f"║ Color:       {vehiculo['color']:<20}║")
            print(f"║ Precio:      {vehiculo['moneda']} {vehiculo['precio']:<15}║")
            print("╚══════════════════════════════════════╝")

    if disponibles == False:
        print("\nNo hay vehículos disponibles.")
        
def buscar_vehiculo(vehiculos):
    def buscar_vehiculo(vehiculos):

    print("\n========== BUSCAR VEHÍCULO ==========")

    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
        return

    busqueda = input(
        "Ingrese ID, marca o modelo del vehículo: "
    ).strip().lower()

    encontrado = False

    for vehiculo in vehiculos:

        id_vehiculo = str(vehiculo["id"])
        marca = vehiculo["marca"].lower()
        modelo = vehiculo["modelo"].lower()

        if (
            busqueda == id_vehiculo
            or busqueda in marca
            or busqueda in modelo
        ):

            encontrado = True

            print("\n╔══════════════════════════════════════╗")
            print(f"║          VEHÍCULO #{vehiculo['id']:<15}║")
            print("╠══════════════════════════════════════╣")
            print(f"║ Marca:       {vehiculo['marca']:<20}║")
            print(f"║ Modelo:      {vehiculo['modelo']:<20}║")
            print(f"║ Año:         {vehiculo['año']:<20}║")
            print(f"║ Kilometraje: {vehiculo['kilometraje']:<20}║")
            print(f"║ Combustible: {vehiculo['combustible']:<20}║")
            print(f"║ Color:       {vehiculo['color']:<20}║")
            print(f"║ Precio:      {vehiculo['moneda']} {vehiculo['precio']:<15}║")

            if vehiculo["vendido"]:
                estado = "VENDIDO"
            else:
                estado = "DISPONIBLE"

            print(f"║ Estado:      {estado:<20}║")
            print("╚══════════════════════════════════════╝")

    if encontrado == False:
        print("\nNo se encontró ningún vehículo.")


def registrar_venta(vehiculos):

    print("\n========== REGISTRAR VENTA ==========")

    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
        return

    # Mostrar vehículos disponibles
    mostrar_vehiculos(vehiculos)

    # Pedir ID del vehículo
    while True:

        try:
            id_venta = int(input("\nIngrese el ID del vehículo vendido: "))
            break

        except ValueError:
            print("El ID debe ser un número.")

    # Buscar el vehículo
    for vehiculo in vehiculos:

        if vehiculo["id"] == id_venta:

            # Verificar si ya fue vendido
            if vehiculo["vendido"]:
                print("\nEste vehículo ya fue vendido.")
                return

            print("\n--- DATOS DE LA VENTA ---")

            # Cliente
            cliente = input("Ingrese el nombre del cliente: ").strip()

            while cliente == "":
                print("El nombre no puede estar vacío.")
                cliente = input("Ingrese el nombre del cliente: ").strip()

            # Precio de venta
            while True:

                try:
                    precio_venta = float(
                        input(
                            f"Ingrese el precio de venta "
                            f"en {vehiculo['moneda']}: "
                        )
                    )

                    if precio_venta > 0:
                        break

                    print("El precio debe ser mayor a 0.")

                except ValueError:
                    print("Debe ingresar un número.")

            # Registrar la venta
            vehiculo["vendido"] = True

            vehiculo["venta"] = {
                "cliente": cliente,
                "precio_venta": precio_venta,
                "moneda": vehiculo["moneda"]
            }

            print("\n================================")
            print("       VENTA REGISTRADA")
            print("================================")
            print("ID:", vehiculo["id"])
            print("Vehículo:", vehiculo["marca"], vehiculo["modelo"])
            print("Cliente:", cliente)
            print("Precio de venta:",
                  vehiculo["moneda"], precio_venta)
            print("Estado: VENDIDO")

            return

    print("\nNo existe un vehículo con ese ID.")
