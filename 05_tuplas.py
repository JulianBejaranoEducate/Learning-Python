# Tuplas
my_tupla = tuple()
my_other_tupla = ()

my_other_tupla = (1,2,3)
my_tupla = (17, 1.58, "Malory", "Farfan", "Malory")
print(my_tupla)
print (type(my_tupla))

print(my_tupla[0])
print(my_tupla[-1])
#print(my_tupla(4))
#print(my_tupla(-6))

# Conjunto ed elementos 
# Le paso un valor y lo cuenta
print(my_tupla.count("Malory"))
# Me dice el indice del elemento que le he dado
print(my_tupla.index("Farfan"))
print(my_tupla.index("Malory"))

""" 
Las tuplas son inmutables, no se modifican pero si se pueden sumer
"""
my_sum_tupla = my_tupla + my_other_tupla
print(my_sum_tupla)
# SUB tupla
print(my_sum_tupla[3:6])

#LAS TUPLAS NO SON MUTABLES 
# SI QUEREMOS QUE SEA MUABLE HA DE SER UNA LISTA
my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla[4] = "Mouredev"
my_tupla.insert(1,"Rosa")
print(tuple(my_tupla))
print(type(my_tupla))
# Convertimos la tupla en lista, lo modificamos
#  y la convertimos de nuevo
# del para eliminar cualquier variable que le pasemos
#del my_tupla
#print(my_tupla)


# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.
print("1.")
my_tupla = (10, 20, 30, 40, 50)
print(my_tupla)
# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muÃ©stralo.
print("2.")
my_tupla = (100, 200, 300, 400, 500)
print(my_tupla[1])
# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
print("3.")
my_tupla = (1,2,3)
print("Error ya que una tupla no se puede modificar") #my_tupla[0] = 10
# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
print("4.")
my_tupla = (1, 2, 3, 3, 4, 5, 3)
print("Cantidad de 3 en la tupla",my_tupla.count(3))
# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
print("5.")
my_tupla = ("Java", "Python", "JavaScript", "Python")
print("Indice de la palabra Python",my_tupla.index("Python"))
# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
print("6.")
my_tupla_a = (1,2,3)
my_tupla_b = (4,5,6)
my_tupla_c = my_tupla_a + my_tupla_b
print("Tupla restante",  my_tupla_c)
# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
print("7.")
my_tupla = (10, 20, 30, 40, 50)
my_sub_tupla = my_tupla[1:4]
print("subtupla", my_sub_tupla)
# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
print("8.")
my_tupla_a = ("rojo", "verde", "azul")
my_list = list(my_tupla_a)
print(type(my_list))
my_list[1] = "Amarillo"
print(my_list)
my_tupla = tuple(my_list)
print(my_tupla, type(my_tupla))
# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
print("9.")
del my_tupla
print("Error ya que la tupla ha sido eliminada")
# print(my_tupla) error
# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
print("10.")
my_tupla = (100, )
print(my_tupla, type(my_tupla))