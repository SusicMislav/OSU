import numpy as np
import matplotlib.pyplot as plt


xpoints = np.array( [ 1, 3, 3, 2, 1])
ypoints = np.array([ 1, 1, 2, 2, 1])

plt.plot(xpoints, ypoints, marker='o', linewidth=1, color='b')
plt.axis([0,4,0,4])
plt.xlabel("x os")
plt.ylabel("y os")

plt.show()