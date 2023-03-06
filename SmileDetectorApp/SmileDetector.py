import cv2

# Load some pre-trained data to detect face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')

# Choose webcam to detect faces in
webcam = cv2.VideoCapture(0) 

# Iterate the loop
while True:

    # Read the current frame
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        break

    # Convert to grayscale
    frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in frame
    faces = face_detector.detectMultiScale(frame_grayscaled)
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x,y), (x+w, y+h), (100, 200, 50), 4)
        
        face = frame[y:y+h, x:x+w]
        face_grayscaled = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(face_grayscaled, scaleFactor = 1.7, minNeighbors = 20)
        
        # Find smiles in the face
        # for (x_, y_, w_, h_) in smiles:
        #     cv2.rectangle(face, (x_, y_), (x_ + w_, y_ + h_), (50, 50, 200), 4)

        # Label 'smiling'
        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale =3, 
            fontFace = cv2.FONT_HERSHEY_PLAIN, color = (255,255,255))

    cv2.imshow('Smile Detector', frame)
    key = cv2.waitKey(1)


    if key==81 or key==113:
        break

webcam.release()
cv2.destroyAllWindows()
