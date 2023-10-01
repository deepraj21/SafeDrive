import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # 0 represents the default camera

while True:
    # Read the current frame from the camera
    ret, frame = cap.read()

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands in the RGB frame
    results = hands.process(frame_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract landmarks for the hand
            palm = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            fingers = [hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP],
                       hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                       hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                       hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
                       hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]]

            # Convert landmarks to pixel coordinates
            palm_x, palm_y = int(palm.x * frame.shape[1]), int(palm.y * frame.shape[0])
            finger_coordinates = [(int(finger.x * frame.shape[1]), int(finger.y * frame.shape[0])) for finger in fingers]

            # Draw palm and fingers on the frame
            cv2.circle(frame, (palm_x, palm_y), 10, (0, 255, 0), -1)
            for finger_coord in finger_coordinates:
                cv2.circle(frame, finger_coord, 10, (0, 0, 255), -1)

    # Display the frame with hand detection
    cv2.imshow('Hand Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
