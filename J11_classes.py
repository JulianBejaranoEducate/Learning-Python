# Classes / Clases

""" Atajos en python con vsc """
# Ctrl + K + C -> Comentar
# Ctrl + K + U -> Descomentar
# Ctrl + Shift + P -> Buscar comandos
# Ctrl + Shift + L -> Seleccionar todas las coincidencias
# Ctrl + D -> Seleccionar la siguiente coincidencia
# Ctrl + Alt + teclad arriba/abajo -> Duplicar línea
# Ctrl + Shift + K -> Eliminar línea
# Alt + flecha arriba/abajo -> Mover línea

class Person: # Se esciben en formato CamelCase en ves de snake_case
    pass 

print(Person()) # <class '__main__.Person'>

class MyPerson:
    def __init__(self, name, surname): # Constructor de la clase, __init__ es para
        """ "Self" se refiere a la instancia de la clase """
        self.name = name
        self.surname = surname

my_person = MyPerson("Julian", "Bejarano")
print(my_person.name, my_person.surname)

class MyPerson:
    def __init__(self, name, surname): # Constructor de la clase
        """ "Self" se refiere a la instancia de la clase """
        self.name = name
        self.surname = surname

my_person = MyPerson("Julian", "Bejarano")
print(f"Hola, bienvenido {my_person.name} {my_person.surname}")

class MyPerson:
    def __init__(self): # Constructor de la clase
        """ "Self" se refiere a la instancia de la clase """
        self.name = "Julian"
        self.surname = "Bejarano"

my_person = MyPerson()
print(f"Hola, bienvenido seas {my_person.name} {my_person.surname}")

class MyPerson:
    def __init__(self, name, surnanme): # Constructor de la clase
        """ "Self" se refiere a la instancia de la clase """
        self.full_name = f"Hola, bienvenido eres {name} {surnanme}"

my_person = MyPerson("Julian", "Bejarano")
print(my_person.full_name)

class MyPerson:
    def __init__(self, name, surnanme): # Constructor de la clase
        """ "Self" se refiere a la instancia de la clase """
        self.full_name = f"Hola, bienvenido eres {name} {surnanme}"

    def walk (self):
        print(f"{self.full_name} está caminando en la calle")

my_person = MyPerson("Julian", "Bejarano")
print(my_person.full_name)

my_person.walk()

class MyPerson:
    def __init__(self, name, surnanme, nickname = "without nickname"): # Constructor de la clase
        """ "Self" se refiere a la instancia de la clase """
        self.full_name = f"Hola, bienvenido eres {name} {surnanme} {nickname}"

    def walk (self):
        print(f"{self.full_name} está caminando en la calle")

my_person = MyPerson("Julian", "Bejarano")
print(my_person.full_name)

my_person.walk()

my_other_person = MyPerson("Julian", "Bejarano", "Juli")
print(my_other_person.full_name)
my_other_person.walk()

my_person.walk()

class MyPerson:
    def __init__(self, name, surnanme, nickname = "without nickname"): # Constructor de la clase
        """ "Self" se refiere a la instancia de la clase """
        self.full_name = f"Hola, bienvenido eres {name} {surnanme} ({nickname})" # Propiedad pública
        self.__name = name # Propiedad privada
        self.__surname = name

    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} está caminando en la calle")

my_person = MyPerson("Julian", "Bejarano")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = MyPerson("Julian", "Bejarano", "Juli")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)




# Enunciados Ejercicios

# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico. 

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie. 

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0. 

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa. 

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro. 

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante. 

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta. 

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos. 

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora. 

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.