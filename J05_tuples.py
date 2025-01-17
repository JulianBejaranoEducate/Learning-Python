# Tuplas

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

my_tupla = tuple()
my_other_tupla = ()

my_tupla = (23, 1.78, "Julian", "Bejarano", "Julian")
my_other_tupla = (35, 60, 30)

print(my_tupla)
print(type(my_tupla))

print(my_tupla[0])
print(my_tupla[-1])
# print(my_tupla[5]) # IndexError
# print(my_tupla[-4]) # IndexError

print(my_tupla.count("Julian")) # Cuenta cuantas veces se repite un valor en la tupla
print(my_tupla.index("Bejarano")) # Devuelve el indice de un valor en la tupla
print(my_tupla.index("Julian")) # Devuelve el indice de un valor en la tupla 

# my_tupla[1] = 1.80

my_sum_tupla = my_tupla + my_other_tupla
print(my_sum_tupla)

print(my_sum_tupla[3:6])

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla[4] = "Ness"
my_tupla.insert(1, "Dorado")
my_tupla = tuple(my_tupla)
print(my_tupla)
print(type(my_tupla))

del my_tupla


# Enunciado Ejercicios

# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprimela.

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muestralo.

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado. 

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante. 

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante. 

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado. 

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento. 

my_new_tupla = ("Santa Marta", "Barranquilla", "Cartagena", "Medellin", "Bogota")
print(my_new_tupla)