import cv2
import mediapipe as mp
import random
import string
from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mediapipe Face Mesh for detecting facial landmarks
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Indices for left and right eye blink detection
LEFT_EYE = [159, 145]
RIGHT_EYE = [386, 374]

def generate_letter():
    """Generate a single random letter (uppercase or lowercase)."""
    return random.choice(string.ascii_letters)

def detect_blink(landmarks):
    """Detects blink based on the eye landmarks' vertical distance."""
    if not landmarks:
        return "NO_BLINK"

    left_eye_ratio = abs(landmarks[LEFT_EYE[0]][1] - landmarks[LEFT_EYE[1]][1])
    right_eye_ratio = abs(landmarks[RIGHT_EYE[0]][1] - landmarks[RIGHT_EYE[1]][1])

    if left_eye_ratio < 0.015:
        return "LEFT_BLINK"
    if right_eye_ratio < 0.015:
        return "RIGHT_BLINK"

    return "NO_BLINK"

@app.route('/')
def home():
    return render_template("index.html")  # Serve HTML file correctly

@app.route('/blink', methods=['GET'])
def detect():
    """Captures a frame, processes face landmarks, and detects blink."""
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Windows Default (more stable)

    if not cap.isOpened():
        return jsonify({"blink": "NO_CAMERA", "letter": None})

    success, frame = cap.read()
    cap.release()

    if not success:
        return jsonify({"blink": "NO_FRAME", "letter": None})

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = {i: (lm.x, lm.y) for i, lm in enumerate(face_landmarks.landmark)}
            blink = detect_blink(landmarks)
            
            if blink in ["LEFT_BLINK", "RIGHT_BLINK"]:
                letter = generate_letter()
                return jsonify({"blink": blink, "letter": letter})

    return jsonify({"blink": "NO_BLINK", "letter": None})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
