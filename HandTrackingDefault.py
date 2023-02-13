import cv2
import HandTrackingModule as htm
import time

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)

pTime = 0

while True:
    success, img = cap.read()

    img = detector.findHands(img, draw=True)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
