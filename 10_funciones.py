# Funciones
# Encapsulan logicas concretas

def my_funcion (): # Definicion de la funcion
    print("Esto es una funcion")

my_funcion()
my_funcion()
my_funcion()

# Recibir valores
# Pasar por parametro lo que se operara
def sum_two_values (firt_values, secound_values):
    print(firt_values + secound_values)

#Sino le doy el paramero que necesita NO OPERA
sum_two_values( 5, 7)
sum_two_values( "5", "7")
sum_two_values( 1.3, 5.2)

# Retornar valores
def sum_two_values_whit_return (firt_value, secound_value):
    my_sum = firt_value + secound_value
    return my_sum

my_result =sum_two_values(5, 5)
print(my_result)

my_result =sum_two_values_whit_return(10, 5)
print(my_result)

def print_name( name, surname):
    #La f accede a los valores 
    print( f"{name} {surname}")

print_name(surname ="Farfan", name ="Malory")

def print_name_whit_defauld( name, surname, alias = "Sin alias"):
    #La f accede a los valores 
    print( f"{name} {surname} {alias}")

print_name_whit_defauld(name ="Malory", surname ="Farfan")
print_name_whit_defauld(name ="Malory", surname ="Farfan", alias = "Sapo")
#Con el asterisco = un número de prametros dinamico
def print_texts(*texts):
    for text in texts:
        print(text)
print_texts("Hola ", "Python ", "Natalia")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
print_upper_texts("Hola ", "Python ", "Natalia")



# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting( name = " Desconocido"):
    print(f"Hola {name}")
personalized_greeting ()

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.
def multiply( a, b):
    return a * b
print (multiply(2, 4))

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(3))

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.
def convert_to_uppercase(text):
    return text.upper()
print (convert_to_uppercase("Holy"))

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers):
    return sum(numbers)
print(arbitrary_sum(1,4,5))

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name , surname):
    print(f"Hola {name} {surname}")
print (generate_full_greeting(name = "Malory", surname = "Farfan"))

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponente):
    return base**exponente
print(power(2,3))

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.
def calculate_average(a, b, c):
    return(a + b + c) / 3
print(calculate_average(2,2,2))

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.
def count_characters(text):
    print(len(text))

print(count_characters("Holas"))
# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*texts):
    for text in texts:
        print(text.upper())

print(display_messages("Hola ", "Python", "Sapo"))
