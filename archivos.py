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


