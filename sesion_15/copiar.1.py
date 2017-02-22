import cv2 as cv

def copiar(im, x1, y1, x2, y2):
    return im[y1:y2, x1:x2]

def pegar(im, sim, x, y):
    (h, w, c) = sim.shape
    im[y:(y + h), x:(x + w)] = sim

im = cv.imread("cat.jpg")

pata = copiar(im, 55, 152, 163, 230)

pegar(im, pata, 300, 300)

cv.imwrite("pata.jpg", im)