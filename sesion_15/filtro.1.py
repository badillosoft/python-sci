import cv2 as cv

im = cv.imread("bolitas.jpg")

r = cv.inRange(im, (0, 160, 220), (127, 255, 255))

cv.imwrite("bolitas_rojas.jpg", r)