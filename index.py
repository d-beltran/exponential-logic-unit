import numpy as np
import pandas as pd

#from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

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

# Creamos un dataset para cada uno de los 16 bits resultado
# Cada dataset debe incluir todos los bits predictores
# Empezamos por el último bit (el de la derecha del todo), que sería el primero que miraríamos para contar
# PRUEBA: Además incluye todos los bits cuadrados a la derecha del actual
for bit in reversed(range(16)):

    # Para cada pareja de valores crea una nueva lista con un bit de los valores cuadrados y todos los valores originales
    # PRUEBA: Además incluye todos los bits cuadrados a la derecha del actual
    data = [ squared[i][bit:] + original_bits for i, original_bits in enumerate(original) ]
    predictors_number = len(data[0]) -1
    column_labels = ['y'] + [ 'x' + str(n) for n in range(predictors_number) ]
    dataset = pd.DataFrame(data, columns=column_labels)

    train_set = dataset.drop(columns = 'y')
    test_set = dataset['y']

    # Separa el dataset en train y test set
    # Además separa los predictores (x) de los resultados (y)
    x_train, x_test, y_train, y_test = train_test_split(
        train_set,
        test_set,
        random_state = 123
    )

    # Define los parámetros del random forest
    modelo = DecisionTreeClassifier(
        random_state = 123
    )

    # Entrena el random forest
    modelo.fit(x_train, y_train)

    # Representa en consola el dataset y el decision tree correspondiente
    text_representation = export_text(modelo)
    print(dataset)
    print(text_representation)

    # Usa el modelo ya entrenado para predecir
    predicciones = modelo.predict(X = x_test)

    # establece los valores esperados en un fromato con el que se pueda trabajar
    esperados = y_test.tolist()

    matches = 0
    for i, r in enumerate(predicciones):
        if r == esperados[i]:
            matches += 1

    print(str(matches) + ' / ' + str(len(predicciones)))
    #break