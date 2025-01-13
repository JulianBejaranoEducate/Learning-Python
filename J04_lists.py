# Lists

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

# Las "listas" son una estructura de datos que permite almacenar múltiples valores en una sola variable y además, las "listas" se diferencian de los "arrays" porque pueden almacenar diferentes tipos de datos.
my_list = list()
my_other_list = []

print(len(my_list))
print(my_other_list)

my_list = [35, 24, 62, 62, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.78, "Julian", "Bejarano"]
print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
# print(my_other_list[4]) # IndexError
# print(my_other_list[-4]) # IndexError

# print(my_list.index("Julian")) # ValueError
print(my_other_list.index("Bejarano")) # Devuelve el indice de un valor en la lista

print(my_other_list.count("Julian")) # Cuenta cuantas veces se repite un valor en la lista
print(my_list.count(30))

''' Maneras de accder a los elementos de una lista '''
# No es recomendable usar este metodo
age, height, name, surname = my_other_list
print(name) # Desenpaquetado de listas

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name) # Desenpaquetado de listas

print(my_list + my_other_list) # Concatenar listas

my_other_list.append("Ness")
print(my_other_list) # Agregar un elemento al final de la lista

my_other_list.insert(2, "Azul")
print(my_other_list) # Insertar un elemento en una posición especifica

my_other_list[2] = "Dorado"

my_other_list.remove("Ness")
print(my_other_list) # Eliminar un elemento de la lista

my_list.remove(30)
print(my_list) # Eliminar un elemento de la lista

# my_list.pop()
print(my_list.pop())
print(my_list) # Eliminar el ultimo elemento de la lista

my_pop_element = my_list.pop(2)
print(my_pop_element) # Eliminar un elemento de la lista en una posición especifica
print(my_list) # Eliminar un elemento de la lista en una posición especifica

del my_list[2]
print(my_list) # Eliminar un elemento de la lista en una posición especifica

my_new_list = my_list.copy()

my_list.clear()
print(my_list) # Eliminar todos los elementos de la lista
print(my_new_list)

my_new_list.reverse()
print(my_new_list) # Invertir los elementos de la lista

my_new_list.sort()
print(my_new_list) # Ordenar los elementos de la lista

print(my_new_list[1:2])

my_list = "Hola Mundo"
print(my_list)
print(type(my_list))



# Enunciados Ejercicios

# 1. Crea una lista con los numeros del 1 al 5 e imprimela.
new_list = [1, 2, 3]
new_list.insert(1, "a")
print(new_list)


new_list = [1, 2, 3, 4, 5]
print(new_list[1:5])

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

# 3. Agrega el numero 6 al final de la lista [1, 2, 3, 4, 5] e imprimela.

# 4. Inserta el numero 15 en la posicion 2 de la lista [10, 20, 30, 40, 50] e imprimela.

# 5. Elimina el primero valor 30 de la lista [10, 20, 30, 40, 50] e imprimela.

# 6. Usa la funcion "pop()" para eliminar el ultimo elemento de la lista [1, 2, 3, 4, 5] y almacenalo en una variable. Imprime la variable y la lista.

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprimela.

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprimela.

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posicion 1 hasta la 3 (sin incluir la posicion 3) e imprimela.