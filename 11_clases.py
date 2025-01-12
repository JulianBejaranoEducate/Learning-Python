# Clases Primera en mayuscula
#Constructores
# Las clases son una forma de organizar y estructurar el códico
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
# Parentesis para cuando se deba pasar un parametro
print(MyEmptyPerson())

class Person:
    # Def init self es un constructor para los valores asociados a la clase
    def __init__(self, name, surname):
        # Inicializacion
        self.name = name
        self.surname = surname

my_person = Person("Malory", "Farfan")
print(f"{my_person.name} {my_person.surname}")

class PersonUno:
    # Def init self es un constructor para los valores asociados a la clase
    def __init__(self):
        # Inicializacion
        self.name = "Brais"
        self.surname = "Moure"
my_person = PersonUno()
print(f"{my_person.name} {my_person.surname}")


class PersonDos:
    # Def init self es un constructor para los valores asociados a la clase
    def __init__(self, name, surname, alias = "Sin alias"):
        # Inicializacion
        self.full_name = f"{name} {surname} ({alias})"
        #__xxx variable privada
        self.__name = name # Variable privada
        # Acceder a los datos privadoscon GET
    def get_name(self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = PersonDos("Julian", "Garcia")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = PersonDos("Santiago", "Gonzales", "El pepe")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Pedro picapiedra (la loca)"
print(my_other_person.full_name)


# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un mÃ©todo "make_sound" que imprima un sonido genÃ©rico.
class Animal:
    def __init__(self, species):
        self.species = species 
    def make_sound(self):
        print("Sonido Generico")

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacÃ©nala en una propiedad pÃºblica. AÃ±ade el mÃ©todo "make_sound" que imprima un sonido dependiendo de la especie.
class AnimalUno:
    def __init__(self, specie):
        self.specie = specie
    def make_sound(self):
        if self.specie == "Perro":
            print("Guau")
        elif self.specie == "Gato":
            print("Miau")
        else:
            print("Sonido Genérico")

# 3. Crea una clase llamada "Car" con las propiedades pÃºblicas "brand" y "model". AdemÃ¡s, debe tener una propiedad privada "_speed" que inicialmente serÃ¡ 0.
class Car:
    def __init__(self, brand, model, speed = 0):
        self.brand = brand
        self.model = model
        self.__speed = speed

# 4. AÃ±ade a la clase "Car" un mÃ©todo llamado "accelerate" que aumente la velocidad en 10 unidades. AÃ±ade tambiÃ©n un mÃ©todo "brake" que reduzca la velocidad en 10 unidades. AsegÃºrate de que la velocidad no sea negativa.
class CarUno:
    def __init__(self, brand, model, speed = 0):
        self.brand = brand
        self.model = model
        self.__speed = speed
    def accelerate(self):
        self.__speed += 10
    def brake(self):
        self.__speed - 10
        if self.__speed < 0:
            self.__speed = 0
            print("Carro detenido")
#   def brake(self):
#       self._speed = max(0, self._speed - 10)

# 5. Crea una clase "Book" que tenga propiedades como "title" (pÃºblico) y "author" (privado). AÃ±ade un mÃ©todo para obtener el autor y otro para cambiar el tÃ­tulo del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    def get_author(self):
        return self.__author
    def set_title(self,title):
        self.title = title

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. AÃ±ade un mÃ©todo para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, nombre, apellido, *notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas 
    def media_notas(self):
        media = sum(self.notas) / len(self.notas)
        return media

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". AÃ±ade mÃ©todos para depositar y retirar dinero, asegurÃ¡ndote de que no se pueda retirar mÃ¡s de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= amount

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". AÃ±ade un mÃ©todo que calcule la distancia entre dos puntos.
print("Ejercicio 8")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
    
print (Point(2, 0).distance(Point(3,5)))
# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". AÃ±ade un mÃ©todo que calcule el pago total basado en las horas trabajadas y el salario por hora.

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). AÃ±ade un mÃ©todo para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

