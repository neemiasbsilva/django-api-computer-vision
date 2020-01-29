import cv2


def stream_video():

    video_capture = cv2.VideoCapture(0)

    while True:
        try:
            check, frame = video_capture.read()

            cv2.imshow("STREAM", frame)

            key = cv2.waitKey(1)

            if key == ord('q'):
                print("Turning off camera.")
                video_capture.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            video_capture.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break