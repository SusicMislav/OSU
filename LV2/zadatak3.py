import numpy as np
import matplotlib.pyplot as plt


img = plt.imread ("road.jpg ")
img = img [:,:,0]. copy ()

img = img.astype(np.float64)
brighterImg = img+80
brighterImg = np.clip(img, 0, 255)

print ( brighterImg . shape )
print ( brighterImg . dtype )
plt . figure ()
plt . imshow (brighterImg, cmap='gray')
plt . show ()