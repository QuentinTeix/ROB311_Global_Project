#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
from fer import FER

detector = FER(mtcnn=False)  # or with mtcnn=False for Haar Cascade Classifier


def simple_detection(image):
    emotion, score = detector.top_emotion(image)
    return emotion, score

def full_detection(image):
    result = detector.detect_emotions(image)
    bounding_box = result[0]["box"]
    emotions = result[0]["emotions"]
    cv2.rectangle(image, (bounding_box[0], bounding_box[1]),
                    (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]), (0, 155, 255), 2,)
    for idx, (emotion, score) in enumerate(emotions.items()):
        
        color = (211, 211, 211) if score < 0.1 else (0, 255, 0)
        emotion_score = "{}: {}".format(emotion, "{:.2f}".format(score) if score > 0.01 else "")
        cv2.putText(image, emotion_score, (bounding_box[0], bounding_box[1] + bounding_box[3] + 30 + idx * 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1,cv2.LINE_AA,)
    
    cv2.imwrite("Current_Image_Result.jpg", image)
    return result, image

def main():
    #image = cv2.imread("justin.jpg")
    image = cv2.imread("Current_Image.jpg")
    result = detector.detect_emotions(image)

    # Result is an array with all the bounding boxes detected. We know that for 'justin.jpg' there is only one.
    bounding_box = result[0]["box"]
    emotions = result[0]["emotions"]

    # Displaying the rectangle
    cv2.rectangle(
        image,
        (bounding_box[0], bounding_box[1]),
        (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
        (0, 155, 255),
        2,
    )

    # Displaying the emotions and scores

    for idx, (emotion, score) in enumerate(emotions.items()):
        
        color = (211, 211, 211) if score < 0.1 else (0, 255, 0)
        emotion_score = "{}: {}".format(
            emotion, "{:.2f}".format(score) if score > 0.01 else "")
        cv2.putText(
            image,
            emotion_score,
            (bounding_box[0], bounding_box[1] + bounding_box[3] + 30 + idx * 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            1,
            cv2.LINE_AA,
        )


    '''
    # Displaying the fittests emotion
    color = (0, 255, 0)
    emotion_score = "{}: {}".format(
        emotion, "{:.2f}".format(score))
    cv2.putText(
        image,
        emotion_score,
        (bounding_box[0], bounding_box[1] + bounding_box[3] + 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        color,
        1,
        cv2.LINE_AA,
    )
    '''
    # Saving the result
    cv2.imwrite("Current_Image_Result.jpg", image)
    print(result)

if __name__ == '__main__':
    main()
