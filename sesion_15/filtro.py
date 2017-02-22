import cv2 as cv

im = cv.imread("cat.jpg", 0)

r1, t1 = cv.threshold(im, 250, 255, cv.THRESH_BINARY_INV)

cv.imwrite("bolitas_gris.jpg", im)
cv.imwrite("bolitas_um.jpg", t1)