class Perro:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def ladrar(self):
        return f"{self.nombre} está ladrando"
    
    def mover_la_cola(self):
        return "Moviendo la cola"