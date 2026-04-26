import numpy as np
import matplotlib.pyplot as plt


img = plt.imread ("road.jpg ")
img = img [:,:,0]. copy ()

img = img.astype(np.float64)

# Brighter image
brighterImg = img+80
brighterImg = np.clip(brighterImg, 0, 255)


# b) DRUGA ČETVRTINA PO ŠIRINI
h, w = img.shape
second_quarter = img[:, w//4:w//2]

# c) ROTACIJA 90° U SMJERU KAZALJKE
rotated = np.rot90(img, k=-1)

# d) ZRCALJENJE (horizontalno)
mirrored = np.fliplr(img)

# PRIKAZ
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.title("Posvijetljena")
plt.imshow(brighterImg, cmap='gray')

plt.subplot(2,2,2)
plt.title("2. četvrtina")
plt.imshow(second_quarter, cmap='gray')

plt.subplot(2,2,3)
plt.title("Rotirana")
plt.imshow(rotated, cmap='gray')

plt.subplot(2,2,4)
plt.title("Zrcaljena")
plt.imshow(mirrored, cmap='gray')

plt.show()
