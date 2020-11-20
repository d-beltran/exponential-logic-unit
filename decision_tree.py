import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

from matplotlib import pyplot as plt

# Train and test the dataframe with a selection tree model
def decision_tree (dataset, full_train : bool = False, print_tree = False, plot_tree = False):

    predictors = dataset.drop(columns = 'y')
    target = dataset['y']

    # Separa el dataset en train y test set
    # Además separa los predictores (x) de los resultados (y)
    x_train, x_test, y_train, y_test = None, None, None, None
    if full_train:
        x_train = predictors
        y_train = target
        x_test = predictors
        y_test = target
    else:
        x_train, x_test, y_train, y_test = train_test_split(
            predictors,
            target,
            random_state = 123,
        )

    # Define los parámetros del random forest
    modelo = DecisionTreeClassifier(
        random_state = 123
    )

    # Entrena el random forest
    modelo.fit(x_train, y_train)

    # Representa en consola el decision tree correspondiente
    if print_tree:
        text_representation = export_text(modelo)
        print(text_representation)

    # Crea un plot del decision tree que detiene la ejecución del script hasta que se cierra
    if plot_tree:
        fig = plt.figure()
        #_ = plot_tree(modelo, feature_names=dataset.feature_names, class_names=dataset.target_names, filled=True)
        tree = plot_tree(modelo, filled=True)
        plt.show()

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