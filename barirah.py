
import cv2
import numpy as np

import mediapipe as mp

import screen_brightness_control as sbc
from pycaw.pycaw import AudioUtilo

# Setup volume control
speaker = AudioUtilities.GetSpeakers()
volume = speaker.EndpointVolume
min_vol, max_vol = volume.GetVolumeRange()[:2]

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    # Detect hands
    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            # Draw hand landmarks
            draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            lm = hand.landmark

            # Thumb tip and index finger tip
            x1, y1 = int(lm[4].x * w), int(lm[4].y * h)
            x2, y2 = int(lm[8].x * w), int(lm[8].y * h)

            # Draw points and line
            cv2.circle(img, (x1, y1), 8, (255, 0, 0), -1)
            cv2.circle(img, (x2, y2), 8, (255, 0, 0), -1)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Calculate distance between fingers
            distance = np.hypot(x2 - x1, y2 - y1)

            # Convert distance to percentage
            value = int(np.interp(distance, [30, 250], [0, 100]))

            # Get detected hand side
            label = result.multi_handedness[
                result.multi_hand_landmarks.index(hand)
            ].classification[0].label

            if label == "Left":
                # Control volume
                vol = np.interp(distance, [30, 250], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

                cv2.putText(img, f"Volume: {value}%",
                            (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2)

            else:
                # Control brightness
                sbc.set_brightness(value)

                cv2.putText(img, f"Brightness: {value}%",
                            (30, 90), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

    # Display webcam
    cv2.imshow("Hand Gesture Control", img)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close webcam
cap.release()
cv2.destroyAllWindows()
