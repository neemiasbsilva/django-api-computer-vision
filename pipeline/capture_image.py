import cv2


def capture_image(path):
    video_capture = cv2.VideoCapture(0)

    while True:
        try:
            check, frame = video_capture.read()

            cv2.imshow("STREAM", frame)

            key = cv2.waitKey(1)

            if key == ord('c'):
                img = frame

                cv2.imwrite(path, img)
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
