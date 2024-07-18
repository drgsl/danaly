from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
from sklearn import tree

iris = load_iris()
d = pd.DataFrame(
    data = np.c_[iris['data'], pd.Categorical.from_codes(iris.target, iris.target_names)],
    columns= iris['feature_names'] + ['class'])


X = d[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
y = d['class']

dt = tree.DecisionTreeClassifier(criterion='entropy').fit(X,y)


import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 20))
f = tree.plot_tree(dt, ax=ax, fontsize=10, feature_names=X.columns)
plt.show()


new_instances = pd.DataFrame([
    (6.1, 2.8, 4.0, 1.3)
], 
columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
new_instances

new_with_pred = new_instances.copy()
new_with_pred['predicted_class'] = dt.predict(new_instances)
new_with_pred