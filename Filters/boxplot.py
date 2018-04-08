import matplotlib.pyplot as plt
import numpy as np

a = np.array([138.13695383948587, 120.06577323173077, 110.0214299799358])
b = np.array([137.94478788080036, 119.72200523842612, 109.61453188970768])
c = np.array([137.23420428028336, 118.8962550744281, 108.63132345145415])
d = np.array([139.38081145665376, 121.9840822414636, 112.39781571208282])
e = np.array([35.330442262327544, 38.18585837540563, 39.99345255353297])
f = np.array([128.68827756597705, 128.9083184414225, 129.06725725545877])
data_to_plot = [a, b, c, d, e, f]

fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot(data_to_plot)
ax.set_xticklabels(['Original', 'Median', 'gaussian', 'Edge','Sobel','Emboss'])
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

fig.savefig('box.png', bbox_inches='tight')

# plt.show()
