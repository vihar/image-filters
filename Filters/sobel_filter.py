import PIL
from PIL import Image, ImageStat, ImageFilter

im = Image.open('brain_enhanced_4.jpg')
im1 = im.filter(ImageFilter.FIND_EDGES())
im1.save('brain_sobel_enhanced.jpg')

