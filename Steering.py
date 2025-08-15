import cv2 as cv
import pydirectinput
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv.VideoCapture(0)
cap.set(3, 1280) # Set a wider resolution for better tracking
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    isTrue, img = cap.read()
    img = cv.flip(img, 1) # Flip the image horizontally for a more intuitive mirror effect

    if not isTrue:
        print("Failed to grab frame from camera.")
        break

    # Detect hands (unpack into list of hands and processed frame)
    # The key change is here: draw=True will show the landmarks, lines, and dots.
    hands, img = detector.findHands(img, draw=True)

    if hands:
        # If two hands are detected, handle the driving logic
        if len(hands) == 2:
            # First hand (let's assume it's the right hand based on position)
            hand1 = hands[0]
            lmList1 = hand1["lmList"]

            # Second hand (let's assume it's the left hand)
            hand2 = hands[1]
            lmList2 = hand2["lmList"]

            # Get only (x, y) from the index fingertip landmark (ID 8)
            point1 = lmList1[8][:2]
            point2 = lmList2[8][:2]

            # Find distance between fingertips and draw the line and points
            # This function automatically draws a line, circles on the fingertips,
            # and a circle at the midpoint, which is what you wanted.
            length, info, img = detector.findDistance(point1, point2, img)
            
            # --- Driving Logic ---

            # 1. Move forward continuously when two hands are up
            pydirectinput.keyDown("w")

            # 2. Steering logic based on the vertical position of the first hand
            # info contains [x1, y1, x2, y2, cx, cy]
            # We use info[1] which is the y-coordinate of the first hand's fingertip.
            if info[1] > 400: # Hand is lower on the screen
                cv.putText(img, "Right", (75, 80), cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)
                pydirectinput.press("d") # Corrected: 'd' for right
            elif info[1] < 250: # Hand is higher on the screen
                cv.putText(img, "Left", (75, 80), cv.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)
                pydirectinput.press("a") # Corrected: 'a' for left

        # If only one hand is detected, you can add other controls or just do nothing
        elif len(hands) == 1:
             # Stop moving forward if one hand is put down
             pydirectinput.keyUp("w")

    # If NO hands are detected, release the forward key
    else:
        pydirectinput.keyUp("w")


    # Show video feed
    cv.imshow("Webcam", img)

    # Exit on 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()