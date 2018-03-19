from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import DataLoading

(X,y) = DataLoading.load_data()
model = GaussianNB()
model.fit(X, y)
print("model:", model)

expected = y
predicted = model.predict(X)

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
