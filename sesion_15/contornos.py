import cv2 as cv

im = cv.imread("bolitas_rojas.jpg")

im2 = cv.cvtColor(im, cv.COLOR_RGB2GRAY)

r, t = cv.threshold(im2, 0, 255, 0)

contornos, h = cv.findContours(t, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(im, contornos, -1, (255, 0, 0))

cv.imwrite("contornos.jpg", im)