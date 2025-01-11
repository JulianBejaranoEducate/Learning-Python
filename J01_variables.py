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
"""
first_name = input("\nCual es tu primer nombre?: ")
age = input("Cuantos años tienes?: ")

print(first_name)
print(age)
"""

# Cambiar el tipo de dato, python no tiene un tipoado fuerte.
name = 25
age = "Julian"

print(name)
print(age)

# Forzar el tipo de dato
address: str = "Nueva Castilla"
address = 25
print(address)
print(type(address))

direccion: str = str (22) # Forzar el cambio al tipo de dato asigando
direccion = "Nueva Castilla"
print(direccion)
print(type(direccion))

address_one = 22
address_two = str(address_one)
print(address_two)
print(type(address_two))

espacio = "\n"
print(espacio)


# Enunciados Ejercicios

# 1.Declara y asgina valores a las siguientes variables:
"""
    a. "name": una cadena <String> que contenga tu nombre.
    b. "age": un numero entero <Integer/Int> que represente tu edad.
    c. "height": un numero flotante que represente tu altura.
    d. imprime cada variable en una linea separada.
"""
name = "Julian Bejarano"
age = 22
height = 1.78

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un textp que diga cuantos años tienes.
age = str(age)
print("Tengo", age, "años.")
print(type(age))

# 3. Declara una variable booleana "is_student" que indique si eres estudiante o no. Use true or false segun corresponda e imprime la variable.
is_student = True
print(is_student)

# 4. Usa la funcion "len()" para calcular cuantos caracteres tiene tu nombre completo, almacenado en una variable.
full_name = "Julian Francisco Bejarano Garcia"
print(len(full_name)) # = 32

# 5. Declara tes variables en una sola linea que represente tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, lastname, city = "Julian", "Bejarano", "Bogota"
print(name, lastname, city)

# 6. Use la "input()" para solicitar al usuario su color favorito y almacenalo en una variable "color". Luego, imprime el valor ingresado.
color = input("Cual es tu color favorito?: ")
print("Tu color favorito es: " + color)
print(type(color))

# 7. Declara una variable "fruit" e inicializala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelvbe a imprimir el valor.
fruit = "Manzana"
fruit = "Banano"
print(fruit)

# 8. Convierte un numero decimal, almecenado en la variable "price, a un numero entero y luego imprime el valor.
price = 1.5
price = int(price)
print(type(price))

# 9. Declara una variable "address_len" y almacena en ella la cantidad de caracteres de una direccion usando la funcion "len()". Luego, imprime el valor.
address_len = "Conjunto Residencial Nueva Castilla"
address_len = len(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable "phone", asegurandote de que siempre sera un numero. Luego, cambia su valor a un numero diferente y verifica el tipo de la variable con "type()".
phone: int = 2001
print(type(phone))
phone = 1994
print(type(phone))

number: str = str (2025) # Forzar el cambio al tipo de dato asigando
print(type(number))
number = 2024
print(type(number))

# Try
my_int = 10
my_str = str(my_int)
print(my_str)
print(type(my_str))