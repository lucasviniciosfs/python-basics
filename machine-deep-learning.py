from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris_data = datasets.load_iris()

features = iris_data.data
targets = iris_data.target

feature_test, feature_train, target_test, target_train = train_test_split(features, targets, test_size=0.2)

model = AdaBoostClassifier(n_estimators=100, learning_rate=1, random_state=123)
model.fitted = model.fit(feature_train, target_train)
model.predicted = model.fitted.predict(feature_test)

print(confusion_matrix(target_test, model.predicted))
print(accuracy_score(target_test, model.predicted))

