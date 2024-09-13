# from ctypes import resize
# from hashlib import new
# from urllib.parse import _ResultMixinBase
import cv2

load = cv2.imread('img/besilang.png', 1)
size_x, size_y = load.shape[1]*2, load.shape[0]*3
new_image = cv2.resize(load, (size_x, size_y))
cv2.imshow('Foto Asli', load)
# cv2.imshow('Foto Baru', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
