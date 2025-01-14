# Bucles - loops

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

""" While """

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condición es menor o igual que 10")  

while my_condition <= 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que a 10")

print("\nLa ejecución del programa continúa")

while my_condition <= 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detine la ejecución del bucle")
        break
    # print("Mi condición es menor o igual que a 20") 
    print(my_condition)

print("\nLa ejecución del programa continúa")

""" For """

my_list = [10, 20, 30, 40, 50]

for element in my_list:
    print(element)

my_tuple = (23, 1.78, "Julian", "Bejarano", "Python")

for element in my_tuple:
    print(element)

my_set = {"Julian", "Bejarano", 23}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Julian", "Apellido": "Bejarano", "Edad": 23, "Pais": "Colombia"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle /for/ para diccionarios ha terminado")

for element in my_dict:
    print(element)
    if element == "Pais":
        continue
    print("Se ejecuta")
else:
    print("El bucle /for/ para diccionarios ha terminado")

print("\nLa ejecución del programa continúa")

for i in range(3):
    print(i)

my_dict = {"Nombre": "Julian", "Apellido": "Bejarano", "Edad": 23, "Pais": "Colombia"}

for element in my_dict:
    print(element)


# Enunciados Ejercicios

# 1. Usa un bucle while para imprimir los números del 1 al 10. 

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número. 

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado. 

# 4. Escribe un bucle for que imprima cada carácter de la cadena “Python”. 

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50. 

# 6. Usa un bucle for para recorrer el diccionario {“name”: “Brais”, “age”: 37, “country”: “Galicia”} e imprime las claves. 

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20. 

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso. 

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40]. 

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre “Brais”. 