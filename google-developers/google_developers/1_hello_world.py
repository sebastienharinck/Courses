# Hello World - Machine Learning Recipes #1
# https://www.youtube.com/watch?v=cKxRvEZd3Mw&index=1&list=PLT6elRN3Aer7ncFlaCz8Zz-4B5cnsrOMt

from sklearn import tree

features = [[130, 0], [140, 0], [150, 1], [160, 1]]
labels = [0, 0, 1, 1]

# training
clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)

# predict
print(clf.predict([[148, 1]]))