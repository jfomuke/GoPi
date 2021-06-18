
import tkinter as tk
import time
import picamera

camera1 = picamera.PiCamera()

# V2 PiCamera:
# 3280x2464 , 15 fps max, FoV Full
# 1640x1232, 40 fps max, Fov Full
# 1280x720, 90fps max, FoV Limited
camera1.resolution = (1640, 1232)
# camera1.resolution = (1920, 1080)
camera1.framerate = 30

def createNewUniqueFilename():      
    fileName = (int(time.time()))
    return fileName

def start_button(event):
    try:
        camera1.resolution = (1640, 1232)
        camera1.framerate = 30
        # true false for duplicate presses          
        fileNameTemp = createNewUniqueFilename()
        fileNameTemp = str(fileNameTemp) + ".h264"
        camera1.start_recording(fileNameTemp)
        # camera1.wait_recording(5)
    finally:
        print("Start button clicked!")


def stop_button(event):
    try:
        camera1.stop_recording()
        # camera1.close()
    finally:
        print("Stop button clicked! Recording has been stopped & Saved")


def screenshot_button(event):
    try:
        fileNameTemp = createNewUniqueFilename()
        fileNameTemp = str(fileNameTemp) + ".jpg"
        camera1.annotate_text = ''
        camera1.resolution = (1980, 1080)
        camera1.capture(fileNameTemp)
        print("Picture Taken")
    finally:
        print("Done")

def preview_button(event):
    try:
        camera1.resolution = (1640, 1232)
        camera1.framerate = 30
        camera1.start_preview()
        camera1.annotate_text = 'Hello world! this is overlaid text'
        time.sleep(5)
        camera1.stop_preview()
    finally:
        print("Preview Done")

window = tk.Tk()

frame1 = tk.Frame(master=window, width=400, height=400, bg="red")
frame1.pack()

btn1 = tk.Button(master=frame1, text="Start", width=20, height=5)
btn1.place(x=0, y=0)
btn1.bind('<Button-1>', start_button)


btn2 = tk.Button(master=frame1, text="Stop", width=20, height=5)
btn2.place(x=0, y=100)
btn2.bind('<Button-1>', stop_button)

btn3 = tk.Button(master=frame1, text="Picture", width=20, height=5)
btn3.place(x=200, y=0)
btn3.bind('<Button-1>', screenshot_button)

btn4 = tk.Button(master=frame1, text="5s Preview(1232p)", width=20, height=5)
btn4.place(x=200, y=100)
btn4.bind('<Button-1>', preview_button)

window.mainloop()

# widget.bind('<Double-1>', quit) for double clicks
