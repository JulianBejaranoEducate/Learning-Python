import subprocess

# Comando para obtener las actualizaciones instaladas
comando = ["wmic", "qfe", "list", "brief"]

# Paso 1: Ejecutar el comando para obtener las actualizaciones
try:
    resultado = subprocess.check_output(comando, text=True)  # Ejecutamos el comando y obtenemos la salida en formato texto
    print("Actualizaciones de Windows (KBs) instaladas:")
    print(resultado)  # Imprimimos las actualizaciones en la consola

    # Paso 2: Guardar el resultado en un archivo de texto
    with open("actualizaciones_instaladas.txt", "w") as archivo:
        archivo.write(resultado)  # Escribimos la salida en el archivo

    print("\nLa lista de actualizaciones instaladas se ha guardado en 'actualizaciones_instaladas.txt'.")
except subprocess.CalledProcessError as e:
    print(f"Hubo un error al ejecutar el comando: {e}")