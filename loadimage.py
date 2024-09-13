import cv2
# memanggil librari cv2
# load = cv2.imread('code.jpg', 1)
load = cv2.imread('img/besilang.png', cv2.IMREAD_COLOR)
print(load.shape)
print('Height: ', load.shape[1])
print('Width: ', load.shape[1])
print('Size: ', load.size)
# cv2.imshow('Load Image', load)
# cv2.imwrite('tedi.png', load)


# cv2.waitKey(0)
# cv2.destroyAllWindows()

