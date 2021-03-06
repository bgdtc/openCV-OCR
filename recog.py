import numpy as np
import cv2
import pytesseract   
import pandas as pd
import time


video_record = cv2.VideoCapture(0)

while True: 
    if not video_record.isOpened():
        print('error')
        sleep(5)
        pass

    ret, frame = video_record.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = imutils.resize(gray, width=500)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # gray = cv2.Canny(gray, 170, 200)
    # RAJOUTÉ RAJOUTÉ RAJOUTÉ RAJOUTÉ
    gray = cv2.medianBlur(gray, 5)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((5,5),np.uint8)
    gray = cv2.dilate(gray, kernel, iterations=1)
    gray = cv2.erode(gray, kernel, iterations=1)
    gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    #  FIN DU RAJOUT FIN DU RAJOUT 
    gray = cv2.Canny(gray, 30, 200)
    # blur = cv2.GaussianBlur(gray, (5,5), 0)
    # ret, tresh_img = cv2.threshold(blur, 140,255,0)
    print(pytesseract.image_to_string(frame))
    contours = cv2.findContours(gray, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[-2]
    for c in contours:
        cv2.drawContours(frame, [c], -1, (0,255,0), 1)
        
        
   
    # cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):

         check, frame = video_record.read()
         cv2.imshow("capturing", frame)
         cv2.imwrite(filename='saved_img.jpg', img=frame)
         video_record.release()
         img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
         img_new = cv2.imshow("captured image", img_new)
         cv2.waitKey(1650)
         print("image saved")
         print("program end")
         cv2.destroyAllWindows()

         break
    elif cv2.waitKey(1) & 0xFF == ord('q'):
         print("turning off camera")
         video_record.release()
         print("camera off")
         print("program stopped")
         cv2.destroyAllWindows
         break

    cv2.imshow('video', gray)
video_record.release()

cv2.destroyAllWindows()
  
# video_record.release()
