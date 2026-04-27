import pandas as pd
import numpy as np


data = pd.read_csv('data_C02_emission.csv')

# a)

print(data.info()) #Sadrži 2211 mjerenja

print(data.dtypes) #Tipovi svih veličina

if(any(data.duplicated())):
    print("There's duplicates in the collection.")
    data = data.drop_duplicates()
else:
    print("There are no duplicates.")

# Pronađi sve stupce koji su tipa 'object'
object_columns = data.select_dtypes(include=['object']).columns

# Pretvori samo te stupce u 'category'
data[object_columns] = data[object_columns].astype('category')


# b)

TopFuelConsumers = data.nlargest(3, 'Fuel Consumption City (L/100km)')

print(TopFuelConsumers.loc[:, ['Make', 'Model', 'Fuel Consumption City (L/100km)']])

MostEconomicConsumers = data.nsmallest(3, 'Fuel Consumption City (L/100km)')

print(MostEconomicConsumers.loc[:, ['Make', 'Model', 'Fuel Consumption City (L/100km)']])


# c)

MidEngineSizeVehicles = data[data['Engine Size (L)'].between(2.5, 3.5)]

print(MidEngineSizeVehicles['CO2 Emissions (g/km)'].mean())

# d)

AudiCars = data[data['Make'] == 'Audi']

AudiCarsWith4Cilinders = AudiCars[AudiCars['Cylinders'] == 4]

print(AudiCarsWith4Cilinders)


# e)

print(data['Cylinders'].value_counts())

print(data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean())

# f)

print(data['Fuel Type'].unique())

diesel = data[data['Fuel Type'] == 'D']
petrol = data[data['Fuel Type'] == 'E']  # ili E/Z ovisno o datasetu

print("Diesel prosjek:", diesel['Fuel Consumption City (L/100km)'].mean())
print("Diesel medijan:", diesel['Fuel Consumption City (L/100km)'].median())

print("Petrol prosjek:", petrol['Fuel Consumption City (L/100km)'].mean())
print("Petrol medijan:", petrol['Fuel Consumption City (L/100km)'].median())

# g)

diesel4 = data[(data['Fuel Type'] == 'D') & (data['Cylinders'] == 4)]

max_car = diesel4.loc[diesel4['Fuel Consumption City (L/100km)'].idxmax()]

print(max_car[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

# h)

manual = data[data['Transmission'].str.startswith('M')]

print("Broj vozila s ručnim mjenjačem:", len(manual))

# i)

corr = data.corr(numeric_only=True)
print(corr)