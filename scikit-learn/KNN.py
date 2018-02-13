from sklearn.datasets import load_iris
iris = load_iris()

n_samples, n_features = iris.data.shape
print(iris.keys())
print(n_samples, n_features)
print(iris.data.shape)
print(iris.target.shape)
print(iris.target_names)
print(iris.feature_names)

import numpy as np
import matplotlib.pyplot as plt
x_index = 2
y_index = 0
formater = plt.FuncFormatter(lambda i,*args:iris.target_names[int(i)])
plt.scatter(iris.data[:,x_index],iris.data[:,y_index],c=iris.target, cmap=plt.cm.get_cmap('RdYlBu',3))
plt.colorbar(ticks=[0,1,2],format=formater)
plt.clim(-0.5,2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
plt.show()

from sklearn import neighbors, datasets
X,y = iris.data, iris.target

# create the model 
knn = neighbors.KNeighborsClassifier(n_neighbors=3, weights='uniform')

# fit the model
knn.fit(X,y)

# predict a sample
X_pred = [10,5,3,4]
result = knn.predict([X_pred,])

print(iris.target_names[result])
print(iris.target_names)
print(knn.predict_proba([X_pred,]))
