# Intro to Machine Learning (ud120)

- [Naive Bayes](naive-bayes)

## Naive Bayes

```python
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

# Para recuperar la precision del classificador sobre los elementos de entrada
score = clf.score(features_test, labels_test)
# o
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)

```
