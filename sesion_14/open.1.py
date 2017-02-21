import cv2

im = cv2.imread("cat.jpg")

(w, h, c) = im.shape

print "Width: %d Height: %d Channels: %d" %(w, h, c)

for y in range(h):
	for x in range(w):
		r = im.item(x, y, 2)
		g = im.item(x, y, 1)
		b = im.item(x, y, 0)

		im.itemset((x, y, 2), 255 - r)
		im.itemset((x, y, 1), 255 - g)
		im.itemset((x, y, 0), 255 - b)

cv2.imwrite("cat2.jpg", im)