import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree

from matplotlib import pyplot as plt

# Train and test the dataframe with a selection tree model
def decision_tree (data : list, full_train : bool = False):
    
    predictors_number = len(data[0]) -1
    predictor_labels = [ 'x' + str(n) for n in range(predictors_number) ]
    column_labels = ['y'] + predictor_labels
    dataset = pd.DataFrame(data, columns=column_labels)

    train_set = dataset.drop(columns = 'y')
    test_set = dataset['y']

    # Separa el dataset en train y test set
    # Además separa los predictores (x) de los resultados (y)
    train_proportion = None
    if full_train:
        train_proportion = 255
    x_train, x_test, y_train, y_test = train_test_split(
        train_set,
        test_set,
        random_state = 123,
        train_size = train_proportion,
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

    # Show the tree is a plot
    fig = plt.figure(figsize=(25,20))
    #_ = plot_tree(modelo, feature_names=dataset.feature_names, class_names=dataset.target_names, filled=True)

    # Usa el modelo ya entrenado para predecir
    test = x_test
    if full_train:
        test = x_train
    predicciones = modelo.predict(X = test)

    # establece los valores esperados en un fromato con el que se pueda trabajar
    esperados = y_test.tolist()
    if full_train:
        esperados = y_train.tolist()

    matches = 0
    for i, r in enumerate(predicciones):
        if r == esperados[i]:
            matches += 1

    print(str(matches) + ' / ' + str(len(predicciones)))
    #break