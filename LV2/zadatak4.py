import numpy as np
import matplotlib.pyplot as plt

# crni i bijeli kvadrat
black = np.zeros((50, 50))
white = np.ones((50, 50)) * 255

# gornji red: crno | bijelo
top = np.hstack((black, white))

# donji red: bijelo | crno
bottom = np.hstack((white, black))

# složi cijelu sliku
img = np.vstack((top, bottom))

# prikaz
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()
