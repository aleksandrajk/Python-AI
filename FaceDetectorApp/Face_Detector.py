import cv2

# Load some pre-trained data to detect face
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image/video/webcam to detect faces in
webcam = cv2.VideoCapture(0) 
# #To detect faces in an image
#img = cv2.imread('file.jpg')
# #To detect faces in a chosen video
#video = cv2.VideoCapture('file.MOV')

# Iterate the loop
while True:

    # Read the current frame
    succesful_frame_read, frame = webcam.read()

    # Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in frame
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)


    if key==81 or key==113:
        break

webcam.release()
