import cv2 as cv

im = cv.imread("cat.jpg")

x1 = 55
x2 = 152

y1 = 163
y2 = 230

pata = im[y1:y2, x1:x2]

im[50:(50 + y2 - y1), 50:(50 + x2 - x1)] = pata

cv.imwrite("pata.jpg", im)