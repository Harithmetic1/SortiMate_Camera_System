import time
import cv2
import os

class CameraHandler:
    def __init__(self) -> None:
        self.cam = cv2.VideoCapture(0)
        if not self.cam.isOpened():
            print("Failed to open camera")

    def takePicture(self):
        time.sleep(2)
        ret, image = self.cam.read()
        file_path = os.path.join(os.getcwd() + '/capturedImage.jpg')
        cv2.imwrite(file_path, image)
        self.cam.release()
        cv2.destroyAllWindows()
        self.cam = cv2.VideoCapture(0)

    def streamVideo(self):
        while True:
            ret, image = self.cam.read()
            cv2.imshow('Imagetest',image)
            k = cv2.waitKey(1)
            if k != -1:
                break
        # self.cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = CameraHandler()
    cam.streamVideo()
