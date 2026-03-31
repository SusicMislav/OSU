import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . linear_model import LogisticRegression
from sklearn . metrics import accuracy_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay
from sklearn.metrics import classification_report


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)


# inicijalizacija i ucenje modela logisticke regresije
LogRegression_model = LogisticRegression()
LogRegression_model.fit( X_train , y_train )
# predikcija na skupu podataka za testiranje
y_test_p = LogRegression_model.predict( X_test )

theta0 = LogRegression_model.intercept_[0]
theta1, theta2 = LogRegression_model.coef_[0]

print("θ0 =", theta0)
print("θ1 =", theta1)
print("θ2 =", theta2)

x1_vals = np.linspace(X_train[:, 0].min(), X_train[:, 0].max(), 100)
x2_vals = -(theta0 + theta1 * x1_vals) / theta2


print ( classification_report (y_test , y_test_p ))

cm = confusion_matrix ( y_test , y_test_p )
print (" Matrica zabune : " , cm)
disp = ConfusionMatrixDisplay ( confusion_matrix (y_test , y_test_p ))
disp . plot ()
plt . show ()


plt.figure()

plt.scatter(X_train[:, 0], X_train[:,1], c=y_train, cmap="viridis", label="Train", marker="o")

plt.scatter(X_test[:, 0], X_test[:,1], c=y_test, cmap="viridis", label="Test", marker="x")
plt.plot(x1_vals, x2_vals, color='red', label='Granica odluke',ls="--")
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Prikaz podataka (train vs test)')
plt.legend()
plt.colorbar(label='Klasa')

plt.show()


right= y_test_p==y_test
wrong = y_test_p!=y_test

plt.figure()
plt.scatter(X_test[right, 0], X_test[right,1], c="green", cmap="viridis", label="Right")
plt.scatter(X_test[wrong, 0], X_test[wrong,1], c="black", cmap="viridis", label="Wrong")
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()

plt.show()