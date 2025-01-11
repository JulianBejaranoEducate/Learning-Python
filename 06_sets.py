# sets
# Un set tiene como base un array pero en pyton no 
# hsy array si no listas directas

my_set = set()
my_other_set = {} # con los corchetes se puede dar un diccioanio tambien
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Natalia", "Farfan", 17}
print(type(my_other_set))

#Operaciones con set
print(len(my_other_set))


#comprobar que hay dentro y agregar
#Añadir datos .add
my_other_set.add("Malory")
print(my_other_set)# Un set no es una estructura ordenada

my_other_set.add("Malory")# un set no admite repetidos
print(my_other_set)


print("Malory" in my_other_set) # Nos dice si un elemento esta dentro del set
print("Malori" in my_other_set) #Respuestas bolleanas

#Eliminar elementos
my_other_set.remove("Malory")
print(my_other_set)


# Borra todos los elementos clar / 
my_other_set.clear()
# Eliminar la propiedad 
del my_other_set

#print(my_other_set(0))
#my_other_set.update().clear()

my_set = {"Natalia", "Farfan", 17}
my_list = list(my_set)
print(my_list)
print(my_list[0])
my_other_set = {"kotlin","Python","java"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_set)) # No pasara nada ya que no se repiten datos
print(my_new_set.union(my_set).union({"Rust"})) # Se pueden hacer uniones en cadena, solo agrega lo nuevo

print(my_new_set.difference(my_set))



# 1. Crea un set con los nÃºmeros del 1 al 5 e imprÃ­melo.

# 2. AÃ±ade el nÃºmero 6 al set {1, 2, 3, 4, 5} e imprÃ­melo.

# 3. Intenta aÃ±adir el nÃºmero 5 al set {1, 2, 3, 4, 5} nuevamente. Â¿QuÃ© sucede?

# 4. Verifica si el nÃºmero 3 estÃ¡ en el set {1, 2, 3, 4, 5} e imprime el resultado.

# 5. Elimina el nÃºmero 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

