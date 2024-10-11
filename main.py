import cv2
import os
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_detect(img):
    face_img = img.copy()

    face_rect = face_cascade.detectMultiScale(face_img, scaleFactor=1.1, minNeighbors=5)
    for(x, y, w, h) in face_rect:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (0,0,255), 3)
    
    return face_img
    
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    frame = face_detect(frame)
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

