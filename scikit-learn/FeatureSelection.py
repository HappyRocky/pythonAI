from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import DataLoading
import numpy as np

X, y = DataLoading.load_data()
print(np.shape(X))

# Tree algorithms allow to compute the informativeness of features.
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_)

# create the RFE model and select 3 attributes
model = LogisticRegression()
rfe = RFE(model, 3)
rfe = rfe.fit(X, y)
# summarize the selection of the attributes
print(rfe.support_)
print(rfe.ranking_)