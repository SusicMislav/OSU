import pandas as pd
import numpy as np


data = pd.read_csv('data_C02_emission.csv')

# a)

print(data.info) #Sadrži 2211 mjerenja

print(data.dtypes) #Tipovi svih veličina

if(any(data.duplicated())):
    print("There's duplicates in the collection.")
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

print(MidEngineSizeVehicles)

print(MidEngineSizeVehicles['CO2 Emissions (g/km)'].mean())

# d)

AudiCars = data[data['Make'] == 'Audi']

print(AudiCars)

AudiCarsWith4Cilinders = AudiCars[AudiCars['Cylinders'] == 4]
                              

print(AudiCarsWith4Cilinders)