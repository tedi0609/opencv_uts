import cv2

imege = cv2.imread('img/besilang.png')
print(imege. shape)
h,w, _ = imege.shape

center = (w/2, h/5)
rotation = cv2.getRotationMatrix2D(center, 90 , 0.2)
rotated_img = cv2.warpAffine(imege, rotation, (w,h))

cv2.imshow("rotated img", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()