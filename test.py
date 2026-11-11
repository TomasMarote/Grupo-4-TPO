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