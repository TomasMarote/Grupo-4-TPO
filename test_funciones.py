#test_funciones.py / Pruebas unitarias para funciones.py 
# Importamos las funciones específicas desde el archivo funciones.py para poder probarlas

from Funciones import (
    buscar_por_id,
    obtener_disponibles,
    filtrar_por_precio,
    filtrar_por_año,
    filtrar_por_combustible,
    ordenar_vehiculos,
    calcular_resumen,
    obtener_extremos,
    calcular_precio_final
) 

# ==============================================================================
# FUNCIÓN AUXILIAR DE DATOS DE PRUEBA
# ==============================================================================

def crear_vehiculos_prueba():
    # Esta función crea y devuelve una lista con 4 vehículos de prueba (3 disponibles y 1 vendido)
    # Se usa como base de datos ficticia en los tests para no modificar el archivo real
    return [
        {
            "id": 0, "marca": "Ford", "modelo": "Focus", "año": 2015,
            "kilometraje": 90000, "combustible": "Nafta", "color": "Azul",
            "precio": 10000.0, "moneda": "USD", "vendido": False
        },
        {
            "id": 1, "marca": "Toyota", "modelo": "Corolla", "año": 2020,
            "kilometraje": 20000, "combustible": "Híbrido", "color": "Blanco",
            "precio": 20000.0, "moneda": "USD", "vendido": False
        },
        {
            "id": 2, "marca": "Fiat", "modelo": "Cronos", "año": 2022,
            "kilometraje": 40000, "combustible": "Nafta", "color": "Negro",
            "precio": 9000000.0, "moneda": "ARS", "vendido": False
        },
        {
            "id": 3, "marca": "Ford", "modelo": "Fiesta", "año": 2018,
            "kilometraje": 50000, "combustible": "Nafta", "color": "Rojo",
            "precio": 5000.0, "moneda": "USD", "vendido": True,
            "venta": {"cliente": "Ana", "precio_venta": 4500.0, "moneda": "USD"}
        }
    ]

# ==============================================================================
# FUNCIONES DE PRUEBA (TESTS UNITARIOS)
# ==============================================================================

def test_buscar_por_id():
    vehiculos = crear_vehiculos_prueba()

    # La búsqueda devuelve un vehículo, no toda la lista.
    assert buscar_por_id(vehiculos, 0) == vehiculos[0]
    assert buscar_por_id(vehiculos, 2) == vehiculos[2]

    # Si el ID no existe, devuelve None.
    assert buscar_por_id(vehiculos, 99) is None
    assert buscar_por_id([], 0) is None


def test_obtener_disponibles():
    vehiculos = crear_vehiculos_prueba()
    disponibles = obtener_disponibles(vehiculos)

    # Los tres primeros vehículos están disponibles.
    assert disponibles == [vehiculos[0], vehiculos[1], vehiculos[2]]

    # El cuarto vehículo está vendido y no debe aparecer.
    assert vehiculos[3] not in disponibles
    assert obtener_disponibles([]) == []


def test_filtrar_por_precio():
    vehiculos = crear_vehiculos_prueba()

    # Debe devolver los dos vehículos disponibles en dólares.
    resultado = filtrar_por_precio(vehiculos, "USD", 5000, 20000)
    assert resultado == [vehiculos[0], vehiculos[1]]

    # Debe devolver únicamente el Fiat, cuyo precio está en pesos.
    resultado = filtrar_por_precio(
        vehiculos, "ARS", 1000000, 10000000
    )
    assert resultado == [vehiculos[2]]


def test_filtrar_por_año():
    vehiculos = crear_vehiculos_prueba()

    # El Toyota y el Fiat son del año 2020 en adelante.
    assert filtrar_por_año(vehiculos, 2020) == [
        vehiculos[1], vehiculos[2]
    ]

    # No hay vehículos de 2025 en adelante.
    assert filtrar_por_año(vehiculos, 2025) == []


def test_filtrar_por_combustible():
    vehiculos = crear_vehiculos_prueba()

    # El Ford disponible y el Fiat utilizan nafta.
    assert filtrar_por_combustible(vehiculos, "Nafta") == [
        vehiculos[0], vehiculos[2]
    ]

    # El Toyota es el único híbrido.
    assert filtrar_por_combustible(vehiculos, "Híbrido") == [
        vehiculos[1]
    ]


def test_ordenar_vehiculos():
    vehiculos = crear_vehiculos_prueba()

    # Ordenamos todos los vehículos por kilometraje ascendente.
    ordenados = ordenar_vehiculos(
        vehiculos, "kilometraje", False
    )

    assert ordenados == [
        vehiculos[1], vehiculos[2], vehiculos[3], vehiculos[0]
    ]

    # Ordenamos los vehículos en dólares por precio descendente.
    ordenados = ordenar_vehiculos(
        vehiculos, "precio", True, "USD"
    )

    assert ordenados == [
        vehiculos[1], vehiculos[0], vehiculos[3]
    ]

    # Ordenar una copia no debe modificar la lista original.
    assert vehiculos == crear_vehiculos_prueba()


def test_calcular_resumen():
    vehiculos = crear_vehiculos_prueba()

    # Hay cuatro vehículos: tres disponibles y uno vendido.
    assert calcular_resumen(vehiculos) == {
        "total": 4,
        "disponibles": 3,
        "vendidos": 1
    }


def test_obtener_extremos():
    vehiculos = crear_vehiculos_prueba()

    menor, mayor = obtener_extremos(vehiculos, "USD")

    # Comparamos vehículos disponibles de la misma moneda.
    assert menor == vehiculos[0]
    assert mayor == vehiculos[1]

    # Una lista vacía no tiene mínimo ni máximo.
    assert obtener_extremos([], "USD") == (None, None)


def test_calcular_precio_final():
    # Sin descuento.
    assert calcular_precio_final(10000, 0) == 10000.0

    # Con un descuento del 10%.
    assert calcular_precio_final(10000, 10) == 9000.0

    # Con un descuento del 100%.
    assert calcular_precio_final(10000, 100) == 0.0