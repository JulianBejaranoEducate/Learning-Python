# Condicionales / Conditionals

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

my_condition = True
my_other_condition = False

""" Para que una condiciones se ejecute, la condición debe ser verdadera "True" """

if my_other_condition:
    print("Se ejecuta la condición de if")

my_condition = 5 * 4

# Es una secuencia de condiciones que se evalúan en orden para ejecutar un bloque de código
if my_condition == 10: # Necesitan una condicion
    print("El resultado de la operación es 25")

if my_condition > 10 and my_condition < 20: # Necesitan una condicion
    print("El resultado de la operación es mayor a 10 y menor a 20", "Conditional IF")
elif my_condition == 20:  # Necesitan una condicion para cumplirse
    print("El resultado de la operacion es igual a 20", "Conditional ELIF")
else: # Si no
    print("El resultado de la operacion es menor o igual a 10 o igual que 20")

if my_other_condition:
    print("No se ejecuta la condición de if")

print("\nLa ejecución del programa continúa")


my_string = ""

if not my_string:
    print("La cadena de texto esta vacia")

if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")

# Enunciados Ejercicios

# 1. Escribe un programa que verifique si un número es positivo, negativo o cero. 

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad. 

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia. 

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad. 

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo. 

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar. 

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial. 

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error. 

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos). 

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar. 