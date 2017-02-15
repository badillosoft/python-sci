import numpy as np

x = np.linspace(-3.14, 3.14, 100)
y = np.cos(x)

print x
print y

import matplotlib.pyplot as plt

plt.plot(x, y)

plt.show()