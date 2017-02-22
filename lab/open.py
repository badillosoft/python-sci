import cv2

im = cv2.imread("im.jpg")

(w, h, c) = im.shape

print "Width: %d Height: %d Channels: %d" %(w, h, c)

for y in range(h):
	for x in range(w):
		r = im.item(x, y, 2)
		g = im.item(x, y, 1)
		b = im.item(x, y, 0)

		G = g / 255.0
		R = r / 255.0

		N = (G - R) / (G + R)
		
		n = (N + 1) / 2

		im.itemset((x, y, 2), n)
		im.itemset((x, y, 1), n)
		im.itemset((x, y, 0), n)

cv2.imwrite("im2.jpg", im)