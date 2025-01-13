# Modulos
# Libreeias Conexiones entre ficheros
# Para llamar modulos o ficheros
"""
 No se pueden importar modylos si estan
   encabezados por numeros
"""

import modulopractica

modulopractica.sum_two_values(5,5)
modulopractica.printValue("Hola")


from modulopractica import sum_two_values , printValue

sum_two_values(1,2,2)
printValue("Hola")


import math

print(math.pi)
print(math.pow(2,8))
#Podemos renombrarlas con AS
from math import pi as PI_VALUE

print(PI_VALUE)