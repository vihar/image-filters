import PIL
from PIL import Image, ImageStat, ImageFilter

im = Image.open('brain.jpg')
im1 = im.filter(ImageFilter.UnsharpMask(radius=1))
im1.save('brain_enhanced_1.jpg')

im2 = im1.filter(ImageFilter.UnsharpMask(radius=1))
im2.save('brain_enhanced_2.jpg')

im3 = im2.filter(ImageFilter.UnsharpMask(radius=1))
im3.save('brain_enhanced_3.jpg')

im4 = im3.filter(ImageFilter.UnsharpMask(radius=1))
im4.save('brain_enhanced_4.jpg')