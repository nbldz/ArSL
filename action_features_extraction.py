from modules import *
from MP_holistic_styled_landmarks import mp_holistic, draw_styled_landmarks
from folder_setup import *
from mediapipe_detection import mediapipe_detection
from keypoints_extraction import extract_keypoints


#cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    cnt2=1
    for action in actions:
        print(action)
      
        #for z in range (1,50):
        targetDirectory = r'D:\base\sign\train/'+str("%04d" %cnt2)+'/'
        cnt2=cnt2+1
        
            
           # for sequence in range(1,number_sequences):
                        
                
        dircontent = list(os.scandir(targetDirectory))
        mp4Files = [[f.name[:-4], targetDirectory+(f.name)] for f in dircontent if f.name.lower().endswith('.mp4')]
        cnt=0
        for sequence in mp4Files:
            cnt=cnt+1

            print(sequence[1], " -- ", type(sequence[1]))
            # This prints: E:\Projects\Programming\Python\OpenCV\_CaptureSaveROI\Motiondetection_Batch_Heatmap\Burglary.mp4  --  <class 'str'>

            # Open file to process
            # Replace backslahes with forward slashes
            videofilepath = sequence[1].replace("\\","/")
            #print(videofilepath)
            # This prints: E:/Projects/Programming/Python/OpenCV/_CaptureSaveROI/Motiondetection_Batch_Heatmap/Burglary.mp4
            cap = cv2.VideoCapture(videofilepath)

            # the following doesn't give an error:
            # cap = cv2.VideoCapture("E:/Projects/Programming/Python/OpenCV/_CaptureSaveROI/Motiondetection_Batch_Heatmap/videofiles/Burglary.mp4")

            #print(cap)
            # This prints: <VideoCapture 018CB4C0>

            if (cap.isOpened() == False):
                print("Error opening the video file")
            else:
                
                sequence_length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                
                
                for frame_num in range(int(sequence_length)):
                    ret, frame = cap.read(frame_num)
                    #heatmap = frame.copy()            

            #♣cap = cv2.VideoCapture(r'D:\base\sign\train/'+str("%04d" %sequence)+".mp4")
            # Check if camera opened successfully
            # if (cap.isOpened()== False): 
            #     print("Error opening video stream or file")
            # ret, frame = cap.read()  
              #☺  if ret == True:
                    #cv2.imshow('Frame',frame)
                    #frame=cv2.resize(frame, None, fx = 0.4, fy = 0.4)
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
            
            # Wait 
                    # if frame_num == 0: 
                    #     cv2.putText(image, 'START NEW ACTION', (120,200), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                    #     cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                    #     cv2.imshow('Action Detection', image)
                    #     #cv2.waitKey(2000)
                    # else: 
                    #     cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                    #     cv2.imshow('Action Detection', image)
                                   
                    keypoints = extract_keypoints(results)
                    keypoint_path = os.path.join(DATA_PATH,action, str(cnt), str(frame_num))
                    
                    if cnt>23:
                        break
                    else:
                        np.save(keypoint_path, keypoints)


                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                    
    cap.release()
    cv2.destroyAllWindows()


