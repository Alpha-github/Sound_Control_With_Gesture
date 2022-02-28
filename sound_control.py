import cv2
import mediapipe as mp
import math
import numpy as np

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ht,wd,c = frame.shape

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lmlist=[]
            for id,lm in enumerate(hand_landmarks.landmark):
                lmlist.append([id,int(wd*lm.x),int(ht*lm.y)])
            # print(lmlist)

            mp_drawing.draw_landmarks(frame,hand_landmarks,
            mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style())

            if lmlist:
                tx,ty = lmlist[4][1],lmlist[4][2]
                ix,iy = lmlist[8][1],lmlist[8][2]

                cv2.line(frame,(tx,ty),(ix,iy),(255,0,0),3)

                length  = math.hypot(ix-tx,iy-ty)

            minVol = volume.GetVolumeRange()[0]
            maxVol = volume.GetVolumeRange()[1]
            vol = np.interp(length , [50 ,300] , [minVol ,maxVol])
            # print(vol)
            volBar = np.interp(length , [50 ,300] , [400 ,150])
            # print(volBar)
            volPer = np.interp(length , [50 ,300] , [0 ,100])

            volume.SetMasterVolumeLevel(vol,None)
            cv2.rectangle(frame , (50 ,150) , (85 , 400) , (255,200,100),3) #(123,213,122)
            cv2.rectangle(frame , (50 , int(volBar)) , (85 ,400) ,(200, 0,0) ,cv2.FILLED)
            cv2.putText(frame , str(int(volPer)) , (40, 450) ,cv2.FONT_HERSHEY_DUPLEX,2 , (244,221,158) , 2)
                

    cv2.imshow("Video",frame)
    if cv2.waitKey(20)==ord('q'): # press 'Q' to exit
        break
