import base64
import time
import gpiod
from NetworkControllerClass import NetworkController
from TakePicture import CameraHandler
from ArduinoController import ArduinoController

PIR_PIN = 17
ENCODING = 'utf-8'

camera = CameraHandler()
api = NetworkController()
arduino = ArduinoController()

chip = gpiod.Chip('gpiochip4')

pir_line = chip.get_line(PIR_PIN)

pir_line.request(consumer="PIR", type=gpiod.LINE_REQ_DIR_IN)

def detectWaste():
    camera.takePicture()
    with open('capturedImage.jpg', 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        base64_string = base64_bytes.decode(ENCODING)
        return api.classifyWaste(image=base64_string)
    
def sortWaste():
    try:
        arduino.write(detectWaste())
    except Exception as e:
        print(f"Error, could not write to arduino: {e}")
    


try:
    while True:
        pir_state = pir_line.get_value()
        print(f"PIR is: {pir_state}")
        if pir_state == 1:
            sortWaste()
            time.sleep(3)
        else:
            time.sleep(1)
        
finally:
    pir_line.release()
