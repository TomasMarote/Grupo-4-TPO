import os
import shutil
import archivos as a


def preparar_carpeta_prueba():
    """Prepara una carpeta temporal para realizar las pruebas."""
    carpeta = "carpeta_prueba_temp"

    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)

    os.makedirs(carpeta)

    return carpeta


def borrar_carpeta_prueba(carpeta):
    """Elimina la carpeta temporal utilizada en las pruebas."""
    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)

def crear_estado():
    """Crea datos de prueba con vehículos, historial de ventas y siguiente ID."""
    vehiculos = [
        {
            "id": 0, "marca": "Ford", "modelo": "Focus", "año": 2015,
            "kilometraje": 90000, "combustible": "Nafta", "color": "Azul",
            "precio": 10000.0, "moneda": "USD", "vendido": False
        },
        {
            "id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2020,
            "kilometraje": 20000, "combustible": "Híbrido", "color": "Blanco",
            "precio": 20000.0, "moneda": "USD", "vendido": True,
            "venta": {
                "cliente": "María Pérez", "dni": "00123", "telefono": "",
                "precio_base": 20000.0, "descuento": 10.0,
                "precio_venta": 18000.0, "moneda": "USD"
            }
        }
    ]

    registro = vehiculos.copy()
    registro["venta"] = vehiculos["venta"].copy()
    historial = [registro]
    siguiente = 2

    return vehiculos, historial, siguiente


def test_primera_ejecucion():
    """Comprueba la carga inicial cuando todavía no existen archivos."""
    carpeta = preparar_carpeta_prueba()

    try:
        vehiculos, historial, siguiente_id, exito = a.cargar_datos(carpeta)

        assert exito is True
        assert vehiculos == []
        assert historial == []
        assert siguiente_id == 0

    finally:
        borrar_carpeta_prueba(carpeta)

def test_guardar_y_recuperar():
    """Comprueba que los datos puedan guardarse y recuperarse correctamente."""
    carpeta = preparar_carpeta_prueba()

    try:
        v_orig, h_orig, sig_orig = crear_estado()

        guardado_ok = a.guardar_datos(carpeta, v_orig, h_orig, sig_orig)

        assert guardado_ok is True

        vehiculos, historial, siguiente_id, exito = a.cargar_datos(carpeta)

        assert exito is True
        assert len(vehiculos) == 2
        assert len(historial) == 1
        assert siguiente_id == 2

        assert isinstance(vehiculos["id"], int)
        assert isinstance(vehiculos["precio"], float)
        assert vehiculos["vendido"] is False

        assert vehiculos["venta"]["dni"] == "00123"
        assert vehiculos["venta"]["telefono"] == ""

        assert vehiculos["venta"] is not historial["venta"]

    finally:
        borrar_carpeta_prueba(carpeta)


def test_vacios_con_contador_conservado():
    """Comprueba que se puedan guardar listas vacías conservando el siguiente ID."""
    carpeta = preparar_carpeta_prueba()

    try:
        assert a.guardar_datos(carpeta, [], [], 8) is True

        assert a.cargar_datos(carpeta) == ([], [], 8, True)

    finally:
        borrar_carpeta_prueba(carpeta)


def test_descuento_total():
    """Comprueba que se puedan guardar y recuperar ventas con descuento del 100%."""
    carpeta = preparar_carpeta_prueba()

    try:
        vehiculos, historial, siguiente = crear_estado()

        for registro in [vehiculos, historial]:
            registro["venta"]["descuento"] = 100
            registro["venta"]["precio_venta"] = 0

        assert a.guardar_datos(carpeta, [], [], 8) is True

        assert a.cargar_datos(carpeta) == (vehiculos, historial, siguiente, True)

    finally:
        borrar_carpeta_prueba(carpeta)

def test_modificacion_y_historial():
    """Comprueba que modificar los datos de un vehículo no altere el historial de ventas."""
    carpeta = preparar_carpeta_prueba()

    try:
        vehiculos, historial, siguiente = crear_estado()

        vehiculos["precio"] = 25000.0
        vehiculos["color"] = "Gris"

        assert a.guardar_datos(carpeta, [], [], 8) is True

        leidos, ventas, _, correcto = a.cargar_datos(carpeta)

        assert correcto is True
        assert leidos["precio"] == 25000.0
        assert ventas["precio"] == 20000.0
        assert ventas["color"] == "Blanco"

    finally:
        borrar_carpeta_prueba(carpeta)


def test_eliminacion_con_historial():
    """Comprueba que el historial se conserve aunque se eliminen todos los vehículos."""
    carpeta = preparar_carpeta_prueba()

    try:
        _, historial, siguiente = crear_estado()

        assert a.guardar_datos(carpeta, [], [], 8) is True

        assert a.cargar_datos(carpeta) == ([], historial, siguiente, True)

    finally:
        borrar_carpeta_prueba(carpeta)
