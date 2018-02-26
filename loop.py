import PIL
from PIL import Image, ImageStat
import numpy as np
import scipy
from scipy import stats

from xlutils.copy import copy    
from xlrd import open_workbook

book_ro = open_workbook("variables.xlsx")
book = copy(book_ro)  # creates a writeable copy
sheet1 = book.get_sheet(0)  # get a first sheet

colx = 1
for rowx in range(1):
    # Write the data to rox, column
    sheet1.write(rowx,colx, url)
    sheet1.write(rowx,colx+1, count)

book.save("D:\Komal\MyPrograms\python_spreadsheet.xls")

images = ['airplane.png']

for i in images:
    image = Image.open(i)
    snr = scipy.stats.signaltonoise(image, axis=None)
    stat = ImageStat.Stat(image)
    print("SNR\tExtrema\tRMS\tCount\tMedian\tStandard Deviation\tVariance")
    print(snr, stat.extrema, stat.rms[0],
          stat.count, stat.median, stat.stddev, stat.var)
