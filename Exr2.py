import cv2
import keyboard
import numpy as np

def DecSkin(frame):
    Frme = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    A = np.array([0, 45, 58], dtype = "uint8")
    B = np.array([20, 150, 250], dtype = "uint8")
    C = np.array([172, 45, 58], dtype = "uint8")
    D = np.array([179, 150, 250], dtype = "uint8")
    Skin = cv2.inRange(Frme, A, B)
    SkinMask = cv2.inRange(Frme, C, D)
    Skin = cv2.GaussianBlur(Skin, (3, 3), 0)
    SkinMask = cv2.GaussianBlur(SkinMask, (3, 3), 0)
    Root = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
    HSV = cv2.dilate(Skin, Root)
    HSV_M = cv2.dilate(SkinMask, Root)
    Skin1 = cv2.bitwise_and(frame, frame, mask = HSV)
    Skin2 = cv2.bitwise_and(frame, frame, mask = HSV_M)
    skin = cv2.bitwise_or(Skin1,Skin2) 
    
    return skin

video= cv2.VideoCapture(0)
while True:
    S, F = video.read()
    if not S or keyboard.is_pressed('0'):
        break
    
    Output = DecSkin(F)
    cv2.imshow('Cam-0', Output)
    cv2.waitKey(1)
   
video.release()
