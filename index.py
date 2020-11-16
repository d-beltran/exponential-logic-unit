import pandas as pd

from no_feedback import no_feedback
from left_feedback import left_feedback
from right_feedback import right_feedback

# Convierte un numero entero en un binario de 16 bits
# El formato es una lista de 16 booleanas: True (1) y False (0)
def int2binary16 (i):
    # El comando 'bin' devuelve el número binario precedido por '0b'. Hay que eliminar este '0b' inicial
    binary = bin(i)[2:]
    # Rellena con 0s hasta tener 16 bits
    binary16 = binary.zfill(16)
    # Convierte cada 0 en false y cada 1 en true
    formattedBinary16 = [ bool(int(binary16[i])) for i in range(16) ]
    return formattedBinary16

# Genera un dataset con los primeros 256 números enteros (predcitores) en formato binario
# Y con sus respectivos cuadrados (resultados) también en formato binario
original = [ int2binary16(n) for n in range(256) ]
squared = [ int2binary16(n*n) for n in range(256) ]

#no_feedback(original, squared)
left_feedback(original, squared)
#right_feedback(original, squared)