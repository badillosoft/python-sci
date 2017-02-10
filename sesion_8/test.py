import matplotlib.pyplot as plt
import numpy as np

fig, ax0 = plt.subplots()

x = np.random.randn(1000, 3)

x = [
    [ 1, -1, 1.5],
    [ 0, -1, 1.5],
    [-0.80237978, -0.63439305,  1.88393278]
]

colors = ['red', 'tan', 'lime']
ax0.hist(x, 10, normed=1, histtype='bar', color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('bars with legend')

fig.tight_layout()
plt.show()