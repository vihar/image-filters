from scipy import ndimage
import numpy as np
import cv2

images = ['tulips.png', 'tulips_median.png', 'tulips_gaussian_blur.png', 'tulips_edge_enhancer.png',
          'tulips_sobel.png', 'tulips_emboss.png', 'tulips_bilateral.png']


for i in images:
    im = cv2.imread(i)
    a = np.asarray(im)
    print(ndimage.variance(a))
