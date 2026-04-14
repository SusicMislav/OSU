import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs//imgs/test_5.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# 1. Definiraj broj željenih boja (K)
K = 5
km = KMeans(n_clusters=K, init='random', n_init=5, random_state=0)

# 2. Pokreni grupiranje nad RGB vrijednostima
# labels će sadržati indeks grupe (0 do K-1) za svaki piksel
labels = km.fit_predict(img_array)

# 3. Dohvati centre grupa (to su naše nove "reprezentativne" boje)
boje_centroidi = km.cluster_centers_

# 4. Zamijeni svaku originalnu boju bojom pripadajućeg centroida
# Svaki piksel sada dobiva RGB vrijednost centra svoje grupe
img_array_aprox = boje_centroidi[labels]

# 5. Vrati sliku u originalni oblik (dimenzije w x h x 3)
img_aprox = np.reshape(img_array_aprox, (w, h, d))

# 6. Prikaz rezultata
plt.figure()
plt.title(f"Smanjen broj boja na K={K}")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()

