import cv
import sys
HAAR_CASCADE_PATH = "haarcascade_frontalface_default.xml"
HAAR_CASCADE_PATH = "parojosG45x11.xml"
def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        #print "line", lineno

    return traceit



storage = cv.CreateMemStorage()
cascade = cv.Load(HAAR_CASCADE_PATH)
faces = []

def detect_faces(image):
    faces = []
    detected = cv.HaarDetectObjects(image, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (45,11))
    if detected:
        for (x,y,w,h),n in detected:
            faces.append((x,y,w,h))
    return faces



cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)
i=0

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    global i
    global faces


    frame = cv.QueryFrame(capture)
    image = frame

    # Only run the Detection algorithm every 5 frames to improve performance
    if i%6==0:
       faces = detect_faces(image)

    for (x,y,w,h) in faces:
        cv.Rectangle(image, (x,y), (x+w,y+h), 255)
    cv.ShowImage("w1", frame)
    c = cv.WaitKey(10)
    i=i+1
    if(c=="n"): #in "n" key is pressed while the popup window is in focus
        camera_index += 1 #try the next camera index
        capture = cv.CaptureFromCAM(camera_index)
        if not capture: #if the next camera index didn't work, reset to 0.
            camera_index = 0
            capture = cv.CaptureFromCAM(camera_index)

sys.settrace(traceit)

while True:
    repeat()
