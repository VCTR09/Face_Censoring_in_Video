## Censoring Faces Using Cat Face
# A program reads a video and censors peoples' faces in the video replacing them with cat faces.


import cv2
 
# Load the video
video = cv2.VideoCapture("IMG_4909.mov")
 
# Load the cat face image in color
cat = cv2.imread("catface.png", 1)
 
# Get the first frame and the width and height of the video
success, frame = video.read()  # Read the first frame of the video to check if it's read correctly
height = frame.shape[0]  # Get the height of the first frame
width= frame.shape[1]  # Get the width of the first frame
 
# Load the face cascade
face_cascade = cv2.CascadeClassifier('faces.xml')
# faces.xml - Cascade file which contains a set of instructions of how human faces look like
 
# Prepare the video object where the output video will be stored
output= cv2.VideoWriter('catoutput.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
 
# Read the frames one by one, detect faces, and overlay the cat face on them
count = 0
while success:  # if success == True
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)  # Detect faces in different scales in the first frame
    for (x,y,w,h) in faces:  # Iterate over faces (dimensions of the rectangle around the detected face)
        rscat = cv2.resize(cat, (w, h)) # Resize cat's face so it's the same size with the rectangle around the face
        place = frame[y:y+h, x:x+w]  # Store in a variable the particular slice of the current frame where the face is
        cv2.imwrite('rscat.jpg', place)  # Saving the image
        blend = cv2.addWeighted(place, 0, rscat, 1,0)  # Adding/blending two images
        cv2.imwrite("fcat.jpg", blend)  # Saving the image
        frame[y:y+h, x:x+w] = blend
    output.write(frame)  # Write the modified frame into the output video object
    success, frame = video.read()  # Go to other frames (next after the first one)
    count += 1
    print(count)  # Improve the experience of programm execution (can see the while loop being executed)
 
output.release  # Release the video and make it able to write on disk
