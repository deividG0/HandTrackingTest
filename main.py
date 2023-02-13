import cv2
import tensorflow as tf
import time
import math
import numpy as np
import HandTrackingModule as htm
from functools import cache

# 0 - A
# 1 - B
# 2 - C
# 3 - D
# 4 - E
# 5 - F
# 6 - G
# 7 - I
# 8 - L
# 9 - M
# 10 - N
# 11 - O
# 12 - P
# 13 - Q
# 14 - R
# 15 - S
# 16 - T
# 17 - U
# 18 - V
# 19 - W
# 20 - X
# 21 - Y

# As letras H, J, K, Z não serão reconhecidas porque essas letras são diferenciadas de outras por conta do movimento
# para realiza-las

cap = cv2.VideoCapture(0)
pTime = 0
distances = []
predict_letter = ""

detector = htm.handDetector()
new_model = tf.keras.models.load_model('saved_model_full_3')

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)

    image = cv2.flip(img, 1)

    # Printar FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    prediction_string = "Letra predita: {}"

    cv2.putText(image, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(image, prediction_string.format(predict_letter), (70, 400), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", image)
    cv2.waitKey(1)

    lmList = detector.findPosition(image, draw=False)

    if cv2.waitKey(2) & 0xFF == 27:
        cv2.destroyAllWindows()
        break

    if len(lmList) != 0:
        distances.clear()
        id1 = 0
        id2 = 0
        for lm1 in lmList:
            for lm2 in lmList:
                distance = math.sqrt(
                    (lmList[id1][0] - lmList[id2][0]) ** 2 + ((lmList[id1][1] - lmList[id2][1]) ** 2))

                if id1 != id2:
                    distances.append(distance)

                id2 += 1
            id2 = 0
            id1 += 1

        predictions = new_model.predict([distances])

        predict = np.argmax(predictions)
        # print(predict)

        if predict == 0:
            predict_letter = "A"

        if predict == 1:
            predict_letter = "B"

        if predict == 2:
            predict_letter = "C"

        if predict == 3:
            predict_letter = "D"

        if predict == 4:
            predict_letter = "E"

        if predict == 5:
            predict_letter = "F"

        if predict == 6:
            predict_letter = "G"

        if predict == 7:
            predict_letter = "I"

        if predict == 8:
            predict_letter = "L"

        if predict == 9:
            predict_letter = "M"

        if predict == 10:
            predict_letter = "N"

        if predict == 11:
            predict_letter = "O"

        if predict == 12:
            predict_letter = "P"

        if predict == 13:
            predict_letter = "Q"

        if predict == 14:
            predict_letter = "R"

        if predict == 15:
            predict_letter = "S"

        if predict == 16:
            predict_letter = "T"

        if predict == 17:
            predict_letter = "U"

        if predict == 18:
            predict_letter = "V"

        if predict == 19:
            predict_letter = "W"

        if predict == 20:
            predict_letter = "X"

        if predict == 21:
            predict_letter = "Y"

