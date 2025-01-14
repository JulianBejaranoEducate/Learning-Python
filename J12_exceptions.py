# Exepciones

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Ctrl + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

""" Try and Except """
number_one = 5
number_two = 6

number_two = "1"

try:
    print(number_one + number_two)
    print("No se ha prodiucido ningun error")
except:
    #Se ejecuta si se produce un error
    print("No se cumplió la condición")


""" Try, Except and Else """
try: # Intenta ejecutar el bloque de código
    print(number_one + number_two) 
    print("No se ha prodiucido ningun error")
except: # Si se produce un error, ejecuta este bloque de código
    print("No se cumplió la condición")

else: # Si no se produce un error, ejecuta este bloque de código, hace la continuación del código
    # Se ejecuta si no se produce un error
    print("La ejecución ha sido exitosa")

""" Try, Except, Else and Finally """
try: # Intenta ejecutar el bloque de código
    print(number_one + number_two) 
    print("No se ha prodiucido ningun error")
except: # Si se produce un error, ejecuta este bloque de código
    print("No se cumplió la condición")

else: # Si no se produce un error, ejecuta este bloque de código, hace la continuación del código
    # Se ejecuta si no se produce un error
    print("La ejecución ha sido exitosa")
finally:
    # Se ejecuta siempre
    print("Se ha completado la ejecución exitosamente")

""" Exepciones por tipo """
try:
    print(number_one + number_two) 
    print("No se ha prodiucido ningun error")
except ValueError:
    print("Se ha prodcuido un ValueError")
except TypeError:
    print("Se ha prodcuido un TypeError")

""" Captura de la información de la excepción """
try:
    print(number_one + number_two) 
    print("No se ha prodiucido ningun error")
except ValueError as error:
    print("error")
except Exception as error:
    print("error")


# Enunciados Ejercicios

# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero). 

# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión. 

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura. 

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores. 

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario. 

# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango. 

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError. 

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar. 

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse. 

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.