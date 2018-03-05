import PIL
from PIL import Image, ImageStat, ImageFilter

im = Image.open('tulips.png')
im1 = im.filter(ImageFilter.GaussianBlur(radius=1))
im1.save('tulips_gaussian_blur.png')
