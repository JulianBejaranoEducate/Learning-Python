# Diccionarios

my_dict = dict ()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))
#Relacion de CLAVE-VALOR
my_other_dict= {"Nombre": "Natalia", "Apellido": "Farfan", "edad": 17, 1:"Python"}

my_dict = {
    "Nombre": "Natalia", 
    "Apellido": "Farfan", 
    "edad": 17,
    "Lenguajes": ("Python", "Java", "Rust"), #clave:str y valor: set
    1: 1.59
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
#Modificar un espacio del diccionario llamando su clave
print(my_dict["Nombre"])
my_dict["Nombre"] = "Malory"
print(my_dict["Nombre"])
#CONSULTA
print(my_dict[1])
# Agregar un espacio al diccionario
my_dict["Calle"] = "Calle Nata"
print(my_dict)

#Operaciones
#Eliminar un elemento en diccionario
del my_dict["Calle"]
print(my_dict)

# Busca si esta en el diccionario por el campo clave
print("Malory" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_list =["Nombre", 1, "Piso"]

#Nuevo diccionario sin valores
print("-------------------------------------------------------")
my_new_dict = my_dict.fromkeys(my_list)#pasar claves
print(my_new_dict)
#
my_new_dict = my_dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
# Meter a todas las claves el valor(es) qu ingresamos
my_new_dict = my_dict.fromkeys(my_dict, ("Malory", "Farfan"))
print(my_new_dict)
#Toma las claves
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))

# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
my_dict = {
    "Name": "Natalia",
    "Age": 17,
    "Country": "Londres"
}
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.
print(my_dict["Name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
my_dict["Job"] = "Programador"
print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
my_dict["Age"] =38
print(my_dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dict["Country"]
print(my_dict)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
my_other_dict={
    1 : 1,
    2 : 4,
    3 : 9,
    4 : 16,
    5 : 25
}
print(my_other_dict)

# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
my_dict = {
    "name": "Brais",
    "age": 37,
    "country": "Galicia"
    }
print(my_dict)

# 8. Imprime solo las claves del diccionario.
print(my_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print(list(my_dict))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] 
# usando fromkeys(), asignando a todas las claves el valor "Desconocido".
my_dict = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_dict,"Desconocido")
print(my_new_dict)

