# Condicionales
# Establecer fujos de ejecusion del codigo

my_condition = True

if my_condition:  # ==True
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor que 20 o distinto de 25")

print ("La ejecusion continua")
print("------------------------------------------------------")

my_string = ""

if not my_string:
    print("Mi cadena de texto es es vacia")

my_string = "Mi cadena de texto"

if my_string == "Mi cadena de texto":
    print("Los textos coinciden")

print("------------------------------------------------------")
# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.
print("1.")
my_num = -3
if my_num > 0:
    print("El número es positivo")
elif my_num == 0:
    print("El numero es cero")
else:
    print("El numeo es negativo")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.
print("2.")
edad_usuario = input("Ingrese su edad:")
if edad_usuario > "18":
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.
print("3.")
my_string = ""
if not my_string :
    print("Esta vacia")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
print("4.")
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
if num1 > num2:
    print("El primer numero es mayor")
elif num1 == num2:
    print("Son iguales")
else: 
    print("El sefundo numero es mayor")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.
print("5.")
num = int(input("Ingrese el número: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("El número es divisible por 3 y por 5")
else:
    print("Nooooooo")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.
print("6.")
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else: 
    print("El número es impar")
# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.
print("7.")
edad = int(input("Ingrese la edad: "))
if edad >= 18:
    print("Puede votar")
elif edad == 16 or edad == 17:
    print("Puede votar con permiso especial")
else:
    print("No puede votar")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.
print("8.")
contraseña = "1234"
contraseña_usuario = input("Ingrese la contraseña:")
if contraseña_usuario == contraseña:
    print("Correcta")
else:
    print("Incorrecta")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).
print("9.")
num = int(input("Ingrese un número: "))
if 10<= num <=20:
    print("El número esta entre 10 y 20 (ambos incluidos)")
else:
    print("NOOOOOOOOOOOOOOOOOOOOO")
# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
print("1o.")
color = input("Ingrese el color del semaforo: ")
if color == "verde":
    print("Avanza")
elif color =="amarillo":
    print("Alerta")
elif color =="rojo":
    print("Detente")
else:
    print("Color invalido")