import cv2

im = cv2.imread("cat.jpg")

(w, h, c) = im.shape

print "Width: %d Height: %d Channels: %d" %(w, h, c)

edges = cv2.Canny(im, 100, 200)

for y in range(h):
	for x in range(w):
		if edges[x][y] > 0:
			im.itemset((x, y, 1), 255)

cv2.imwrite("cat4.jpg", im)