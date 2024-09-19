# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 03:58:10 2024

@author: nbl
"""

from modules import *
from MP_holistic_styled_landmarks import mp_holistic,draw_styled_landmarks
from mediapipe_detection import mediapipe_detection
from keypoints_extraction import extract_keypoints
import keras
from folder_setup import *
from visualization import prob_viz,colors



sequence = []
sentence = []
threshold = 0.3

model = keras.models.load_model(r'D:\sharjah\sign\nblsignvideo\Model\lstm_model.h5')

cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():


        ret, frame = cap.read()


        image, results = mediapipe_detection(frame, holistic)
        print(results)
        

        draw_styled_landmarks(image, results)
        

        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-30:]
        
        
        res = model.predict(np.expand_dims(sequence, axis=0))[0]
        print(actions[np.argmax(res)])
            
            

        if res[np.argmax(res)] > threshold: 
            if len(sentence) > 0: 
                if actions[np.argmax(res)] != sentence[-1]:
                    sentence.append(actions[np.argmax(res)])
            else:
                sentence.append(actions[np.argmax(res)])

        if len(sentence) > 5: 
            sentence = sentence[-5:]
                

            
            image = prob_viz(res, actions, image, colors)
            
        
            
        cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, ' '.join(sentence), (3,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        

       
        cv2.imshow('Action_Recognition', image)


        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()