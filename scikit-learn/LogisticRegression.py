from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import DataLoading as dl

(X, y) = dl.load_data()

# get model
model = LogisticRegression()
model.fit(X, y)
print("model", model)

# predict
expected = y
predicted = model.predict(X)

# summarize the fit of the model
print("report", metrics.classification_report(expected, predicted))
print("confusion matrix", metrics.confusion_matrix(expected, predicted))