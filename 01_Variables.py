# Variables
# Una funcion que es capaz de hacer algo
# En minusculas, claras, cortas
my_string_variable = "My String" #Pueden llevar comillas simples
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

#Cambio de "int" a una cadena de texto

my_int_change_str_variable =str(my_int_variable)
print (my_int_change_str_variable)
print (type(my_int_change_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion en print 
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Funcion LEN = contar
print(len(my_int_change_str_variable))
print(len(my_string_variable))

#Variables en una sola línea
#Es mejor no combinar tipos de datos
name, lastname,alias, age = "Nata", "Farfan", "Nartish", 17
print("Me llamo", name, lastname, ", tengo:", age, "mi alias es:",alias)

#Salida para interacción con el usuario
"""
name = input("What is your name?: ")
age =input ("How old are you? ")
print(name)
print(age)"""

# Una variable puede cambiar constantemente
name = 35
age = "Sara"
print(name)
print(age)

#Forzar el tipo
address : str="Mi direccion"
address = int = 40
#Al colocar el tipo de dato en la definicion, no afecta que lyego cambie
print(type(address))


# 1. Declara y asigna valores a las siguientes variables:
name = "Nataia Farfan"
age = 17
height = 1.59
print ("Mi nombre es: ", name)
print ("Mi edad es: ", age)
print ("Mi altura es: ", height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
my_change_age = str(age)
print(type(my_change_age))
print ("Mi edad es: ", my_change_age)

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. 
# Usa True o False segÃºn corresponda e imprÃ­mela.
is_student = True
print("Soy estudiante? Respuesta: ", is_student)

# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
nombre_completo = "Malory Natalia Farfan Tique"
print("Su nombre tiene", len(nombre_completo), "caracteres")

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen.
#  Luego, imprime estos valores.
name, lastname, ciudad = "Malory", "Farfan", "Bogotá"
print("Minombre es: ",name, " ", lastname, "Soy de: ", ciudad)

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y 
# almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color_usuario = input("¿Cual es tu color favorito?")
print("El color favorito del usuario es: ", color_usuario)

# 7. Declara una variable fruit e inicialÃ­zala con un valor. 
# Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruta = "Mora"
fruta = input("¿Cual es tu fruta favorita?")
print("La fruta final es: ", fruta)
# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.
price = 1.99
numero = int =(price)
print(numero)
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres 
# de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len = "Carrera 50 trans 78 #23"
print("La cantidad de caracteres  de la direccion es: ", len(address_len))
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. 
# Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone = int = 123
phone = 456
print(type(phone))