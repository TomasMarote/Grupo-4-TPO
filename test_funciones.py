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
    # Prueba la búsqueda de un vehículo por su ID único
    
    # 1. Cargamos la lista de vehículos de prueba
    vehiculos = crear_vehiculos_prueba()
    
    # 2. Verificamos que al buscar el ID 0 devuelva exactamente el primer vehículo de la lista
    assert buscar_por_id(vehiculos, 0) == vehiculos
    
    # 3. Verificamos que al buscar el ID 2 devuelva el tercer vehículo
    assert buscar_por_id(vehiculos, 2) == vehiculos
    
    # 4. Verificamos que buscar un ID que no existe (ej. 99) devuelva None
    assert buscar_por_id(vehiculos, 99) is None
    
    # 5. Verificamos que buscar en una lista vacía devuelva None sin romper el programa
    assert buscar_por_id([], 0) is None

def test_obtener_disponibles():
    # Prueba que se filtren únicamente los vehículos cuya clave 'vendido' sea False
    
    # 1. Cargamos la lista de prueba
    vehiculos = crear_vehiculos_prueba()
    
    # 2. Llamamos a la función para obtener los disponibles
    disponibles = obtener_disponibles(vehiculos)
    
    # 3. Verificamos que haya exactamente 3 vehículos disponibles (de los 4 totales)
    assert len(disponibles) == 3
    
    # 4. Verificamos que el vehículo vendido (el de posición) NO esté dentro de la lista resultante
    assert vehiculos not in disponibles
    
    # 5. Verificamos que al pasar una lista vacía devuelva una lista vacía
    assert obtener_disponibles([]) == []

def test_filtrar_por_precio():
    # Prueba el filtrado de vehículos por rango de precios y moneda
    
    # 1. Cargamos los vehículos de prueba
    vehiculos = crear_vehiculos_prueba()
    
    # 2. Filtramos en dólares (USD) entre $5.000 y $20.000
    res_usd = filtrar_por_precio(vehiculos, "USD", 5000, 20000)
    
    # 3. Comprobamos que trae 2 vehículos (Focus y Corolla; excluye el Fiesta por estar vendido)
    assert len(res_usd) == 2
    
    # 4. Filtramos en pesos (ARS) entre $1.000.000 y $10.000.000
    res_ars = filtrar_por_precio(vehiculos, "ARS", 1000000, 10000000)
    
    # 5. Comprobamos que trae exactamente 1 vehículo
    assert len(res_ars) == 1
    
    # 6. Confirmamos que la marca del vehículo encontrado sea "Fiat"
    assert res_ars["marca"] == "Fiat"

def test_filtrar_por_año():
    # Prueba el filtrado de vehículos a partir de un año mínimo de fabricación
    
    # 1. Cargamos los vehículos de prueba
    vehiculos = crear_vehiculos_prueba()
    
    # 2. Filtramos vehículos del año 2020 en adelante
    res = filtrar_por_año(vehiculos, 2020)
    
    # 3. Verificamos que encuentre 2 vehículos (Corolla 2020 y Cronos 2022)
    assert len(res) == 2
    
    # 4. Verificamos que buscar un año futuro sin resultados (ej. 2025) devuelva una lista vacía
    assert filtrar_por_año(vehiculos, 2025) == []

def test_filtrar_por_combustible():
    # Prueba el filtrado por tipo de combustible
    
    # 1. Cargamos los vehículos de prueba
    vehiculos = crear_vehiculos_prueba()
    
    # 2. Filtramos vehículos que usen "Nafta"
    nafta = filtrar_por_combustible(vehiculos, "Nafta")
    
    # 3. Verificamos que haya 2 vehículos disponibles a nafta (Focus y Cronos)
    assert len(nafta) == 2
    
    # 4. Filtramos vehículos que usen "Híbrido"
    hibrido = filtrar_por_combustible(vehiculos, "Híbrido")
    
    # 5. Verificamos que haya 1 vehículo disponible híbrido (Corolla)
    assert len(hibrido) == 1
