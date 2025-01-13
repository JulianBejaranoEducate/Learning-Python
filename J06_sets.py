# Sets

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

my_set = set()
# Hay dos tipos de estructuras de datos que se pueden definir de la misma manera.
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Incialmente es un diccionario

my_other_set = {"Julian", "Bejarano", 23}
# print(my_other_set[0]) # TypeError
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Python")
print(my_other_set) # un "set" no tiene una estructura definida o ordenada

my_other_set.add("Python")
print(my_other_set) # No se puede repetir elementos en un "set"

print("Julian" in my_other_set)
print("Canco" in my_other_set)

my_other_set.remove("Julian")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set # Elimina la variable
# print(my_other_set) # NameError

my_set = {"Julian", "Bejarano", 23} # Cambia el orden en el que imprime los elementos
my_list = list(my_set)
print(my_list)
print(type(my_list))
print(my_list[0])

my_other_set = {"Java", "C++", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.union(set2)
print(set1.union(set2))

# Enunciados Ejercicios

# 1. Crea un set con los números del 1 al 5 e imprímelo. 

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo. 

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede? 

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado. 

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante. 

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud. 

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista. 

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante. 

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado. 

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado. 