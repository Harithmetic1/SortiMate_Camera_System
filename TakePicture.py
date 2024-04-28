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

    def streamVideo(self, zoom_factor=0.5):  # Add zoom_factor argument
        while True:
            ret, image = self.cam.read()

            # Get image width and height
            width = image.shape[1]
            height = image.shape[0]

            # Define new width and height based on zoom factor
            new_width = int(width * zoom_factor)
            new_height = int(height * zoom_factor)

            # Calculate starting pixel coordinates for cropping
            start_x = int((width - new_width) / 2)
            start_y = int((height - new_height) / 2)

            # Crop the image
            cropped_image = image[start_y:start_y + new_height, start_x:start_x + new_width]

            cv2.imshow('Imagetest', cropped_image)
            k = cv2.waitKey(1)
            if k != -1:
                break
            cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = CameraHandler()
    cam.streamVideo()
