import cv2
import numpy as np
 
# Load the video
video = cv2.VideoCapture("smile.mp4")
 
# Load the cat face image in color
cat = cv2.imread("catface.png", 1)

# print(cat[40, 40])     
 
# Get the first frame and the width and height of the video
success, frame = video.read()
height = frame.shape[0]
width= frame.shape[1]
 
# Load the face cascade
face_cascade = cv2.CascadeClassifier('faces.xml')
 
# Prepare the video object where the output video will be stored
output= cv2.VideoWriter('catoutput.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
 
# Read the frames one by one, detect faces, and overlay the cat face on them
count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x,y,w,h) in faces:
        rscat = cv2.resize(cat, (w, h))
        place = frame[y:y+h, x:x+w]
        # cv2.imwrite('rscat.jpg', place)
        rscat_width = rscat.shape[1]
        rscat_height = rscat.shape[0]
        # Iterate through catface.png to remove green pixels
        for i in range(rscat_width):
            for j in range(rscat_height):
                pixel = rscat[j, i]
                # print(type(pixel))
                if np.any(pixel == [79, 248, 117]):
                    rscat[j, i] = place[j, i]
        # blend = cv2.addWeighted(place, 0, rscat, 1,0)
        # cv2.imwrite("fcat.jpg", rscat)
        frame[y:y+h, x:x+w] = rscat
    output.write(frame)
    success, frame = video.read()
    count += 1
    print(count)
 
output.release
