import cv2
import cv2.data

modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model = cv2.CascadeClassifier(modelPath)
image = cv2.imread("./team.jpg")

faces = model.detectMultiScale(image, 1.3, 5)
for face in faces:
    x, y, w, h = face

    image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0))

cv2.imshow(("Cricket Team"),image)
cv2.waitKey(0)