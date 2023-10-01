import cv2
import numpy as np

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera

while True:
    # Read the current frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected face
    for (x, y, w, h) in faces:
        # Create a grid pattern on the face
        step = 20  # Grid step size

        # Draw vertical lines on the face
        for i in range(x, x + w, step):
            cv2.line(frame, (i, y), (i, y + h), (0, 255, 0), 2)

        # Draw horizontal lines on the face
        for j in range(y, y + h, step):
            cv2.line(frame, (x, j), (x + w, j), (0, 255, 0), 2)

    # Display the frame with the grid pattern overlay
    cv2.imshow('Face Grid', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
