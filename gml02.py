import numpy as np
import pydot
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO

#import iris data
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])
for i in range(len(iris.target)):
    print('Example %d: label %s, features %s' % (i, iris.target[i], iris.data[i]))

#training data
test_idx = [0,50,100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#train a classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#these should match
print("these should match")
print(test_target)
print(clf.predict(test_data))

# viz code
dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file = dot_data,
                     feature_names =iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True, impurity=False)
graph = pydot.graph_from_dot_data(dot_data.get_value())
graph.write_pdf("iris.pdf")

print(test_data[0], test_target[0])

print(iris.feature_names, iris.target_names)


