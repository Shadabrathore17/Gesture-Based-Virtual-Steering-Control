# Gesture-Based-Virtual-Steering-Control
🖐 Control your car in racing games using just your hands — AI-powered gesture steering with Python, OpenCV, and cvzone. 🚗🎮
🖐 Gesture-Based Virtual Steering Control 🚗

A Python-based gesture control system that uses computer vision to steer in racing games without a physical controller or steering wheel. This project leverages OpenCV, cvzone's HandTrackingModule, and PyDirectInput to track your hands in real time and translate gestures into driving commands.

📌 Features

🎮 Hands-Free Gaming – Drive and steer using only hand gestures.

🖐 Two-Hand Detection – Move forward when both hands are raised.

↔ Steering Control – Tilt your hands up or down to steer left or right.

📹 Real-Time Tracking – Powered by OpenCV and HandTrackingModule for smooth tracking.

⚡ Instant Input Mapping – Sends keystrokes directly to your game via PyDirectInput.

🛠️ Tech Stack

Language: Python

Libraries:

OpenCV – for video capture and image processing

cvzone.HandTrackingModule – for hand and landmark detection

PyDirectInput – for sending game control inputs

📷 How It Works

The webcam captures the video feed.

The HandTrackingModule detects hand landmarks in real time.

The distance and position of your hands determine the driving actions:

Both hands up → Move forward (W key)

Right hand lower → Steer right (D key)

Right hand higher → Steer left (A key)

PyDirectInput sends the corresponding keystrokes to the game.

📂 Installation

Clone the repository:-

git clone https:
//https://github.com/Shadabrathore17/Gesture-Based-Virtual-Steering-Control


Install dependencies :-

pip install opencv-python cvzone pydirectinput


Run the script :-

python main.py

🎮 Usage Notes

Make sure your webcam is connected and working.

Stand/sit where both hands are clearly visible to the camera.

Adjust detection sensitivity by tweaking detectionCon in the code.

Works best in good lighting conditions.

📸 Demo

(project GIF or screenshot here uploaded)

🚀 Future Improvements

Add speed control using hand distance.

Support for more gestures like braking or drifting.

Integrate with VR environments.
