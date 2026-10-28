# Entrega modificada del 40% 

def mostrar_menu():
    print("\n===== GPS AUTOMOTORES =====")
    print("1. Registrar vehículo")
    print("2. Ver vehículos disponibles")
    print("3. Buscar vehículo")
    print("4. Registrar venta")
    print("5. Ver vehículos vendidos")
    print("6. Salir")
    print("7. Modificar un vehículo")
    print("8. Eliminar un vehículo")
    print("9. Filtrar disponibles por precio")
    print("10. Filtrar disponibles por año mínimo")
    print("11. Filtrar disponibles por combustible")
    print("12. Ordenar vehículos por precio o kilometraje")
    print("13. Mostrar resumen del stock")
    print("14. Mostrar disponibles de menor y mayor precio")
    print("15. Consultar historial de ventas")
    print("16. Consultar detalle por ID")

# Funciones Atomicas / Auxiliares
#Cada vez que se usa algo de eso, se llama a las funciones atomicas 

def leer_texto(mensaje):
    valido = False 
    while not valido: 
        texto = input(mensaje).strip() 
        if texto != "": 
            valido = True 
        else:
            print("El dato no puede estar vacio")
    return texto 

#Pide un entero con un minimo y opcionalmente un maximo permitido 
def leer_entero(mensaje, minimo, maximo=None):
    valido = True 
    while not valido:
        # try, intenta convertir la entrada a un entero y comprobar su rango
        # lugar seguro / hermetico para probar una cosa 
        try :
            numero = int(input(mensaje))
            if numero < minimo: 
                print(f"El numero debe ser mayor o igual a {minimo}.")
            elif maximo is not None and numero > maximo: 
                print(f"El numero debe ser menor o igual a {maximo}.")
            else:
                valido = True 
            # except captura ValueError cuando el texto no representa un entero.
        # La bandera sigue en False y se vuelve a pedir el dato.
        except ValueError:
            print("Debe ingresar un número entero.")
    return numero

# Pide un precio positivo y finito; los decimales se ingresan con punto.
def leer_precio(mensaje):
    valido + False 
    while not valido:
        #try intenta convertir el texto a un numero decimal con float 
        try:
            precio = float(input(mensaje))
            # se excluyen infinito (inf) y valores no numericos (nan)
            if 0 < precio < float("inf"):
                valido = True 
            else:
                print ("El precio debe ser un numero positivo y finito")
        # except captura ValueError cuando el texto no puede convertirse a float.
        # Se informa el error y se repite el pedido sin finalizar el programa.
        except ValueError:
            print("Debe ingresar un número. Use punto para los decimales.")
    return precio

#Muestra un diccionario de opciones y devulee el valor elegido
def elegir_opcion(titulo, opciones):
    print(f"\n{titulo}")
    for clave, valor in opciones.items():
        print(f"{clave}. {valor}")
    valida = False
    while not valida:
        opcion = input("Seleccione una opción: ").strip()
        if opcion in opciones:
            valida = True
        else:
            print("Opción inválida.")
    return opciones[opcion]

# Muestra los datos de un vehículo y, si está vendido, los datos de la venta.
def mostrar_detalle(vehiculo):
    print("\n----------------------------------------")
    print(f"VEHÍCULO #{vehiculo['id']}")
    print(f"Marca: {vehiculo['marca']}")
    print(f"Modelo: {vehiculo['modelo']}")
    print(f"Año: {vehiculo['año']}")
    print(f"Kilometraje: {vehiculo['kilometraje']}")
    print(f"Combustible: {vehiculo['combustible']}")
    print(f"Color: {vehiculo['color']}")
    print(f"Precio: {vehiculo['moneda']} {vehiculo['precio']:.2f}")
    if vehiculo["vendido"]:
        venta = vehiculo["venta"]
        print("Estado: VENDIDO")
        print(f"Cliente: {venta['cliente']}")
        print(f"Precio de venta: {venta['moneda']} {venta['precio_venta']:.2f}")
    else:
        print("Estado: DISPONIBLE")
    print("----------------------------------------")

