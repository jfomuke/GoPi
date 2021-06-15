
import picamera
camera1 = picamera.PiCamera()
camera1.start_recording('test.h264')
camera1.wait_recording(5)
camera1.stop_recording()
camera1.close()

