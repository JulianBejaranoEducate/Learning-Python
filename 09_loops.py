# Loop
# Bucles - Ciclos 
print(" -------------- WHILE --------------")

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition+= 2
else:
    print("Ya ha pasado el 10 o es igual")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1 # Incrementa de uno en uno
    if my_condition==15:
        print("Se detiene en 15")
        # Detiene el bucle
        break
    print(my_condition)

print("La ejecución continua")

print(" -------------- FOR --------------")
# Se repite segun la cantidad de elementos
# Estan ordenadas
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

# No se modifican
my_tuple = ( 17, 1.59, "Malory", "Natalia", "Sapo") 
for element in my_tuple:
    print(element)

# No se repite
my_set = {"Malory", "Natalia", 17}
for element in my_set:
    print(element)

# Orden clave-Valor
my_dict= {"Nombre": "Natalia", "Apellido": "Farfan", "Edad": 17, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Edad":
        # Para el bucle en donde le indique
        break
    print("Se ejecuta")
else:
    print("Termina el for para diccionario")


for element in my_dict:
    print(element)
    if element == "Edad":
        # Para que el bucle continue, para iniciarlo de nuevo
        continue
    print("Se ejecuta")
else:
    print("Termina el for para diccionario")


for element in my_dict:
    print(element)
    if element == "Edad":
        # Para que el bucle continue, para iniciarlo de nuevo
        continue
    else: # OPCIONAL
        print("Se ejecuta")
else:
    print("Termina el for para diccionario")

print("La ejecucion continua")

print("----------------------------------------------------------")
# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.
print("1.")
num = 0
while num <= 10:
    print(num)
    num +=1
else: 
    print(" Se acabo ")

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero. 
print("2.")
my_list = [10, 20, 30, 40, 50]
for element in my_list:
    print(element)
else: 
    print(" Se acabo ")

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.
print("3.")
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".
print("4")
palabra = "Python"
for letter in palabra:
    print (letter)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.


# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.


# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.


# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.


# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].


# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

