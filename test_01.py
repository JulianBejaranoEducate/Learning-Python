import subprocess

# Paso 1: Ejecutar el comando 'winget list' en la terminal de Windows
comando = ["winget", "list"]  # Comando para obtener los programas instalados

# Paso 2: Ejecutar el comando y obtener el resultado
try:
    resultado = subprocess.check_output(comando, text=True)  # Ejecutamos el comando y obtenemos la salida en formato texto
    print("Programas instalados en tu PC:")
    print(resultado)  # Imprimimos los programas en la consola

    # Paso 3: Guardar el resultado en un archivo de texto
    with open("programas_instalados.txt", "w") as archivo:
        archivo.write(resultado)  # Escribimos la salida en el archivo

    print("\nLa lista de programas se ha guardado en 'programas_instalados.txt'.")
except subprocess.CalledProcessError as e:
    print(f"Hubo un error al ejecutar el comando: {e}")
