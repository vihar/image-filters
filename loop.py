import PIL
from PIL import Image, ImageStat, ImageFilter
import numpy as np
import scipy
from scipy import stats
import pandas as pd
import csv

images = ['tulips.png', 'tulips.png']

# im = Image.open('test.jpg')
# im1 = im.filter(ImageFilter.EDGE_ENHANCE)
# im1.save('test_sharp.png')

for i in images:
    image = Image.open(i)
    snr = scipy.stats.signaltonoise(image, axis=None)
    stat = ImageStat.Stat(image)
    with open('values.csv', 'w') as csvfile:
        fieldnames = ['IMAGE NAME', 'SNR', 'extrema', 'RMS',
                      'Count', "Median", "Standard Deviation", "Variance"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'IMAGE NAME': i,
            'SNR': snr,
            'extrema': stat.extrema,
            'RMS': stat.rms[0],
            'Count': stat.count,
            "Median": stat.median,
            "Standard Deviation": stat.stddev,
            "Variance": stat.var
        })
