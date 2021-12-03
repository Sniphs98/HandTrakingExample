import cv2
import mediapipe as media_pipe
import time


class hand_detector():
    def __init__(self,
        static_image_mode = False,
        max_num_hands = 2,
        model_complexity = 1,
        min_detection_confidence = 0.5,
        min_tracking_confidence = 0.5):




hands_media_pipe = media_pipe.solutions.hands
hands = hands_media_pipe.Hands()
draw_media_pipe = media_pipe.solutions.drawing_utils


    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,"\n",lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 4:
                    cv2.circle(img,(cx,cy), 10, (255,0,255), cv2.FILLED)

            draw_media_pipe.draw_landmarks(img, handLms, hands_media_pipe.HAND_CONNECTIONS)



def main():

    previous_time = 0
    current_time = 0
    camera_capture = cv2.VideoCapture(0)

    while True:
        success, img = camera_capture.read()

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()