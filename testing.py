import picamera
import time

camera1 = picamera.PiCamera()
camera1.resolution = (1640, 1232)
camera1.framerate = 30
camera1.start_preview()
camera1.annotate_text = 'Hello world!'
time.sleep(5)
camera1.capture('foo.jpg')
camera1.stop_preview()