# 
# Solicita los datos, crea el diccionario del vehículo y lo agrega a la lista.
def registrar_vehiculo(vehiculos):
    print("\n===== REGISTRAR VEHÍCULO =====")
    marca = leer_texto("Ingrese la marca: ")
    modelo = leer_texto("Ingrese el modelo: ")
    año = leer_entero("Ingrese el año (2010 - 2026): ", 2010, 2026)
    kilometraje = leer_entero("Ingrese el kilometraje: ", 0)
    combustible = elegir_opcion("Tipo de combustible:", {
        "1": "Nafta", "2": "Diésel", "3": "Híbrido", "4": "Eléctrico"
    })
    color = leer_texto("Ingrese el color: ")
    moneda = elegir_opcion("Moneda del precio:", {"1": "ARS", "2": "USD"})
    precio = leer_precio(f"Ingrese el precio en {moneda}: ")

    # Conservamos IDs desde 0. len sirve aquí porque no se eliminan vehículos.
    vehiculo = {
        "id": len(vehiculos),
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
    vehiculos.append(vehiculo)
    print("\nVEHÍCULO REGISTRADO CORRECTAMENTE")
    mostrar_detalle(vehiculo)

    
def mostrar_por_estado(vehiculos, vendido):
    encontrado = False
    for vehiculo in vehiculos:
        if vehiculo["vendido"] == vendido:
            mostrar_detalle(vehiculo)
            encontrado = True
    return encontrado
    
# Muestra los disponibles y devuelve una bandera que indica si hay alguno.
def mostrar_vehiculos(vehiculos):
    print("\n===== VEHÍCULOS DISPONIBLES =====")
    disponibles = mostrar_por_estado(vehiculos, False)
    if not disponibles:
        print("No hay vehículos disponibles.")
    return disponibles

# Busca por ID exacto o por parte de la marca o modelo, sin distinguir mayúsculas.
def buscar_vehiculo(vehiculos):
    print("\n===== BUSCAR VEHÍCULO =====")
    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
        return
    busqueda = leer_texto("Ingrese ID, marca o modelo del vehículo: ").lower()
    encontrado = False
    for vehiculo in vehiculos:
        if (busqueda == str(vehiculo["id"])
                or busqueda in vehiculo["marca"].lower()
                or busqueda in vehiculo["modelo"].lower()):
            mostrar_detalle(vehiculo)
            encontrado = True
    if not encontrado:
        print("No se encontró ningún vehículo.")
        
def buscar_por_id(vehiculos, id_vehiculo):
    resultado = None
    encontrado = False
    posicion = 0
    while posicion < len(vehiculos) and not encontrado:
        if vehiculos[posicion]["id"] == id_vehiculo:
            resultado = vehiculos[posicion]
            encontrado = True
        else:
            posicion += 1
    return resultado

# Pide datos opcionales, calcula el descuento y guarda la venta si se confirma.
def registrar_venta(vehiculos, historial):
    print("\n===== REGISTRAR VENTA =====")
    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
        return
    disponibles = mostrar_vehiculos(vehiculos)
    if not disponibles:
        return

    id_venta = leer_entero("Ingrese el ID del vehículo vendido: ", 0)
    vehiculo = buscar_por_id(vehiculos, id_venta)
    if vehiculo is None:
        print("No existe un vehículo con ese ID.")
    elif vehiculo["vendido"]:
        print("Este vehículo ya fue vendido.")
    else:
        cliente = leer_texto("Ingrese el nombre del cliente: ")
        dni = input("DNI del cliente (Enter para omitir): ").strip()
        telefono = input("Teléfono del cliente (Enter para omitir): ").strip()
        precio_base = leer_precio(f"Ingrese el precio de venta en {vehiculo['moneda']}: ")
        descuento = leer_descuento()
        precio_venta = calcular_precio_final(precio_base, descuento)
        print(f"Precio final: {vehiculo['moneda']} {precio_venta:.2f}")
        if not confirmar("¿Confirmar la venta?"):
            print("Venta cancelada. El vehículo sigue disponible.")
            return
        # Los datos de la venta forman un diccionario dentro del vehículo.
        vehiculo["venta"] = {
            "cliente": cliente,
            "dni": dni,
            "telefono": telefono,
            "precio_base": precio_base,
            "descuento": descuento,
            "precio_venta": precio_venta,
            "moneda": vehiculo["moneda"]
        }
        vehiculo["vendido"] = True
        # Copias independientes: modificar o eliminar el vehículo no borra la venta.
        registro = vehiculo.copy()
        registro["venta"] = vehiculo["venta"].copy()
        historial.append(registro)
        print("\nVENTA REGISTRADA")
        mostrar_detalle(vehiculo)
        mostrar_detalle(vehiculo)
    
def mostrar_vendidos(vehiculos):
    print("\n===== VEHÍCULOS VENDIDOS =====")
    vendidos = mostrar_por_estado(vehiculos, True)
    if not vendidos:
        print("No hay vehículos vendidos.")

# Devuelve True para confirmar y False para cancelar; valida la respuesta.
def confirmar(mensaje):
    respuesta = elegir_opcion(mensaje, {"1": "Sí", "2": "No"})
    return respuesta == "Sí"

# Pide un porcentaje entre 0 y 100; Enter equivale a no aplicar descuento.
def leer_descuento():
    valido = False
    descuento = 0
    while not valido:
        texto = input("Descuento de 0 a 100% (Enter para omitir): ").strip()
        if texto == "":
            descuento = 0
            valido = True
        else:
            # try intenta convertir el porcentaje escrito a un decimal.
            try:
                descuento = float(texto)
                if 0 <= descuento <= 100:
                    valido = True
                else:
                    print("El descuento debe estar entre 0 y 100.")
            # except captura texto no numérico y permite volver a intentar.
            except ValueError:
                print("Debe ingresar un número. Use punto para los decimales.")
    return descuento

# calcular precio con descuento y redondear a dos decimales 
def calcular_precio_final(precio, descuento): 
    return round(precio * (1 - descuento / 100), 2)

# pide la moneda para no comparar importes de pesos con importe de dolares 
def seleccionar_moneda(): 
    return elegir_opcion("Seleccione la moenda:", {"1": "ARS", "2": "USD"})

# Solicita un ID y devuelve su vehículo, o None si no puede encontrarlo.
def solicitar_vehiculo(vehiculos):
    if len(vehiculos) == 0:
        print("No hay vehículos registrados.")
        return None
    id_vehiculo = leer_entero("Ingrese el ID del vehículo: ", 0)
    vehiculo = buscar_por_id(vehiculos, id_vehiculo)
    if vehiculo is None:
        print("No existe un vehículo con ese ID.")
    return vehiculo

# Permite actualizar únicamente precio, color, kilometraje o año (F-13).
def modificar_vehiculo(vehiculos):
    vehiculo = solicitar_vehiculo(vehiculos)
    if vehiculo is None:
        return
    mostrar_detalle(vehiculo)
    campo = elegir_opcion("Dato a modificar:", {
        "1": "precio", "2": "color", "3": "kilometraje", "4": "año"
    })
    if campo == "precio":
        nuevo = leer_precio(f"Nuevo precio en {vehiculo['moneda']}: ")
    elif campo == "color":
        nuevo = leer_texto("Nuevo color: ")
    elif campo == "kilometraje":
        nuevo = leer_entero("Nuevo kilometraje: ", 0)
    else:
        nuevo = leer_entero("Nuevo año (2010 - 2026): ", 2010, 2026)
    vehiculo[campo] = nuevo
    print("Vehículo modificado. Los datos de una venta previa no cambian.")
    mostrar_detalle(vehiculo)

    # Elimina solo el vehículo seleccionado si el usuario confirma (F-14).
def eliminar_vehiculo(vehiculos):
    vehiculo = solicitar_vehiculo(vehiculos)
    if vehiculo is None:
        return
    mostrar_detalle(vehiculo)
    if confirmar("¿Eliminar este vehículo? Su venta, si existe, queda en el historial."):
        vehiculos.remove(vehiculo)
        print("Vehículo eliminado.")
    else:
        print("Eliminación cancelada.")

# Devuelve una lista de disponibles sin modificar la lista original.
def obtener_disponibles(vehiculos):
    return [vehiculo for vehiculo in vehiculos if not vehiculo["vendido"]]


# Muestra una lista de resultados o avisa que no hay coincidencias.
def mostrar_resultados(resultados):
    if len(resultados) == 0:
        print("No hay vehículos que coincidan con la consulta.")
    else:
        for vehiculo in resultados:
            mostrar_detalle(vehiculo)

# Filtra disponibles por moneda y rango inclusivo usando filter y lambda (F-15).
def filtrar_por_precio(vehiculos, moneda, minimo, maximo):
    disponibles = obtener_disponibles(vehiculos)
    return list(filter(lambda vehiculo: vehiculo["moneda"] == moneda
                       and minimo <= vehiculo["precio"] <= maximo, disponibles))


# Solicita un rango válido de precios y muestra los resultados del filtro.
def consultar_por_precio(vehiculos):
    moneda = seleccionar_moneda()
    minimo = leer_precio("Precio mínimo (mayor que cero): ")
    valido = False
    while not valido:
        maximo = leer_precio("Precio máximo: ")
        if maximo >= minimo:
            valido = True
        else:
            print("El máximo no puede ser menor que el mínimo.")
    mostrar_resultados(filtrar_por_precio(vehiculos, moneda, minimo, maximo))
