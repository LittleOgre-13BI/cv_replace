import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture("./Videos/resized.mp4")
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
imgBg = cv2.imread('./Images/1.jpg')

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgBg, threshold=0.5)

    # imgStack = cvzone.stackImages([img, imgOut], 2, 1)
    # _, imgStack = fpsReader.update(imgStack, color=(0, 0, 255))
    cv2.imshow("image", imgOut)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
