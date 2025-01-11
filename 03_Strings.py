#Strings

my_string = "My String"
my_other_string = "My Other String"

print(len(my_string))
print(len(my_other_string))
print( my_string +" "+ my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

#Fomatear Strings
name, lastname, age ="Natalia", "Farfan", 17
print("Mi nombre es: {} {} y mi edad es {}".format(name,lastname,age))
print("Mi nombre es: %s %s y mi edad es %d" %(name,lastname,age))
print("Mi nombre es: " + name + lastname + "y mi edada es: "+ str(age))
#Inferencia de datos
print(f"Mi nombre es: {name} {lastname} y mi edad es {age}")

# Desempaquetado de datos
lenguaje ="python"
a, b, c, d, e, f= lenguaje
print(a)
print(e)

# División

lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]
print(lenguaje_slice)
# Salta y toma solo las posiciones que escojamos
lenguaje_slice = lenguaje[0:2:4]
print(lenguaje_slice)

# Reverse

reverse_lenguaje =lenguaje [::-1]

#Funciones del sistema

print(lenguaje.capitalize()) #Primera letra en mayuscula
print(lenguaje.upper()) #Todo en mayuscula
print(lenguaje.count("t")) #Cuenta las veces que se repite el parametro indicado
print(lenguaje.isnumeric()) #Pregunta si es un número (True or Flase)
print("1".isnumeric())
print(lenguaje.lower())#Todo minuscula
print(lenguaje.upper().isupper()) #Coloca todo en mayúscula y pregunta si es mayúscula
print(lenguaje.lower().isupper()) #Coloca todo en minuscula y pregunta si es mayúcula
print(lenguaje.startswith("py")) #Le decimos: python empiza con "x" parametro que le pasemos
print(lenguaje.startswith("Py"))
print("Py" == "py")


# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
print("1.")
my_text = "Aprendiendo Python"
print("La longitud es: ",len(my_text))
# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
print("2.")
a, b = "Hola ", "Python"
print( a + b)
print ("Hola", "Python")
# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
print("3.")
print("Hola\nPython")
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
print("4.")
print(f"Mi nombre es {"Natalia "}{"Farfan"} y tengo {17}")
# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
print("5.")
palabra = "python"
a,b,c,d,e,f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
print("6.")
palabra = "programacion"
palabra_slice = palabra[3:7]
print (palabra_slice)
# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
print("7.")
cadena = "python"
cadena_invertida = cadena[::-1]
print(cadena_invertida)
# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
print("8.")
cadena = "Aprendiendo python"
print(cadena.upper())
# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
print("9.")
cadena = "Programación en python"
print(cadena.count("a"))
# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
print("10.")
cadena = "12345"
print(cadena.isnumeric())