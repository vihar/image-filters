import cv2
import numpy as np

img_file = 'airplane.png'
img = cv2.imread(img_file, cv2.IMREAD_COLOR)
alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
pixel_array_alpha = np.array(alpha_img)
pixel_array_gray = np.array(gray_img)

# print(type(np.array(img)))

print(np.array(img))
print('RGB shape: ', np.array(img).shape)
print('ARGB shape:', pixel_array_alpha.shape)
print('Gray shape:', pixel_array_gray.shape)
print('img.dtype: ', img.dtype)
print('img.size: ', img.size)
