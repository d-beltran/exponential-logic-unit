import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

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