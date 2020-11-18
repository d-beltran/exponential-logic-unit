from decision_tree import decision_tree

# Empezamos a resolver los bits por la izquierda y utilizamos los bits ya resueltos como predictores
def left_feedback (original : list, squared : list):

    # Creamos un dataset para cada uno de los 16 bits resultado
    # Cada dataset debe incluir todos los bits predictores
    # Además incluye todos los bits cuadrados a la izquierda del actual
    # Empezamos por el primer bit (el de la izquierda del todo)
    for bit in range(16):

        # Para cada pareja de valores crea un dataset con los siguientes bit en orden:
        # El 'bit' cuadrado
        # Los bits cuadrados a la izquierda del 'bit'
        # Los bits originales
        data = [ list(reversed(squared[i][:(bit + 1)])) + original_bits for i, original_bits in enumerate(original) ]
        decision_tree(data)