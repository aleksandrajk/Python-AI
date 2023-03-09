import cv2

# Get video
video = cv2.VideoCapture('LondonDrivingDowntown.mp4')
# Load some pre-trained data 
car_tracker = cv2.CascadeClassifier('car_tracking.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')


while True:

    # Read the current frame
    (read_successful, frame) = video.read()

    if read_successful:
        # Convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break    

    # Detect cars and pedestriand
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)


    # Draw rectangles around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (17, 255, 238) ,2)

    # Draw rectangles around the pedestrians
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 132, 67) ,2)

    # Display the image with the figures spotted
    cv2.imshow('Car and Pedestrian Tracking', frame)

    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

# Release the VideoCapture object
video.release()

'''
# For images
# img = cv2.imread('test.png')
# Load some pre-trained data 
car_tracker = cv2.CascadeClassifier('car_tracking.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')


grayscaled_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_tracker.detectMultiScale(grayscaled_frame)

pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)


# Draw rectangles around the cars
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (17, 255, 238) ,2)

# Draw rectangles around the pedestrians
for (x, y, w, h) in pedestrians:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 132, 67) ,2)
    

# Display the image with the figures spotted
cv2.imshow('Car and Pedestrian Tracking', img)
cv2.waitKey()
'''
