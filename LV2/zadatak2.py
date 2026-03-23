import numpy as np 

import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)


print(len(data)) # mjerenja su izvršena na 10000 osoba

plt.scatter(data[:, 1], data[:, 2]) # prikaz svih podataka
plt.scatter(data[::50, 1], data[::50, 2]) # prikaz svakog 50-og podatka
plt.xlabel('visina')
plt.ylabel('težina')
#plt.show()

print("najmanja visina: ", np.min(data[:,1]))
print("najveća visina: ", np.max(data[:,1]))
print("srednja vrijednsot visine: ", np.mean(data[:,1]))

menIndex = (data[:,0]==1)
men = data[menIndex]

womenIndex = data[:,0] == 0
women = data[womenIndex]

print("najmanja visina muškaraca: ", np.min(men[:,1]))
print("najveća visina muškaraca: ", np.max(men[:,1]))
print("srednja vrijednsot visine muškaraca: ", np.mean(men[:,1]))

print("najmanja visina žena: ", np.min(women[:,1]))
print("najveća visina žena: ", np.max(women[:,1]))
print("srednja vrijednsot visine žena: ", np.mean(women[:,1]))