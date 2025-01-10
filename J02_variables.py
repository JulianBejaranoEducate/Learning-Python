# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 7
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

# Cambio de tipo de dato de "int" a "str"
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Tipo de dato "NoneType", porque "print" no es un tipo de dato.
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))
print("\nEste es el valor de:", my_bool_variable)

# Funciones del sistema
""" 
    Fucion "len" para contar caracteres 
    "len" es una avreviatura de "length" en inglés
    Lo que significa que cuenta la longitud de la cadena de texto
"""
print(len(my_int_to_str_variable)) # = 1
print(len(my_string_variable)) # = 18
print(len("Hello World\n")) # = 11

name = "Julian"
print("\nMi nombre es: " + name, len(name)) # = 6

# Variables en una sola línea. "No es una buena practica declarar variables en una sola línea"
new_name, lastname, alias, age = "Julian", "Bejarano", "Canco", 23
print("\nMe llamo", new_name, lastname + ". Mi edad es:", age, "años", "mi alias es:", alias, len(new_name), len(lastname), len(alias), len(str(age)))

# Inputs
first_name = input("\nCual es tu primer nombre?: ")
age = input("Cuantos años tienes?: ")

print(first_name)
print(age)

name = 25
age = "Julian"

print(name)
print(age)

print((name))




