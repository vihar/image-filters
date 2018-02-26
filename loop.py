import PIL
from PIL import Image, ImageStat
import numpy as np
import scipy
from scipy import stats


images = ['airplane.png']

for i in images:
    image = Image.open(i)
    snr = scipy.stats.signaltonoise(image, axis=None)
    stat = ImageStat.Stat(image)
    print("SNR\tExtrema\tRMS\tCount\tMedian\tStandard Deviation\tVariance")
    print(snr, stat.extrema, stat.rms[0],
          stat.count, stat.median, stat.stddev, stat.var)
