# Entrega modificada del 40% 

def mostrar_menu():
    print("\n===== GPS AUTOMOTORES =====")
    print("1. Registrar vehículo")
    print("2. Ver vehículos disponibles")
    print("3. Buscar vehículo")
    print("4. Registrar venta")
    print("5. Ver vehículos vendidos")
    print("6. Salir")

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

# Registra el cliente y el precio de venta, y cambia el estado a vendido.
def registrar_venta(vehiculos):
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
        precio_venta = leer_precio(f"Ingrese el precio de venta en {vehiculo['moneda']}: ")
        # Los datos de la venta forman un diccionario dentro del vehículo.
        vehiculo["venta"] = {
            "cliente": cliente,
            "precio_venta": precio_venta,
            "moneda": vehiculo["moneda"]
        }
        vehiculo["vendido"] = True
        print("\nVENTA REGISTRADA")
        mostrar_detalle(vehiculo)
    
def mostrar_vendidos(vehiculos):
    print("\n===== VEHÍCULOS VENDIDOS =====")
    vendidos = mostrar_por_estado(vehiculos, True)
    if not vendidos:
        print("No hay vehículos vendidos.")