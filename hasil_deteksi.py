import cv2
# Load gambar
load = cv2.imread('img/tryout.png', 1)

# Deteksi tepi menggunakan metode Canny
edges = cv2.Canny(load, 500, 100)

# Tampilkan gambar hasil deteksi tepi
cv2.imshow("Edge Detection", edges)

# fungsi di pustaka OpenCV yang menunggu peristiwa penting keluar.
cv2.waitKey(0)

# Tutup semua jendela
cv2.destroyAllWindows()
