import cv2
import cv2.data

# Load the pre-trained Haar Cascade classifier for face detection
modelPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(modelPath)

# Initialize video capture from the default camera (0 is typically the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if camera is opened successfully
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

print("Face Detection Camera Started")
print("Press 'q' to quit, 's' to save a screenshot")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Failed to capture frame")
        break
    
    # Convert the frame to grayscale (required for Haar Cascade)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        # Draw a green rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Optionally, add text with face count
        cv2.putText(frame, f"Face", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # Display face count on the frame
    face_count = len(faces)
    cv2.putText(frame, f"Faces Detected: {face_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)
    
    # Keyboard input handling
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press 'q' to quit
        print("Exiting...")
        break
    elif key == ord('s'):  # Press 's' to save a screenshot
        cv2.imwrite('face_detection_screenshot.jpg', frame)
        print("Screenshot saved as 'face_detection_screenshot.jpg'")

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
print("Face Detection Camera Closed")
