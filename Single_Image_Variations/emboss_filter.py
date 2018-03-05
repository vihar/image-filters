import PIL
from PIL import Image, ImageStat, ImageFilter

im = Image.open('tulips.png')
im1 = im.filter(ImageFilter.EMBOSS())
im1.save('tulips_emboss.png')

im2 = im1.filter(ImageFilter.EMBOSS())
im2.save('ltulips_emboss_1.png')
