'''
Made By :
Akshat Pandey - F07
Abhishek Pandey - F04
Apurv Singh - F15
Namshit Manikpuri - F33
'''

import cv2
import numpy as np
def sketch(image):
     img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     img_gray_blur=cv2.GaussianBlur(img_gray,(5,5),0)
     canny_edge=cv2.Canny(img_gray_blur,10,70)
     ret, mask=cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY_INV)
     return mask

cap=cv2.VideoCapture(0)
while True:
     ret, frame = cap.read()
     cv2.imshow('Our Live Sketcher', sketch(frame))
     if cv2.waitKey(1)==13:
          break

cap.release()
cv2.destroyAllWindows()
