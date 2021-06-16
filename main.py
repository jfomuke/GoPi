
import tkinter as tk
import time
import picamera

camera1 = picamera.PiCamera()

# V2 PiCamera:
# 3280x2464 , 15 fps max, FoV Full
# 1640x1232, 40 fps max, Fox Full
# 1280x720, 90fps max, FoV Limited
camera1.resolution = (1640, 1232)
camera1.framerate = 30

def start_button(event):
    try:
        # true false for duplicate presses          
        fileName = (int(time.time()))
        fileName = str(fileName) + ".h264"
        camera1.start_recording(fileName)
        # camera1.wait_recording(5)
    finally:
        print("Start button clicked!")

def stop_button(event):
    try:
        camera1.stop_recording()
        # camera1.close()
    finally:
        print("Stop button clicked! Recording has been stopped & Saved")

window = tk.Tk()

frame1 = tk.Frame(master=window, width=400, height=400, bg="red")
frame1.pack()

btn1 = tk.Button(master=frame1, text="Start", width=20, height=5)
btn1.place(x=0, y=0)
btn1.bind('<Button-1>', start_button)


btn2 = tk.Button(master=frame1, text="Stop", width=20, height=5)
btn2.place(x=0, y=100)
btn2.bind('<Button-1>', stop_button)

btn3 = tk.Button(master=frame1, text="Temp", width=20, height=5)
btn3.place(x=200, y=0)
btn3.bind('<Button-1>', start_button)

window.mainloop()

# widget.bind('<Double-1>', quit) for double clicks