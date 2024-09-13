#import library OpenCV
import cv2

#membaca gambar yang akan dipotong
image = cv2.imread('img/tryout.png')

#mendapatkan ukuran gambar
height, width = image.shape[:2]

#memotong gambar dengan ukuran 100x100 piksel pada posisi (50,50)
cropped_image = image[10:10, 10:10]

#menampilkan gambar yang telah dipotong
cv2.imshow('Cropped Image', cropped_image)

#menunggu input keyboard untuk menutup jendela
cv2.waitKey(0)

#menutup jendela
cv2.destroyAllWindows()