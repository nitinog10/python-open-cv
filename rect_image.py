import cv2
image = cv2.imread("./team.jpg")
# image = cv2.resize(image, (1000, 1000))

image = cv2.rectangle( image, (120,150), (320,300), (255, 0, 0), 3 )

cv2.imshow("Cricket", image)
cv2.waitKey(0)