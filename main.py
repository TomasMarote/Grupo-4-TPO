import os
from archivos import cargar_datos, guardar_datos
from Funciones import (
    mostrar_menu,
    registrar_vehiculo,
    mostrar_vehiculos,
    buscar_vehiculo,
    registrar_venta,
    mostrar_vendidos,
    modificar_vehiculo,
    eliminar_vehiculo,
    consultar_por_precio,
    consultar_por_año,
    consultar_por_combustible,
    consultar_ordenados,
    mostrar_resumen,
    mostrar_extremos,
    mostrar_historial,
    consultar_detalle,
    confirmar,
)

# Intenta guardar y permite reintentar si ocurre un error.
def guardar_con_reintento(carpeta, vehiculos, historial, siguiente_id):
    # Realizamos el primer intento de guardado.
    guardado = guardar_datos(carpeta, vehiculos, historial, siguiente_id)
    reintentar = True

    # Repetimos mientras falle el guardado y el usuario quiera reintentar.
    while not guardado and reintentar:
        print("Los cambios siguen en memoria, pero no se guardaron.")

        reintentar = confirmar(
            "¿Reintentar guardar? No = cerrar con cambios sin guardar."
        )

        if reintentar:
            # Volvemos a guardar los datos que siguen en memoria.
            guardado = guardar_datos(
                carpeta, vehiculos, historial, siguiente_id
            )

    # Informamos el resultado final.
    if guardado:
        print("Datos guardados correctamente.")
    else:
        print("Programa cerrado con cambios SIN GUARDAR.")

    return guardado

# Carga los archivos, ejecuta el menú y guarda después de cada operación de cambio.
def main(carpeta=None):
    if carpeta is None:
        carpeta = os.path.dirname(__file__)

    vehiculos, historial, siguiente_id, carga_correcta = cargar_datos(carpeta)

    if not carga_correcta:
        print("No se pudieron cargar los datos. Revise el error indicado.")
        return

    continuar = True
    print("Los datos se cargan y guardan en la carpeta del programa.")

    while continuar:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            siguiente_id = registrar_vehiculo(vehiculos, siguiente_id)
        elif opcion == "2":
            mostrar_vehiculos(vehiculos)
        elif opcion == "3":
            buscar_vehiculo(vehiculos)
        elif opcion == "4":
            registrar_venta(vehiculos, historial)
        elif opcion == "5":
            mostrar_vendidos(vehiculos)
        elif opcion == "6":
            continuar = False
        elif opcion == "7":
            modificar_vehiculo(vehiculos)
        elif opcion == "8":
            eliminar_vehiculo(vehiculos)
        elif opcion == "9":
            consultar_por_precio(vehiculos)
        elif opcion == "10":
            consultar_por_año(vehiculos)
        elif opcion == "11":
            consultar_por_combustible(vehiculos)
        elif opcion == "12":
            consultar_ordenados(vehiculos)
        elif opcion == "13":
            mostrar_resumen(vehiculos)
        elif opcion == "14":
            mostrar_extremos(vehiculos)
        elif opcion == "15":
            mostrar_historial(historial)
        elif opcion == "16":
            consultar_detalle(vehiculos)
        else:
            print("\nOpción inválida. Intente nuevamente.")
        # También guardar al salir crea los archivos de una primera ejecución vacía.
        if opcion in ["1", "4", "7", "8", "6"]:
            guardado = guardar_con_reintento(carpeta, vehiculos, historial, siguiente_id)
            if not guardado:
                continuar = False
            elif opcion == "6":
                print("\nPrograma finalizado.")


# Inicia el programa solo cuando se ejecuta este archivo directamente.
if __name__ == "__main__":
    main()
