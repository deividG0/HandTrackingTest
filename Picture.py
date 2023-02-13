import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
ret,frame = cap.read() # return a single frame in variable `frame`

# while(True):
#     cv2.imshow('img1',frame) #display the captured image
#     if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
#         cv2.imwrite('images/test.png',frame)
#         cv2.destroyAllWindows()
#         break
#
# cap.release()

filename = 97

path = "images_full/{}.png"

while True:
    success, img = cap.read()

    image = cv2.flip(img, 1)

    cv2.imshow("Image", image)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
        cv2.imwrite(path.format(filename), frame)
        print("i got here: " + path.format(filename) + " and: " + str(filename))
        filename += 1
        ret, frame = cap.read()

    if cv2.waitKey(2) & 0xFF == 27:
        cv2.destroyAllWindows()
        break

cap.release()