from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
import DataLoading

X, y = DataLoading.load_data()
model = ExtraTreesClassifier()
model.fit(X,y)

print(model.feature_importances)