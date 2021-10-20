import cv2
import time
from fer import FER
from test import simple_detection, full_detection

video = cv2.VideoCapture(0)

print(video)

print("WAITING FOR THE CAMERA")
time.sleep(2)

while True:
    check, frame = video.read()
    cv2.imwrite('Current_Image.jpg', frame)

    #emotion, score = simple_detection(frame)
    #print("emotion : ", emotion, " | score : ", score, flush=True)

    result, image = full_detection(frame)
    cv2.imshow('image',image)

    key = cv2.waitKey(300)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
