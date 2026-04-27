import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error

# učitaj podatke
data = pd.read_csv('data_C02_emission.csv')

# numeričke + kategorička
num_cols = ['Engine Size (L)', 'Cylinders',
            'Fuel Consumption City (L/100km)',
            'Fuel Consumption Hwy (L/100km)',
            'Fuel Consumption Comb (L/100km)',
            'Fuel Consumption Comb (mpg)']

# one-hot encoding
fuel_encoded = pd.get_dummies(data['Fuel Type'], prefix='Fuel')

# X i y
X = pd.concat([data[num_cols], fuel_encoded], axis=1)
y = data['CO2 Emissions (g/km)']

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# model
model = lm.LinearRegression()
model.fit(X_train, y_train)

# predikcija
y_pred = model.predict(X_test)

# metrike
MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

print("MAE:", MAE)
print("MSE:", MSE)
print("RMSE:", RMSE)

# =========================
# maksimalna pogreška
# =========================
errors = np.abs(y_test - y_pred)

max_error = errors.max()
max_index = errors.idxmax()

print("Maksimalna pogreška:", max_error)

# koji auto?
worst_case = data.loc[max_index]

print("Vozilo s najvećom pogreškom:")
print(worst_case[['Make', 'Model', 'CO2 Emissions (g/km)']])