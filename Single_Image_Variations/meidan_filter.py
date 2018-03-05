from PIL import Image, ImageFilter
im = Image.open('tulips.png')

median = im.filter(ImageFilter.MedianFilter(3))
median.save('tulips_median.png')