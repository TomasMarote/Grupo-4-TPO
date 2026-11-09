# Manejo de archivos con las herramientas de la clase 10.
# Los CSV son texto UTF-8 sin encabezado, con campos separados por ;.
import os
import json


# Convierte un vehículo a texto; los seis campos de venta van vacíos si no se vendió.
def convertir_a_registro(vehiculo):
    registro = (f"{vehiculo['id']};{vehiculo['marca']};{vehiculo['modelo']};"
                f"{vehiculo['año']};{vehiculo['kilometraje']};{vehiculo['combustible']};"
                f"{vehiculo['color']};{vehiculo['precio']};{vehiculo['moneda']};"
                f"{vehiculo['vendido']}")
    if vehiculo["vendido"]:
        venta = vehiculo["venta"]
        registro += (f";{venta['cliente']};{venta['dni']};{venta['telefono']};"
                     f"{venta['precio_base']};{venta['descuento']};{venta['precio_venta']}")
    else:
        registro += ";;;;;;"
    return registro + "\n"


# Recupera tipos y valida los 16 campos; devuelve None si el registro es inválido.
def convertir_a_vehiculo(registro):
    datos = registro.rstrip("\r\n").split(";")
    if len(datos) != 16 or datos[9] not in ["True", "False"]:
        return None
    # try convierte los campos numéricos leídos como texto.
    try:
        vehiculo = {
            "id": int(datos[0]), "marca": datos[1], "modelo": datos[2],
            "año": int(datos[3]), "kilometraje": int(datos[4]),
            "combustible": datos[5], "color": datos[6], "precio": float(datos[7]),
            "moneda": datos[8], "vendido": datos[9] == "True"
        }
        if (vehiculo["id"] < 0 or not 2010 <= vehiculo["año"] <= 2026
                or vehiculo["kilometraje"] < 0
                or not 0 < vehiculo["precio"] < float("inf")
                or vehiculo["moneda"] not in ["ARS", "USD"]
                or vehiculo["combustible"] not in ["Nafta", "Diésel", "Híbrido", "Eléctrico"]):
            return None
        for campo in ["marca", "modelo", "color"]:
            if vehiculo[campo].strip() == "":
                return None
        if vehiculo["vendido"]:
            venta = {
                "cliente": datos[10], "dni": datos[11], "telefono": datos[12],
                "precio_base": float(datos[13]), "descuento": float(datos[14]),
                "precio_venta": float(datos[15]), "moneda": vehiculo["moneda"]
            }
            if (venta["cliente"].strip() == ""
                    or not 0 < venta["precio_base"] < float("inf")
                    or not 0 <= venta["descuento"] <= 100
                    or not 0 <= venta["precio_venta"] < float("inf")
                    or venta["precio_venta"] != round(venta["precio_base"] * (1 - venta["descuento"] / 100), 2)):
                return None
            vehiculo["venta"] = venta
        elif datos[10:] != ["", "", "", "", "", ""]:
            return None
    # except rechaza números mal escritos, sin tratarlos como un archivo vacío.
    except ValueError:
        return None
    return vehiculo

# Lee un CSV por líneas; devuelve registros, si existe y si pudo leerse bien.
def cargar_registros(ruta):
    registros = []
    ids = []
    # try intenta abrir el archivo y leer sus registros.
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            numero_linea = 0
            for linea in archivo:
                numero_linea += 1
                vehiculo = convertir_a_vehiculo(linea)
                if vehiculo is None or vehiculo["id"] in ids:
                    print(f"Datos inválidos o ID repetido en {ruta}, línea {numero_linea}.")
                    return [], True, False
                registros.append(vehiculo)
                ids.append(vehiculo["id"])
    # except distingue un archivo inexistente de uno dañado o inaccesible.
    except FileNotFoundError:
        return [], False, True
    # except informa errores de acceso o texto que no se puede leer como UTF-8.
    except (OSError, UnicodeError) as error:
        print(f"No se pudo leer {ruta}: {error}")
        return [], True, False
    return registros, True, True

<<<<<<< HEAD


=======
# Lee el historial de ventas desde un archivo JSON.
# Devuelve el historial, si el archivo existe y si pudo leerse correctamente.
>>>>>>> f52d018e8c8d192ff6845bfbefc5649841ad66a3
def cargar_historial(ruta):
    try:
        # Abrimos el archivo para lectura.
        with open(ruta, "r", encoding="utf-8") as archivo:

            # Recuperamos la lista de ventas guardada en JSON.
            historial = json.load(archivo)

        # El historial del programa debe ser una lista.
        if type(historial) != list:
            print("El historial debe contener una lista.")
            return [], True, False

        # Guardamos los IDs encontrados para detectar ventas repetidas.
        ids = []

        # Revisamos cada venta recuperada.
        for registro in historial:

            # Reutilizamos las funciones que ya validan los datos del vehículo.
            vehiculo = convertir_a_vehiculo(
                convertir_a_registro(registro)
            )

            # Rechazamos datos inválidos, vehículos sin vender o IDs repetidos.
            if (vehiculo is None
                    or not vehiculo["vendido"]
                    or vehiculo["id"] in ids):
                print("El historial contiene una venta inválida o un ID repetido.")
                return [], True, False

            # Recordamos el ID para comprobar los siguientes registros.
            ids.append(vehiculo["id"])

    except FileNotFoundError:
        # El archivo todavía no existe.
        return [], False, True

    except Exception as error:
        # Informamos errores de lectura, de JSON o de los datos guardados.
        print(f"No se pudo leer {ruta}: {error}")
        return [], True, False

    # El archivo existe y el historial se recuperó correctamente.
    return historial, True, True

<<<<<<< HEAD

=======
>>>>>>> f52d018e8c8d192ff6845bfbefc5649841ad66a3
# Lee el próximo ID: el archivo debe contener una única línea con un entero.
def cargar_siguiente_id(ruta):
    cantidad = 0
    siguiente_id = 0
    # try abre el archivo, recorre sus líneas y convierte el número.
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                cantidad += 1
                siguiente_id = int(linea.strip())
        if cantidad != 1 or siguiente_id < 0:
            print("El archivo del siguiente ID tiene un formato inválido.")
            return 0, True, False
    # except permite reconocer la primera ejecución, cuando aún no hay archivos.
    except FileNotFoundError:
        return 0, False, True
    # except informa problemas de lectura, codificación o conversión a entero.
    except (OSError, ValueError) as error:
        print(f"No se pudo leer {ruta}: {error}")
        return 0, True, False
    return siguiente_id, True, True

