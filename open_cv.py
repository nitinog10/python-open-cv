import cv2
image = cv2.imread("./Image.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow(" MY BMW ", gray_image)
cv2.imshow(" BMW ", image)
cv2.waitKey(0)