import cv2
import mediapipe as mp
import pickle
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# IMAGE_FILES = ['images/test.png']
IMAGE_FILES = []
filename = 1
lastImage = 220
distances = []

path = "images_full/{}.png"

while filename <= lastImage:
    IMAGE_FILES.append(path.format(filename))
    filename += 1
    #print("IMAGE FILES: ")
    #print(IMAGE_FILES)

print("Finished ...")
filename = 1

with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:
    for idx, file in enumerate(IMAGE_FILES):

        image = cv2.imread(file)
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        lmList = []

        if results.multi_hand_landmarks:
            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)

                lmList.append([id, cx, cy])

        if len(lmList) != 0:
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

        # Colocando a lista em arquivos na pasta "data"
        with open(f'data_full/{int(filename)}', "wb") as fp:  # Pickling

            pickle.dump(distances, fp)

        filename += 1
        distances.clear()
