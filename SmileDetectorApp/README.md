# Smile Detector App using OpenCV

This project is an implementation of a Smile Detector app using OpenCV library in Python. The app detects faces in real-time video feed from your device's camera and then detects if the person is smiling or not.

## Technologies Used
* Python
* OpenCV

## Installation
To run this project, you need to have Python installed on your system along with OpenCV library. You can install OpenCV using the following command:
```
pip install opencv-python
```

## Usage
To run the app, simply run the SmileDetector.py file using Python. The app will start capturing the video feed from your device's camera and will detect faces and smiles in real-time.
```
python SmileDetector.py
```

## How it works
The app works by using Haar Cascade Classifiers to detect faces and smiles in the video feed. The face detection is performed first, and then the region of interest (ROI) containing the face is used for smile detection. The smile detection algorithm is based on the detection of the curvature of the mouth corners. If the curvature exceeds a certain threshold, the app considers the person to be smiling.

## Credits
The Haar Cascade classifier used in this application was trained using the OpenCV training module. Special thanks to the OpenCV community for providing the training tools and resources.
Use these links to learn more about [Cascade Classifier](https://docs.opencv.org/2.4/doc/tutorials/objdetect/cascade_classifier/cascade_classifier.html) and [Cascade Classifier Training](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html).
