import cv2
import pytesseract
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    imgH ,imgW,_ = frame.shape
    x1,y1,w1,h1 = 2,2,imgH ,imgW
    imgchar = pytesseract.image_to_string(frame)
    imgboxes =  pytesseract.image_to_boxes(frame)
    for boxes in imgboxes.splitlines():
        boxes = boxes.split(' ')
        x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
        cv2.rectangle(frame,(x,imgH-y),(w,imgH-h),(0,255,0),3)
        cv2.putText(frame,imgchar,(x1 +int(w1/50),y1+int(h1/50)),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2) 
        print(pytesseract.image_to_string(frame))
        cv2.imshow('text',frame)
        if cv2.waitKey(2) & 0xFF ==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()