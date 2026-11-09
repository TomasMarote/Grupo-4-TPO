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

# Lee el historial de ventas desde un archivo JSON.
# Devuelve el historial, si el archivo existe y si pudo leerse correctamente.
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


# Comprueba que las ventas y los IDs de los tres archivos sean coherentes.
def datos_coherentes(vehiculos, historial, siguiente_id):
    ventas_por_id = {}
    for registro in historial:
        if not registro["vendido"] or registro["id"] >= siguiente_id:
            return False
        ventas_por_id[registro["id"]] = registro["venta"]
    for vehiculo in vehiculos:
        if vehiculo["id"] >= siguiente_id:
            return False
        venta = ventas_por_id.get(vehiculo["id"])
        if vehiculo["vendido"]:
            if venta != vehiculo["venta"]:
                return False
        elif venta is not None:
            return False
    return True


# Carga todo; solo inicia vacío si faltan los tres archivos, nunca si falta uno solo.
def cargar_datos(carpeta):
    vehiculos, existe_v, valido_v = cargar_registros(os.path.join(carpeta, "vehiculos.csv"))
    # Recuperamos el historial mediante la función que lee JSON.
    historial, existe_h, valido_h = cargar_historial(
    os.path.join(carpeta, "ventas.json")
)
    siguiente_id, existe_i, valido_i = cargar_siguiente_id(os.path.join(carpeta, "siguiente_id.txt"))
    if not (valido_v and valido_h and valido_i):
        return [], [], 0, False
    if not existe_v and not existe_h and not existe_i:
        return [], [], 0, True
    if not (existe_v and existe_h and existe_i):
        print("Faltan archivos del guardado. No se iniciará con datos incompletos.")
        return [], [], 0, False
    if not datos_coherentes(vehiculos, historial, siguiente_id):
        print("Los archivos no coinciden: revise las ventas y el siguiente ID.")
        return [], [], 0, False
    return vehiculos, historial, siguiente_id, True


# Copia por líneas el guardado anterior a archivos .bak antes de reemplazarlo.
def respaldar_datos(carpeta):
    # try comprueba y copia los tres archivos; si falla, no comienza el guardado.
    try:
        for nombre in ["vehiculos.csv", "ventas.json", "siguiente_id.txt"]:
            ruta = os.path.join(carpeta, nombre)
            # try abre primero el original: si no existe, no crea un respaldo vacío.
            try:
                with open(ruta, "r", encoding="utf-8") as original:
                    with open(ruta + ".bak", "w", encoding="utf-8") as respaldo:
                        for linea in original:
                            respaldo.write(linea)
            # except omite el respaldo de un archivo que aún no se creó.
            except FileNotFoundError:
                pass
    # except informa una falla al leer o escribir la copia de seguridad.
    except (OSError, UnicodeError) as error:
        print("No se pudo completar el respaldo previo:", error)
        return False
    return True

# Guarda los vehículos en CSV, el historial en JSON y el próximo ID en TXT.
def guardar_datos(carpeta, vehiculos, historial, siguiente_id, crear_respaldo=True):

    # Si corresponde, respaldamos los archivos antes de escribir.
    if crear_respaldo and not respaldar_datos(carpeta):
        return False

    try:
        # Guardamos los vehículos como registros separados por punto y coma.
        with open(
            os.path.join(carpeta, "vehiculos.csv"),
            "w",
            encoding="utf-8"
        ) as archivo:

            # Escribimos una línea por cada vehículo.
            for vehiculo in vehiculos:
                archivo.write(convertir_a_registro(vehiculo))

        # Abrimos el archivo JSON para guardar el historial completo.
        with open(
            os.path.join(carpeta, "ventas.json"),
            "w",
            encoding="utf-8"
        ) as archivo:

            # Convertimos la lista de ventas a JSON y la escribimos.
            # indent=4 organiza el texto para facilitar su lectura.
            json.dump(historial, archivo, indent=4)

        # Guardamos el número que recibirá el próximo vehículo.
        with open(
            os.path.join(carpeta, "siguiente_id.txt"),
            "w",
            encoding="utf-8"
        ) as archivo:
            archivo.write(f"{siguiente_id}\n")

    except (OSError, UnicodeError) as error:
        # Avisamos si ocurrió un problema durante la escritura.
        print("No se completó el guardado:", error)
        print("Los archivos pueden haber quedado incompletos. No borre las copias .bak.")
        return False

    # Los tres archivos se guardaron correctamente.
    return True