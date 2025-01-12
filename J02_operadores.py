# Operadores

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Ctrl + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea


''' Operadores aritméticos '''
print(5 + 4) # Suma
print(5 - 4) # Resta
print(5 * 4) # Multiplicación
print(5 / 4) # División
print(5 % 4) # Módulo "Resto de la división"
print(5 ** 4) # Exponenciación
print(5 // 4) # División entera "Cociente de la división" Es decir el resultado de la división sin decimales

print("Hola " + "Python") # Concatenación con el signo suma
print("Hola " + str(22)) # Concatenación
print("Hola " * 3) # Repetición con el signo multiplicación
print("Hola " * (3 **2)) # Repetición

my_float = 2.5 * 2
print("Hola " * int(my_float)) # Repetición con concatenación
print("\n")


''' Operadores de comparación '''
print(5 == 4) # Igualdad
print(5 != 4) # Diferente
print(5 > 4) # Mayor que
print(5 < 4) # Menor que
print(5 >= 4) # Mayor o igual que
print(5 <= 4) # Menor o igual que

# Ordena alfabéticamente y por valor ASCII
print("Hola" == "Python") # Igualdad
print("Hola" != "Python") # Diferente
print("aaaa" > "Aaaa") # Mayor que
print("Hola" < "Python") # Menor que
print("Hola" >= "Python") # Mayor o igual que
print("Hola" <= "Python") # Menor o igual que
print("\n")


''' Operadores lógicos '''
print(5 > 4 and "Hola" > "Python") # and
print(5 > 4 or "Hola" > "Python") # or
print(5 < 4 and "Hola" < "Python")
print(5 < 4 or "Hola" > "Python")
print(5 > 4 or ("Hola" > "Python" and 4 == 4))
print(not (5 > 4)) # not "Cambia el valor de la expresión"
print("\n")


# Enunciados Ejercicios

# 1. Realiza las siguientes operaciones aritméticas:
"""
    a. Suma: 15 + 25
    b. Resta: 50 - 22
    c. Multiplicación: 8 * 7
    d. División: 100 / 20
"""
print(15 + 25) # Suma
print(50 - 22) # Resta
print(8 * 7) # Multiplicación
print(100 / 20) # División

# 2. Calcula al resto de la división de 37 entre 5 y almacenalo en una variable "remainder". Luego, imprime el valor de la variable.
remainder = 37 % 5
print(remainder) # Módulo

# 3. Convierte el numero 7 en una cadena de texto y concatenalo con la frase " es mi número favorito". Imprime el resultado.
numero: str = str(7)
print(numero + " es mi número favorito")
print(type(numero))

print(str(7) + " es mi número favorito")

# 4. Repite la palabra "Python" 10 veces usando el operador de multiplicación para cadenas y luego imprime el resultado.
print("Python " * 10)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable boolena "resultado". Imprime el resultado.
a = 12
b = 8
resultado = a > b
print(resultado) # true

# 6. Compara dos cadenas de texto ("apple" y "banana") usando los operadores > y <, y explica cual tiene mayor orden alfabetico.
print("apple" > "banana") # False porque "apple" inici
print("apple" < "banana") # True

# 7. Realiza una comparacion logica usando "and" para verificar si el numero 10 es mayor que 5 y menor que 20. Imprime el resultado.
print(10 > 5 and 10 < 20) # True

# 8. Usa el operador "or" para verificar si el numero 7 es menor que 3 o mayor que 5. Imprime el resultado.
print(7 < 3 or 7 > 5) # True

# 9. Aplica el operador "not" para invertir el resultado de la comparacion 15 > 20. Imprime el resultado. ¿Cual es el resultado?
print(not (15 > 20)) # True

# 10. Combina operadores aritmeticos y logicos: Verifica si el numero resultante de la expresion (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
print((5 * 3) + 2 > 10 and (5 * 3) + 2 < 20) # True