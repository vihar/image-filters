import PIL
from PIL import Image, ImageStat, ImageFilter
import numpy as np
import scipy
from scipy import stats, ndimage
import pandas as pd
import csv
from math import ceil, floor
import cv2

images = ['tulips.png', 'tulips_median.png', 'tulips_gaussian_blur.png', 'tulips_edge_enhancer.png',
          'tulips_sobel.png', 'tulips_emboss.png', 'tulips_bilateral.png']
# im = Image.open('test.jpg')
# im1 = im.filter(ImageFilter.EDGE_ENHANCE)
# im1.save('test_sharp.png')


def float_round(num, places=0, direction=floor):
    return direction(num * (10**places)) / float(10**places)


with open('values.csv', 'w') as csvfile:
    fieldnames = ['IMAGE NAME', 'SNR', 'extrema', 'RMS',
                  'Count', "Median", "Standard Deviation", "Variance", "Image Variance"]
    for i in images:
        image = Image.open(i)
        snr = scipy.stats.signaltonoise(image, axis=None)
        stat = ImageStat.Stat(image)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        im = cv2.imread(i)
        a = np.asarray(im)
        variance = ndimage.variance(a)
        writer.writerow({
            'IMAGE NAME': i,
            'SNR': float_round(snr, 3, ceil),
            'extrema': stat.extrema,
            'RMS': stat.rms,
            'Count': stat.count,
            "Median": stat.median,
            "Standard Deviation": stat.stddev,
            "Variance": stat.var,
            "Image Variance": variance
        })
