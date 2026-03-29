# ✋ Hand Motion Tracking with MediaPipe

Real-time hand tracking projects using [MediaPipe](https://mediapipe.dev/) and OpenCV. Two implementations are included — one for precise single-landmark tracking (index fingertip), and one for full hand skeleton visualization.

---

## 📁 Project Structure

```
├── index_finger_tracker.py     # Script 1 – Index fingertip tracker (MediaPipe Tasks API)
├── full_hand_tracker.py        # Script 2 – Full hand landmark visualizer (MediaPipe Solutions API)
├── hand_landmarker.task        # Required model file for Script 1 (see setup below)
└── README.md
```

---

## 🧠 Scripts Overview

### Script 1 — Index Finger Tracker (`index_finger_tracker.py`)

Tracks the tip of the **index finger** in real time using the newer **MediaPipe Tasks API**. Draws a magenta circle on the tracked point.

- Uses `HandLandmarker` from `mediapipe.tasks.python.vision`
- Tracks **1 hand** at a time
- Highlights **landmark #8** (index fingertip) with a filled circle
- Easily customizable to track any of the 21 hand landmarks (wrist, thumb, index, middle, ring, pinky)
- Requires the `hand_landmarker.task` model file (see setup)

**Landmark Index Reference:**
```
Wrist:   0
Thumb:   1,  2,  3,  4
Index:   5,  6,  7,  8   ← tip = 8
Middle:  9, 10, 11, 12
Ring:   13, 14, 15, 16
Pinky:  17, 18, 19, 20
```

---

### Script 2 — Full Hand Skeleton Tracker (`full_hand_tracker.py`)

Detects and draws the **complete hand skeleton** (all 21 landmarks + connections) using the classic **MediaPipe Solutions API**. Supports up to **2 hands** simultaneously.

- Uses `mediapipe.python.solutions.hands`
- Draws all landmarks and finger connections using default MediaPipe styles
- Supports **multi-hand detection** (up to 2 hands)
- Clean function-based structure with `run_hand_tracking()`

---

## ⚙️ Requirements

```
Python >= 3.8
opencv-python
mediapipe
```

Install dependencies:

```bash
pip install opencv-python mediapipe
```

---

## 🔧 Setup

### Script 1 — Download the Model File

Script 1 requires a `.task` model file. Download it here:

```
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task
```

Place `hand_landmarker.task` in the **same directory** as `index_finger_tracker.py`.

### Script 2 — No extra setup needed

Script 2 uses the built-in MediaPipe Solutions API and requires no model download.

---

## ▶️ Usage

**Run Script 1 (Index Finger Tracker):**
```bash
python index_finger_tracker.py
```

**Run Script 2 (Full Hand Tracker):**
```bash
python full_hand_tracker.py
```

Press **`Q`** to quit either script.

---

## 🎛️ Customization

### Script 1 — Track a different landmark
Change the landmark index to track a different point. For example, to track the **thumb tip**:

```python
# index_tip = hand_landmarks[8]   # index fingertip
thumb_tip = hand_landmarks[4]     # thumb tip
x, y = int(thumb_tip.x * w), int(thumb_tip.y * h)
```

### Script 1 — Adjust confidence thresholds
```python
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.8,   # Increase for fewer false positives
    min_hand_presence_confidence=0.8,
    min_tracking_confidence=0.8
)
```

### Script 2 — Track more hands
```python
mp_hands.Hands(
    max_num_hands=4,   # Default is 2
    ...
)
```

---

## 🔍 API Comparison

| Feature                    | Script 1 (Tasks API)        | Script 2 (Solutions API)     |
|----------------------------|-----------------------------|------------------------------|
| API Style                  | MediaPipe Tasks             | MediaPipe Solutions (legacy) |
| Hands Supported            | 1                           | Up to 2                      |
| Visualization              | Custom (single point)       | Full skeleton auto-drawn     |
| Model File Required        | ✅ Yes (.task file)         | ❌ No                        |
| Customizability            | High                        | Medium                       |
| Best For                   | Gesture/point tracking      | General hand visualization   |

---

## 📌 Notes

- Both scripts use **webcam index `0`** (default camera). Change to `1` or `2` for external cameras.
- Script 1 **mirrors the frame** before display (`cv2.flip`). Script 2 mirrors at display time.
- Tested with **MediaPipe 0.10+** and **OpenCV 4.x**.

---

## 📄 License

MIT License — free to use, modify, and distribute.
