import PIL
from PIL import Image, ImageStat, ImageFilter
import numpy as np
import scipy
from scipy import stats


images = ['airplane.png', 'output.png', 'endge_enhance.png']
im = Image.open('airplane.png')
# im1 = im.filter(ImageFilter.EDGE_ENHANCE)
# im1.save('endge_enhance.png')

for i in images:
    image = Image.open(i)
    snr = scipy.stats.signaltonoise(image, axis=None)
    stat = ImageStat.Stat(image)
    print("SNR\tExtrema\tRMS\tCount\tMedian\tStandard Deviation\tVariance")
    print(snr, stat.extrema, stat.rms[0],
          stat.count, stat.median, stat.stddev, stat.var)
