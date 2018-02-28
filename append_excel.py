import pandas as pd
import PIL
from PIL import Image, ImageStat, ImageFilter
import numpy as np
import scipy
from scipy import stats
import xlsxwriter


images = ['airplane.png', 'test.jpg']

df = pd.DataFrame(columns=['1', '2', '3', '4', '5', '6', '7'])

for i in images:
    image = Image.open(i)
    snr = scipy.stats.signaltonoise(image, axis=None)
    stat = ImageStat.Stat(image)
    print("SNR\tExtrema\tRMS\tCount\tMedian\tStandard Deviation\tVariance")

    df = pd.DataFrame({i: [snr, stat.extrema, stat.rms[0],
                           stat.count, stat.median, stat.stddev, stat.var]})
    df2 = pd.DataFrame
    print(df)