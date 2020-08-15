from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
#X, y = make_classification(n_samples=10000, n_classes=2, n_features=2 , n_informative=1, n_repeated=0,n_redundant=1, n_clusters_per_class=1)
weights = (0.6,0.4)
X, y =  make_classification(n_samples=10000, n_classes=2,n_features=2, n_redundant=0, n_informative=1,n_clusters_per_class=1, weights=weights)
plt.plot(X[:, 0:1],X[:, 1:2],"ro")
plt.show()
dat = open("creado.txt", "w")
[dat.write(f"{y[i]},{X[i][0]},{X[i][1]}\n" ) for i in range(len(y))]

