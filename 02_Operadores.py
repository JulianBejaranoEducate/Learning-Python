#Operadores aritméticos y comparativos

print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10//3)# divicion aproximada a un numero entero
print(10%2) #Operador de modulo : el resto de una divicion al final
print(2**3)# dos ELEVADO al tres

# concatenar con +
print("Hola " + "Python "+ "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2**3))

my_float = 2.5 *2
print("Hola "* int(my_float))


#Operadores comparativos

print(3>4)
print(3<4)
print(3>=4)
print(3<=4)
print(3==4)
print(3+4) # ≠ no me acepta el signo de diferencia
print(3>4==2)
print("------------------------------------")
# Revisa el Orden alfabetivo
print("Hola">"Python")
print("Hola"<"Python")
print("Hola">="Python")
print("AAA">="aaa")
print("aaa">="aaa")
print("Hola"<="Python")
print("Hola"=="Python")

#Operadores Lógicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")

print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
#Primero opera el parentesis
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not (3 > 4))



# 1. Realiza las siguientes operaciones aritmÃ©ticas:
print("1.")
print("15 + 25 =", 15 + 25)
print("50 - 22 =", 50 - 22)
print("8 * 7 =", 8 * 7)
print("100 / 20 =", 100 / 20)

# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y 
# almacÃ©nalo en una variable remainder. Luego imprÃ­melo.
print("2.")
remainder = (37 % 5)
print("El resto es: ", remainder)
# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase
#  â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.
print("3.")
numero = 7
print("Est es mi nuerofavorito: ", str(numero))
# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.
print("4.")
print("Python " * 10)
# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y 
# almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
print("5.")
a , b = 12 , 8
c = a > b
print((a > b), type(c))
# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y 
# explica cuÃ¡l tiene mayor orden alfabÃ©tico.
print("6.")
# banana tiene mayor orden alfabetico porque las letras utilizadas estan mas adelante
print ("apple" > "banana")
print ("apple" < "banana")
# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y
#  menor que 20. Imprime el resultado.
print("7.")
print("¿10 Es mayor que 5 y menor que 30? ",10 > 5 and 10 < 30)
# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.
print("8.")
print("¿El 7 es menor que 3 0 mayor que 5? ", 7 < 3 or 7 > 5)
# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
print("9.")
print( "15 mayor que 20 con not: ",not( 15 > 20))
# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la 
# expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
print("10.")
print("¿El resultado de la operacion (5*3)+2 es mayor que 10 y menor que 20?", ((5 * 3) + 2) > 10 and ((5*3)+2)<20)
