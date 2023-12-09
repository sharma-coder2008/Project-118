# import the opencv library
import cv2

# Define a video capture object
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

   
# Capture the video frame by frame
video = cv2.VideoCapture("walking.avi")

while True :
    ret,frame = video.read()
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,1.2,3)

    for x,y,w,h in faces :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        crop = frame[y:y+h,x:x+h]
        cv2.imwrite("face.jpg",crop)

    cv2.imshow("img",frame)
    if cv2.waitKey(25) == 32 :
        break

video.release()
cv2.destroyAllWindows()