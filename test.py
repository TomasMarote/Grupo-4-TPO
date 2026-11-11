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
