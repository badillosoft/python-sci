import cv2

im = cv2.imread("cat.jpg")

# rectangle(im, punto_i, punto_f, color, [ancho])
cv2.rectangle(im, (55, 182), (123, 220), (210, 199, 55), -1)

# line(im, punto_i, punto_f, color, [ancho])
cv2.line(im, (246, 185), (263, 391), (255, 128, 255), 10)

im2 = im.copy()

# circle(im, punto_c, radio, color, [ancho])
cv2.circle(im, (219, 130), 9, (190, 145, 112), -1)

import numpy as np

puntos = np.array([(255, 110), (302, 100), (244, 39)])

# polylines(im, puntos, cerrado?, color, [ancho])
cv2.polylines(im, [puntos], True, (75, 177, 28), 10)

cv2.imwrite("cat3.jpg", im2)