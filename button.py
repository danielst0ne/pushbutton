import RPi.GPIO as GPIO
import time
from datetime import datetime
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
while True:
    
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        camera.capture('img/{}.jpg'.format(datetime.now()))

        time.sleep(0.2)





# Camera warm-up time



# Camera warm-up time


