import cv2;

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

print(video)

while True:
    check, frame = video.read()
    cv2.imshow('Face Detector', frame)
    cv2.imwrite('Current_Image.jpg', frame)

    key = cv2.waitKey(1000)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
