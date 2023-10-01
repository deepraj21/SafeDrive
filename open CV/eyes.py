import cv2

# Load the pre-trained eye detection classifiers
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
eye_pair_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_eyepair_small.xml')

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera

while True:
    # Read the current frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect individual eyes
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Detect pairs of eyes
    eye_pairs = eye_pair_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the individual eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Draw rectangles around the pairs of eyes
    for (x, y, w, h) in eye_pairs:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame with eye detections
    cv2.imshow('Eye Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
