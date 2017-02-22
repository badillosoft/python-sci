import cv2 as cv

im = cv.imread("cat.jpg")

im2 = im.copy()

cv.circle(im2, (100, 100), 100, (0, 0, 255), -1)

cv.imshow("Mi ventana", im)
cv.imshow("Mi ventana 2", im2)

cv.waitKey(0)

cv.destroyAllWindows()