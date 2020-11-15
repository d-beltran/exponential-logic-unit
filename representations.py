# Representa en consola el binario y el binario cuadrado de un número
def squared_binary (num : int):
     # El comando 'bin' devuelve el número binario precedido por '0b'. Hay que eliminar este '0b' inicial
    binary = bin(num)[2:]
    # Rellena con 0s hasta tener 16 bits
    binary16 = binary.zfill(16)
    # Repite para el cuadrado
    squared_binary = bin(num*num)[2:]
    squared_binary16 = squared_binary.zfill(16)
    # Representa el binario y su cuadrado en consola
    print(binary16 + " - " + str(num) + "\n||||||||||||||||\n" + squared_binary16 + " - " + str(num*num))