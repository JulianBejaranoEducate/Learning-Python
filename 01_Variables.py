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
name = input("What is your name?: ")
age =input ("How old are you? ")
print(name)
print(age)

# Una variable puede cambiar constantemente
name = 35
age = "Sara"
print(name)
print(age)

#Forzarl el tipo
address : str="Mi direccion"
address = int = 40
#Al colocar el tipo de dato en la definicion, no afecta que lyego cambie
print(type(address))
