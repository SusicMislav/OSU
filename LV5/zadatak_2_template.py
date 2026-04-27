import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

labels = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}

def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()

    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution),
        np.arange(x2_min, x2_max, resolution)
    )

    # KLJUČNI FIX
    Z = classifier.predict(np.c_[xx1.ravel(), xx2.ravel()])
    Z = Z.astype(int)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.8,
            c=colors[idx],
            marker=markers[idx],
            edgecolor='w',
            label=labels[cl]
        )

# =========================
# UČITAVANJE PODATAKA
# =========================

df = pd.read_csv("penguins.csv")

print("Nedostajuće vrijednosti:\n", df.isnull().sum())

# makni stupac 'sex'
df = df.drop(columns=['sex'])

# izbaci redove s NaN
df.dropna(axis=0, inplace=True)

# kodiranje klase
df['species'] = df['species'].map({
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2
})

print(df.info())

print(df['species'].unique())
print(df['species'].dtype)

# =========================
# ODABIR VARIJABLI
# =========================

output_variable = ['species']

input_variables = [
    'bill_length_mm',
    'flipper_length_mm'
]

X = df[input_variables].to_numpy()
y = df[output_variable].to_numpy()

# =========================
# TRAIN / TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)

# =========================
# BROJ PRIMJERA PO KLASAMA
# =========================

classes_train, counts_train = np.unique(y_train, return_counts=True)
classes_test, counts_test = np.unique(y_test, return_counts=True)

x = np.arange(len(classes_train))
width = 0.35

plt.figure(figsize=(8, 6))

plt.bar(x - width/2, counts_train, width, label='Train')
plt.bar(x + width/2, counts_test, width, label='Test')

plt.xticks(x, classes_train)
plt.xlabel('Vrsta pingvina')
plt.ylabel('Broj primjera')
plt.title('Broj primjera po klasama (train vs test)')
plt.legend()

plt.show()

# =========================
# LOGISTIČKA REGRESIJA
# =========================

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train.ravel())

# parametri
print("\nKoeficijenti (coef_):")
print(model.coef_)

print("\nPresjeci (intercept_):")
print(model.intercept_)

# =========================
# GRANICA ODLUKE
# =========================

plot_decision_regions(X_train, y_train.ravel(), classifier=model)
plt.xlabel('bill_length_mm')
plt.ylabel('flipper_length_mm')
plt.legend()
plt.title('Granica odluke (train skup)')
plt.show()

# =========================
# TEST EVALUACIJA
# =========================

y_pred = model.predict(X_test)

print("\nMatrica zabune:")
print(confusion_matrix(y_test, y_pred))

print("\nTočnost:")
print(accuracy_score(y_test, y_pred))

print("\nClassification report:")
print(classification_report(y_test, y_pred))
