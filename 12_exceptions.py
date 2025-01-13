# Exceptions
# Manejo de errores
numberOne = 5
numberTwo = 1
#no se suman numeros y cadenas de texto
#   numberTwo = "1"
#Try except
try:
    print(numberOne + numberTwo) 
    print("La suma es correcta")
    # Se ejecuta si se produce una excepcion
except:
    print("Error: Tipos de datos diferentes")  # Manejo de errores

#try except else
try:
    print(numberOne + numberTwo) 
    print("La suma es correcta")
except:
    print("Error: Tipos de datos diferentes")  # Manejo de errores
    #Se ejecuta si no se produce ninguna excecion
else:
    print("Continua el programa") # Si no hay errores

# try except else finally
try:
    print(numberOne + numberTwo) 
    print("La suma es correcta")
except:
    print("Error: Tipos de datos diferentes")  # Manejo de errores
    #Se ejecuta si no se produce ninguna excecion
else:
    print("Continua el programa") # Si no hay erroreS
    # Se ejecuta siempre
finally: #Opcioanl
    print("CONTINÚA")

# Excepciones por tipo

try:
    print(numberOne + numberTwo) 
    print("La suma es correcta")
    # Se ejecua solo si se produce este tipo de ERROR
except ValueError:
    print(" Error:  ValurError")
except TypeError:
    print(" Error: TypeError")

# Captura de la informacion del error

try:
    print(numberOne + numberTwo) 
    print("La suma es correcta")
    # Se ejecua solo si se produce este tipo de ERROR
except ValueError as error:
    print(error)
except Exception as my_error_random_name:
    print(my_error_random_name)


# 1. Crea una funciÃ³n que intente dividir dos nÃºmeros proporcionados por el usuario. Usa try-except para capturar cualquier error de divisiÃ³n (por ejemplo, divisiÃ³n por cero).
def division():
    try:
        numberOne = int(input("Ingrese el primer numero: "))
        numberTwo = int(input("Ingrese el segundo numero: "))
        print(numberOne / numberTwo)
    except ZeroDivisionError:
        print("Error: Division por cero")
    except ValueError:
        print("Error: Tipo de dato incorrecto")

# 2. Crea una funciÃ³n que tome una cadena e intente convertirla en un nÃºmero entero. Usa try-except para capturar cualquier error en la conversiÃ³n.
def conversion():
    try:
        number = int(input("Ingrese un numero: "))
        print(number)
    except ValueError:
        print("Error: Tipo de dato incorrecto")

# 3. Crea una funciÃ³n que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.
def OpenFile():
    try:
        file = open("file.txt", "r")
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except Exception as error:
        print(error)
    finally:
        file.close()

# 4. Crea una funciÃ³n que realice mÃºltiples operaciones (suma, resta, divisiÃ³n, multiplicaciÃ³n) con dos nÃºmeros. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.
def calculadora():
    try:
        numberOne = int(input("Ingrese el primer numero: "))
        numberTwo = int(input("Ingrese el segundo numero: "))
        print(numberOne + numberTwo)
        print(numberOne - numberTwo)
        print(numberOne * numberTwo)
        print(numberOne / numberTwo)
    except ZeroDivisionError:
        print("Error: Division por cero")
    except ValueError:
        print("Error: Tipo de dato incorrecto")
    else:
        print("Operaciones realizadas con exito")
    finally:
        print("Fin del programa") 

# 5. Crea una funciÃ³n que le pida al usuario su edad y lance un ValueError si la entrada no es un nÃºmero entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.
def edades():
    try:
        edad = int(input("Ingrse su edad: "))
        if edad <=0:
            raise ValueError("Error: Edad no valida")
        print(edad)
    except ValueError as error:
        print(error)

# 6. Crea una funciÃ³n que intente acceder a un elemento de una lista por Ã­ndice. Usa try-except para manejar el caso donde el Ã­ndice estÃ© fuera de rango.
def accede():
    try:
        Lista = [1,2,3,4,5]
        print(Lista(6))
    
    
    except IndexError:
            print("Error: Indice fuera de rango")
# 7. Crea una funciÃ³n que use try-except para manejar mÃºltiples excepciones: ZeroDivisionError, ValueError y TypeError.
def menjoErrores():
    try:
        numberOne = int(input("Ingrese el primer numero: "))
        numberTwo = int(input("Ingrese el segundo numero: "))
        print(numberOne / numberTwo)
    except ZeroDivisionError:
        print("Error: Division por cero")
    except ValueError:
        print("Error: Tipo de dato incorrecto")
    except TypeError:
        print("Error: Tipo de dato incorrecto")
        
# 8. Crea una funciÃ³n que simule una transacciÃ³n. Lanza una excepciÃ³n personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

# 9. Crea una funciÃ³n que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

# 10. Crea una funciÃ³n que calcule la raÃ­z cuadrada de un nÃºmero. Lanza un ValueError si el nÃºmero es negativo.