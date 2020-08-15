from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler #https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
'''
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html
https://rodrigopb.wordpress.com/2015/12/28/evaluar-aprendizaje-automatico/
http://rasbt.github.io/mlxtend/user_guide/evaluate/confusion_matrix/
'''
from sklearn.metrics import accuracy_score, precision_recall_fscore_support 

K = 10
X, y = load_iris(return_X_y=True)
#iris = load_iris()
#X, y = iris.data[iris.target > 0], iris.target[iris.target > 0]
#X = X[:, [2,1,3]]
escalador = StandardScaler()

pca = PCA()
X_pca = pca.fit_transform(X)
print(X_pca)
print(pca.explained_variance_ratio_)

fig = plt.figure(figsize=(20,7))
ax = fig.add_subplot

kfcvSF = KFold(n_splits=K)
skfcvSF = StratifiedKFold(n_splits=K)
kfcvST = KFold(n_splits=K,shuffle=True)
skfcvST = StratifiedKFold(n_splits=K,shuffle=True)

lst_acc = []
for train_index, test_index in skfcvST.split(X_pca,y):
    #print(f'Indices de entranmiento: {train_index}')
    #print(f'Indices de prueba: {test_index}')
    #escalador.fit(X[train_index])   
    clasificador = KNeighborsClassifier(n_neighbors=1) 
    #clasificador.fit(escalador.transform(X[train_index]), y[train_index])
    #prediccion = clasificador.predict(escalador.transform(X[test_index]))
    clasificador.fit(X[train_index], y[train_index])
    prediccion = clasificador.predict(X[test_index])
    #print(f'Predicciones {prediccion}')
    #print(f'Objetivos {y[test_index]}')
    print(f'Exactitud: {accuracy_score(y[test_index], prediccion)}')
    print(f'Precision, Sensibilidad, F-Score y Apoyo : {precision_recall_fscore_support(y[test_index], prediccion, average=None)}')
    lst_acc.append(accuracy_score(y[test_index],prediccion))
print(f'{sum(lst_acc)/K}')