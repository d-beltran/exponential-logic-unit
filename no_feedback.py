from decision_tree import decision_tree

# Empezamos a resolver los bits por la derecha y utilizamos los bits ya resueltos como predictores
def no_feedback (original : list, squared : list):

    # Creamos un dataset para cada uno de los 16 bits resultado
    # Cada dataset debe incluir todos los bits predictores
    for bit in range(16):

        # Para cada pareja de valores crea un dataset con los siguientes bit en orden:
        # El 'bit' cuadrado
        # Los bits originales
        data = [ [squared[i][bit]] + original_bits for i, original_bits in enumerate(original) ]
        decision_tree(data, full_train = True)