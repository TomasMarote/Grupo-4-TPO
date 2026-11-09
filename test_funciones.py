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

