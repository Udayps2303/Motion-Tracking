import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Download the hand landmarker task model from this link 
# and place it in the same directory as this code:
#https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task

base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1,
                                         min_hand_detection_confidence=0.8,
                                         min_hand_presence_confidence=0.8,
                                         min_tracking_confidence=0.8)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h,w,_= frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    results = detector.detect(mp_image)
    
    if results.hand_landmarks:
        for hand_landmarks in results.hand_landmarks:
            
            # Put inside [] what to track,
            # Indexing from bottom to top of fingers are as follows:
            # Thumb: 1 , 2 , 3 , 4
            # Index: 5 , 6 , 7 , 8
            # Middle: 9 , 10 , 11 , 12
            # Ring: 13 , 14 , 15 , 16
            # Pinky: 17 , 18 , 19 , 20
            
            index_tip = hand_landmarks[8] # Tracking the tip of the index finger
            x,y = int(index_tip.x * w), int(index_tip.y * h)
            cv2.circle(frame, (x,y), 10, (255,0,255), -1)
    
    cv2.imshow('index finger track', frame)
    
    #Quitting
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()