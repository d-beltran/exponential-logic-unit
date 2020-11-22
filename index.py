from utils import int2binary

import pandas as pd

from decision_tree import decision_tree

# Empezamos a resolver los bits por la derecha y utilizamos los bits ya resueltos como predictores
def main (
    exponent : int = 2,
    feedback : bool = False,
    right_2_left : bool = False,
    full_train : bool = False,
    print_dataset : bool = False,
    print_tree : bool = False,
    plot : bool = False,
    ):

    # Set the maximum possible number of bits in the output
    # Since the maximum possible input is 255 (11111111), the maximum possible output is 255 * exponent
    # The number of bits of the output value is always the number of bits of the input value multiplied by the exponent
    output_bits = exponent * 8

    # Genera un dataset con los primeros 256 números enteros (predcitores) en formato binario
    # Y con sus respectivos cuadrados (resultados) también en formato binario
    original_bits = pd.DataFrame( [ int2binary(n) for n in range(256) ] )
    squared_bits = pd.DataFrame( [ int2binary(n**exponent, output_bits) for n in range(256) ] )

    # Renombra las columnas del dataset original añadiéndoles una 'p' (de predictor)
    original_bits.columns = [ 'p' + str(column) for column in original_bits.columns]

    # Set the ordered indexes of squared bits to be solved
    bits = range(output_bits)
    if right_2_left:
       bits = reversed(range(output_bits))

    # Creamos un dataset para cada uno de los 16 bits cuadrados
    # Cada dataset debe incluir todos los bits predictores
    for bit in bits:

        # Establece la primera columna: el bit a resolver
        # Ponle de nombre 'y'
        target_bit = squared_bits.loc[:, [bit]]
        target_bit.columns = ['y']

        # En caso de que haya feedback establece los bits que se usan como feedback
        # Esto dependerá de si se lee de izquierda a derecha o viceversa
        feedback_bits = None
        if feedback:
            if right_2_left:
                # Los bits a la derecha del actual
                feedback_bits = squared_bits.loc[:, bit +1 : ]
            else:
                # Los bits a la izquierda del actual
                feedback_bits = squared_bits.loc[:, : bit -1 : ]
            # Cambia los nombres de las columnas añadiéndoles una 'f' (de feedback)
            feedback_bits.columns = [ 'f' + str(column) for column in feedback_bits.columns]

        # Para cada pareja de valores crea un dataset con los siguientes bit en orden:
        # El 'bit' cuadrado
        # Los bits originales
        data = pd.concat([ target_bit, feedback_bits, original_bits ], axis = 1)

        if print_dataset:
            print(data)

        decision_tree(
            data,
            full_train = full_train,
            print_tree = print_tree,
            plot = plot,
        )


main(exponent = 3, feedback = True, right_2_left = True, full_train = True, print_dataset = True, print_tree = True)
# ----------------------------------------------------------------------------------------------

#no_feedback(original, squared, full_train = True)
#left_feedback(original, squared)
#right_feedback(original, squared)