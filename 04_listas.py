# Listas

my_list = list()
my_other_list = []

print (len (my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print (len (my_list))

my_other_list =[17, 1.58, "Malory", "Farfan"]
print(type(my_list))
print(type(my_other_list))

# Acceder a los datos

print ("Mi edad es: ", my_other_list[0])
print (my_other_list[1])
print (my_other_list[-1])
print (my_other_list[-3])
print (my_other_list[-4])
print (my_other_list.count("Malory"))
print (my_list.count(30)) #Contar elementos de la lista 
#print (my_other_list[-5]) Error (no existe en 
#print (my_other_list[4])  lista esta posicion)
age, height, name, lastname = my_other_list
print (name)

name, height, age, lastname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
#print(my_list - my_other_list)
#Tipado dinaámico -> puede camiar mi variable

# Trabajar con elementos de la lista
# append -> Agregar elementos al final de la lista
my_other_list.append("Moredev")
print(my_other_list)
# insert -> coloca lo que le digo en la posicion dada
my_other_list.insert(1,"Lila")
print(my_other_list)
# Modificar el valor
my_other_list[1] = "Rosa"
print(my_other_list)


# remove -> Elimina el elemento dado
my_other_list.remove("Rosa")
print(my_other_list)
print("--------------------------------------")
#elimina un elemento que sabemos que esta
my_list.remove(30)
print(my_list)
# Elimina el ultimo elemento o el que se da por parametro
# Si necesitamos el elemento quitado, nos devuelve
# el elemento "desapilado"
print(my_list.pop())
print(my_list)
#toma el índice del elemento que quiero eliminar
# Así se gusrda en una variable
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)
#elimina por indice
del my_list[2]
print(my_list)

#Copar la lista y guardar en otra variable
my_new_list = my_list.copy()

#elimina la lista
my_list.clear()
print(my_list)
print(my_new_list)
#La invierte
my_new_list.reverse()
print(my_new_list)
# Ordenar la lista y se le ueden mandar criterios
my_new_list.sort()
print(my_new_list)

# Como hacer SUB listas
#Entre elemto 1y2
print(my_new_list[1:2])
print(my_new_list[1:3])

my_list = "Hola python"
print(my_list)
print(type(my_list))



#    Ejercision

# 1. Crea una lista con los nÃºmeros del 1 al 5 e imprÃ­mela.
print("1.")
my_list_uno = [1,2,3,4,5]
print(my_list)
# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
print("2.")
my_list =[10, 20, 30, 40, 50]
print(my_list)
print (my_list[2])
# 3. Agrega el nÃºmero 6 al final de la lista [1, 2, 3, 4, 5] e imprÃ­mela.
print("3.")
print(my_list_uno)
my_list_uno.append(6)
print(my_list_uno)
# 4. Inserta el nÃºmero 15 en la posiciÃ³n 2 de la lista [10, 20, 30, 40, 50].
print("4.")
print(my_list)
my_list.insert(1,15)
print(my_list)
# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
print("5.")
my_list = [10, 20, 30, 30, 40, 50]
print(my_list)
my_list.remove(30)
print(my_list)
# 6. Usa la funciÃ³n pop() para eliminar el Ãºltimo elemento de la lista [1, 2, 3, 4, 5] y almacÃ©nalo en una variable. 
# Imprime la variable y la lista.
print("6.")
my_list = [1,2,3,4,5]
my_pop_element = my_list.pop()
print(my_pop_element)
print(my_list)
# 7. Invierte la lista [100, 200, 300, 400, 500] e imprÃ­mela.
print("7.")
my_list = [100, 200, 300, 400, 500]
my_list.reverse()
print(my_list)
# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprÃ­mela.
print("8.")
my_list = [3, 1, 4, 2, 5]
my_list.sort(reverse=False)
print(my_list)
my_list.sort(reverse=True)
print(my_list)
# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
print("9.")
my_first_list =[1, 2, 3]
my_second_list =[4, 5, 6]
my_new_list = my_first_list + my_second_list
print(my_new_list)
# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posiciÃ³n 1 hasta la 3 (sin incluir la posiciÃ³n 3).
print("10.")
my_list = [10, 20, 30, 40, 50]
print(my_list[1:2])
