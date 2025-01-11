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
my_new_dict = my_dict.fromkeys(my_list)#pasar claves
print(my_new_dict)
my_new_dict = my_dict.fromkeys("Nombre", 1, "Piso")#pasar claves
print(my_new_dict)
my_new_dict = my_dict.fromkeys(my_dict)#pasar claves
print(my_new_dict)

#quede en minuto 14:44