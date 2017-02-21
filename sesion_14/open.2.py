import cv2

im = cv2.imread("cat.jpg")

(w, h, c) = im.shape

print "Width: %d Height: %d Channels: %d" %(w, h, c)

for y in range(h):
	for x in range(w):
		r = im.item(x, y, 2)
		g = im.item(x, y, 1)
		b = im.item(x, y, 0)

		p = int((r + g + b) / 3.0)

		im.itemset((x, y, 2), p)
		im.itemset((x, y, 1), p)
		im.itemset((x, y, 0), p)

cv2.imwrite("cat3.jpg", im)