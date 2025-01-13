# String

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Shift + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string)) # Longitud de la cadena   
print(len(my_other_string)) # Longitud de la cadena

print(my_string + " " + my_other_string) # Concatenación

my_new_line_string = "Este es un String \ncon un salto de línea"
print(my_new_line_string) # Salto de línea

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string) # Tabulación

my_scape_string = "\\Este es un String \\ escapado"
print(my_scape_string) # Escapado


''' Formateo '''
nombre, apellido, age = "Julian", "Bejarano", 22
print("Mi nomnbre es %s %s y tengo %d años" % (nombre, apellido, age)) # Formateo con %
print("Mi nomnbre es {} {} y tengo {} años".format(nombre, apellido, age)) # Formateo con format
# No se recomienda el formateo con concatenación
print("Mi nombre es " + nombre + " " + apellido + " y tengo " + str(age) + " años") # Concatenación
print(f"Mi nombre es {nombre} {apellido} y tengo {age} años") # Formateo con f


''' Desenpaquetado de caracteres '''
language = "Python"
a, b, c, d, e, f = language
print(a) # P
print(b) # y


''' División '''
language_slice = language[0:3] # [start:stop]
print(language_slice)

language_slice = language[1:] # [start:]
print(language_slice)

language_slice = language[-3] # [-index]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


''' Reverse '''
reversed_language = language[::-1] # [start:stop:step]
print(reversed_language)


''' Funciones '''
idioma = "python"
print(idioma.capitalize()) # Capitaliza la primera letra
print(idioma.upper()) # Mayúsculas
print(idioma.lower()) # Minúsculas
print(idioma.count("t")) # Cuenta
print(idioma.find("t")) # Encuentra
print(idioma.isnumeric()) # Es numérico
print("1".isnumeric()) # Es numérico
print(idioma.replace("P", "J")) # Reemplaza
print(idioma.count("P")) # Cuenta

print(idioma.upper().isupper())
print(idioma.lower().islower())

print(idioma.startswith("py")) # Empieza con
print(idioma.endswith("on")) # Termina con


# Enunciados Ejercicios

# 1. Declara una variable "text" con la frase <Aprendiendo Python> y luego imprime la longitud de la cadena usando "len()".
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: "Hola" y "Python", y muestra el resultadp en una sola linea.
print("Hola" + " Python")
print("Hola", "Python")
print("Hola" + " " + "Python")

# 3. Crea una cadena que incluya un salto de linea, y luego imprimela para ver el resultado.
text_string = "Hola\nPython"
print(text_string)

# 4. Usa el formateo de cadenas con "f-strings" para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre, apellido, edad = "Julian", "Bejarano", 22
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

# 5. Desempaqueta los caracteres de la palabra "Python" en variables separadas y luego imprimelos uno por uno.
world = "Python"
a, b, c, d, e, f = world
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un "slice" de la palabra "Programacion" para obtener los caracteres desde la posicion 3 hasta la 7.
word = "Programacion"
slice_word = word[3:8]
print(slice_word)

# 7. Inivierte la cadena "Python" usando slicing y muestra el resulatado.
word = "Python"
reverse_word = word[::-1]
print(reverse_word)

# 8. Convierte la cadena "Aprendiendo python" en mayúsculas usando el metodo adecuado e imprimela.
text = "Aprendiendo python"
print(text.upper())

# 9. Cuenta cuantas veces aparce la letra "n" en la cadena "Programacion en Python".
text = "Programacion en Python"
print(text.count("n"))

# 10. Verifica si la cadena "12345" es numerica usando el metodo adecuado e imprime el resultado.
text = "12345"
print(text.isnumeric())