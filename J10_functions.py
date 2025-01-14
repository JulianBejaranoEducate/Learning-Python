# Funciones / Functions

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Ctrl + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

 # Una funcion tiene la palabra reservada "def" seguido del nombre de la funcion y parentesis
def my_function():
    print("Esto es una funcion") # Esta es la tarea que realiza la funcion

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(10, 20)
sum_two_values("5", "7") # Esto no es una suma, es una concatenacion
sum_two_values(1.5, 2.5) # Esto no es una suma, es una concatenacion

""" Return """
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(7, 7)
print(my_result)

def sum_two_values(a, b):
    return a + b

result = sum_two_values(5, 7)
print(result)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

def print_name(name, surname):
    print(f"Hola, {name} {surname}") # f-string, para acceder a variables dentro de un string

print_name(surname = "Julian", name = "Garcia")

def print_name_with_default(name, surname, nickname):
    print(f"Hola, {name} {surname} {nickname}")

print_name_with_default("Julian", "Garcia", "Juli")

def print_name_with_default(name, surname, nickname = "Juliancho"):
    print(f"Hola, {name} {surname} {nickname}")

print_name_with_default("Julian", "Garcia")

def print_texts(text):
    print(text)

print_texts("Hola")

def print_texts(*text): # Puede pasar un numero indefinido de argumentos o parametros
    print(text)

print_texts("Hola", "Python", "Juli")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola", "Python", "Juli")

print_texts("Hola", "Python", "Juli")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Juli")


# Enunciados Ejercicios

# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido". 

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos. 

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar. 

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas. 

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos. 

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave. 

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente. 

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio. 

# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene. 

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado. 