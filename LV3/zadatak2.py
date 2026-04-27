import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# učitavanje podataka
data = pd.read_csv('data_C02_emission.csv')

# =========================
# a) HISTOGRAM CO2 EMISIJE
# =========================
plt.figure()
plt.hist(data['CO2 Emissions (g/km)'], bins=30)
plt.title('Histogram CO2 emisija')
plt.xlabel('CO2 Emissions (g/km)')
plt.ylabel('Broj vozila')
plt.show()

# =========================
# b) SCATTER: POTROŠNJA vs CO2
# =========================
plt.figure()

# boje po tipu goriva
fuel_types = data['Fuel Type'].unique()

for fuel in fuel_types:
    subset = data[data['Fuel Type'] == fuel]
    plt.scatter(subset['Fuel Consumption City (L/100km)'],
                subset['CO2 Emissions (g/km)'],
                label=fuel)

plt.title('Gradska potrošnja vs CO2 emisija')
plt.xlabel('Fuel Consumption City (L/100km)')
plt.ylabel('CO2 Emissions (g/km)')
plt.legend(title="Fuel Type")
plt.show()

# =========================
# c) BOXPLOT izvangradske potrošnje
# =========================
plt.figure()

data.boxplot(column='Fuel Consumption Hwy (L/100km)',
             by='Fuel Type')

plt.title('Izvangradska potrošnja po tipu goriva')
plt.suptitle('')
plt.xlabel('Fuel Type')
plt.ylabel('Fuel Consumption Hwy (L/100km)')
plt.show()

# =========================
# d) BROJ VOZILA PO TIPU GORIVA
# =========================
plt.figure()

fuel_counts = data.groupby('Fuel Type').size()

fuel_counts.plot(kind='bar')

plt.title('Broj vozila po tipu goriva')
plt.xlabel('Fuel Type')
plt.ylabel('Broj vozila')
plt.show()

# =========================
# e) PROSJEČNA CO2 EMISIJA PO CILINDRIMA
# =========================
plt.figure()

avg_co2 = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()

avg_co2.plot(kind='bar')

plt.title('Prosječna CO2 emisija po broju cilindara')
plt.xlabel('Cylinders')
plt.ylabel('CO2 Emissions (g/km)')
plt.show()