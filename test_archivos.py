import os
import archivos as a


# Usamos una carpeta exclusiva para los datos ficticios.
# Debe crearse manualmente junto a los archivos Python.
CARPETA = os.path.join(
    os.path.dirname(__file__), "carpeta_pruebas"
)


def crear_estado():
    # Creamos un vehículo disponible y otro vendido.
    vehiculos = [
        {
            "id": 0,
            "marca": "Ford",
            "modelo": "Focus",
            "año": 2015,
            "kilometraje": 90000,
            "combustible": "Nafta",
            "color": "Azul",
            "precio": 10000.0,
            "moneda": "USD",
            "vendido": False
        },
        {
            "id": 1,
            "marca": "Toyota",
            "modelo": "Corolla",
            "año": 2020,
            "kilometraje": 20000,
            "combustible": "Híbrido",
            "color": "Blanco",
            "precio": 20000.0,
            "moneda": "USD",
            "vendido": True,
            "venta": {
                "cliente": "María Pérez",
                "dni": "00123",
                "telefono": "",
                "precio_base": 20000.0,
                "descuento": 10.0,
                "precio_venta": 18000.0,
                "moneda": "USD"
            }
        }
    ]

    # Creamos otro diccionario para el historial.
    # Copiamos los campos del vehículo vendido mediante un for.
    registro = {}

    for clave, valor in vehiculos[1].items():
        if clave != "venta":
            registro[clave] = valor

    # La venta también necesita un diccionario independiente.
    registro["venta"] = {}

    for clave, valor in vehiculos[1]["venta"].items():
        registro["venta"][clave] = valor

    historial = [registro]
    siguiente_id = 2

    return vehiculos, historial, siguiente_id


def test_primera_ejecucion():
    # Consultamos una ruta donde no existen archivos.
    # No hay que crear ni guardar datos en "sin_archivos".
    ruta = os.path.join(CARPETA, "sin_archivos")

    # Debe iniciar sin vehículos, sin ventas y con ID inicial 0.
    assert a.cargar_datos(ruta) == ([], [], 0, True)


def test_guardar_y_recuperar():
    vehiculos, historial, siguiente = crear_estado()

    # Guardamos los datos ficticios.
    assert a.guardar_datos(
        CARPETA, vehiculos, historial, siguiente
    ) is True

    # Recuperamos lo que acabamos de guardar.
    leidos, ventas, contador, correcto = a.cargar_datos(CARPETA)

    assert correcto is True
    assert leidos == vehiculos
    assert ventas == historial
    assert contador == siguiente

    # Verificamos que los números conserven sus tipos.
    assert isinstance(leidos[0]["id"], int)
    assert isinstance(leidos[0]["precio"], float)
    assert leidos[0]["vendido"] is False

    # El DNI conserva sus ceros iniciales y el teléfono vacío.
    assert leidos[1]["venta"]["dni"] == "00123"
    assert leidos[1]["venta"]["telefono"] == ""

    # Cambiar una venta leída no debe modificar el historial.
    leidos[1]["venta"]["cliente"] = "Otro cliente"
    assert ventas[0]["venta"]["cliente"] == "María Pérez"


def test_vacios_con_contador_conservado():
    # Aunque no haya vehículos ni ventas, conservamos el contador.
    assert a.guardar_datos(CARPETA, [], [], 8) is True

    assert a.cargar_datos(CARPETA) == ([], [], 8, True)


def test_descuento_total():
    vehiculos, historial, siguiente = crear_estado()

    # Aplicamos el descuento al vehículo vendido y al historial.
    for registro in [vehiculos[1], historial[0]]:
        registro["venta"]["descuento"] = 100
        registro["venta"]["precio_venta"] = 0

    # Guardamos los datos modificados, no listas vacías.
    assert a.guardar_datos(
        CARPETA, vehiculos, historial, siguiente
    ) is True

    assert a.cargar_datos(CARPETA) == (
        vehiculos, historial, siguiente, True
    )


def test_modificacion_y_historial():
    vehiculos, historial, siguiente = crear_estado()

    # Modificamos el vehículo, pero no su registro histórico.
    vehiculos[1]["precio"] = 25000.0
    vehiculos[1]["color"] = "Gris"

    assert a.guardar_datos(
        CARPETA, vehiculos, historial, siguiente
    ) is True

    leidos, ventas, contador, correcto = a.cargar_datos(CARPETA)

    assert correcto is True
    assert contador == siguiente

    # El vehículo conserva los datos nuevos.
    assert leidos[1]["precio"] == 25000.0
    assert leidos[1]["color"] == "Gris"

    # El historial conserva los datos anteriores.
    assert ventas[0]["precio"] == 20000.0
    assert ventas[0]["color"] == "Blanco"


def test_eliminacion_con_historial():
    vehiculos, historial, siguiente = crear_estado()

    # Simulamos eliminar todos los vehículos.
    # El historial y el contador deben conservarse.
    assert a.guardar_datos(
        CARPETA, [], historial, siguiente
    ) is True

    assert a.cargar_datos(CARPETA) == (
        [], historial, siguiente, True
    )