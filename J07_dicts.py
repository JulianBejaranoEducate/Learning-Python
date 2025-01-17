# Diccionarios

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Claves y valores
my_other_dict = {"Nombre": "Julian", "Apellido": "Garcia", "Edad": 23, 1: "Python"}

my_dict = {"Nombre": "Julian", "Apellido": "Garcia", "Edad": 23, "Lenguajes": {"Python", "Java", "C++"}, 1: 1.78}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Francisco"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Address"] = "Nueva Castilla"
print(my_dict)

del my_dict["Address"]
print(my_dict)

print("Francisco" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get("Nombre")) # Si no existe la clave, devuelve None

my_list = ["Nombre", 1, "Piso"]

my_new_dict = my_other_dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso", "Color")) # Se crea un diccionario con las claves de la tupla y valores None
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Julian") # Se asigna a todas las claves el valor "Julian"
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ("Julian", "Bejarano")) # Se asigna a todas las claves el valor de la tupla
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ["Julian", "Bejarano"]) # Se asigna a todas las claves la misma lista
print(my_new_dict)

print(list(my_new_dict)) # Se convierten las claves en una lista
print(list(my_new_dict.keys()))
print(list(my_new_dict.values()))

print(tuple(my_new_dict)) # Se convierten las claves en una tupla
print(set(my_new_dict)) # Se convierten las claves en un conjunto


# Enunciados Ejercicios

# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario. 

# 2. Accede al valor de la clave name en el diccionario. 

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado. 

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado. 

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante. 

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...). 

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}. 

# 8. Imprime solo las claves del diccionario. 

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante. 

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido". 

new_dict = {"Julian": 23, "Francisco": 24, "Jeisson": 25, "Steven": 29}
print(new_dict)