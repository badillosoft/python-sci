import cv2 as cv

im = cv.imread("cat.jpg")

cv.imshow("Mi ventana", im)
cv.imshow("Mi ventana 2", im)

cv.waitKey(0)

cv.destroyAllWindows()