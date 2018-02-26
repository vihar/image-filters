import PIL
from PIL import Image, ImageStat
import numpy as np
import scipy
from scipy import stats

image = Image.open("airplane.png")
img_pixel_array = np.array(image)
print(img_pixel_array)

rgb_array = list(image.getdata())
rgb_mean = np.mean(rgb_array, axis=0)
print("RGB MEAN")
print(rgb_mean)

snr = scipy.stats.signaltonoise(image, axis=None)
print("SIGNAL TO NOISE RATIO")
print(snr)

"""
print(rgb_array)

print(type(rgb_array))
bw_array = image.convert('L').getdata()
print(type(bw_array))

print(rgb_array)
print(rgb_array[2])
print(bw_array[2])
"""

stat = ImageStat.Stat(image)
print("Extrema")
print(stat.extrema)
print("Pixel RMS")
print(stat.rms[0])
print("Pixel Count")
print(stat.count)
print("Pixel Median")
print(stat.median)
print("Standard Deviation")
print(stat.stddev)
print("Variance")
print(stat.var)
