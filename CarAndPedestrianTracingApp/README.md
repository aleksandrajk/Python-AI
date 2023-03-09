# Face Detector App using OpenCV

This is a Python application for detecting and tracking cars and pedestrians in videos using OpenCV. The application uses a pre-trained object detection model from OpenCV.

## Features
* Detects cars and pedestrians in images or videos
* Draws a bounding box around each detected object
* Can handle multiple objects in the same image or video


## Technologies Used
* Python
* OpenCV


## Installation
To use this application, you will need to have Python 3.6 or higher installed on your system. You will also need to install the following Python package:
* OpenCV (version 4.2.0 or higher). 

You can install this package using pip:
```
pip install opencv-python
```


## Usage
1. Open the app by running __'python CarAndPedestrianTracing.py'__.
2. Wait for the app to finish processing the file.
3. The processed file will be displayed on the app window with bounding boxes around the detected cars and pedestrians.


## Credits
The Haar Cascade classifier used in this application was trained using the OpenCV training module. Special thanks to the OpenCV community for providing the training tools and resources.
Use these links to learn more about [Cascade Classifier](https://docs.opencv.org/2.4/doc/tutorials/objdetect/cascade_classifier/cascade_classifier.html) and [Cascade Classifier Training](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html).
