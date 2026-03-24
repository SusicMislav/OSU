import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn . preprocessing import MinMaxScaler
import sklearn . linear_model as lm
from sklearn . metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import root_mean_squared_error

data = pd.read_csv('data_C02_emission.csv')

columns = ['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 
           'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 
           'Fuel Consumption Comb (mpg)']
CO2_emissions = 'CO2 Emissions (g/km)'

x=data[columns]
y=data[CO2_emissions]

X_train , X_test , y_train , y_test = train_test_split (x, y, test_size = 0.2, random_state =1)

odabrana_velicina = 'Cylinders' 

# plt.figure()

# plt.scatter(X_train[odabrana_velicina], y_train, color='blue', label='Skup za učenje', alpha=0.5)
# plt.scatter(X_test[odabrana_velicina], y_test, color='red', label='Skup za testiranje', alpha=0.5)

# plt.title(f'Ovisnost emisije CO2 o {odabrana_velicina}')
# plt.xlabel(odabrana_velicina)
# plt.ylabel('CO2 Emissions (g/km)')
# plt.legend()
# plt.grid(True)

# plt.show()




sc = MinMaxScaler()

prije_skaliranja = X_train[odabrana_velicina]
X_train_n = sc.fit_transform( X_train )
X_test_n = sc.transform( X_test )

X_train_scaled_df = pd.DataFrame(X_train_n, columns=X_train.columns)
poslije_skaliranja = X_train_scaled_df[odabrana_velicina]

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# # Histogram prije skaliranja
# ax1.hist(prije_skaliranja, bins=20, color='skyblue', edgecolor='black')
# ax1.set_title(f'Prije skaliranja\n({odabrana_velicina})')
# ax1.set_xlabel('Originalna vrijednost')
# ax1.set_ylabel('Frekvencija')

# # Histogram nakon skaliranja
# ax2.hist(poslije_skaliranja, bins=20, color='salmon', edgecolor='black')
# ax2.set_title(f'Nakon skaliranja\n({odabrana_velicina})')
# ax2.set_xlabel('Standardizirana vrijednost (z-score)')

# plt.tight_layout()
# plt.show()


linearModel = lm.LinearRegression ()
linearModel.fit( X_train_n , y_train )

print(f"Presjek (Intercept - theta_0): {linearModel.intercept_}")
print(f"Koeficijenti (Coefficients - theta_1, theta_2, ...): {linearModel.coef_}")

y_test_p = linearModel.predict( X_test_n )
MAE = mean_absolute_error (y_test, y_test_p)
MSE = mean_squared_error (y_test, y_test_p)
RMSE = root_mean_squared_error (y_test, y_test_p)

# plt.figure()
# plt.scatter(y_test, y_test_p, color='darkcyan', alpha=0.6, edgecolors='k')

# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Idealno')

# plt.title('Odnos stvarnih i procjenjenih vrijednosti CO2')
# plt.xlabel('Stvarne vrijednosti (y_test)')
# plt.ylabel('Procjene modela (y_pred)')
# plt.legend()
# plt.grid(True)

# plt.show()