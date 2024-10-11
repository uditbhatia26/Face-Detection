# Face Detection Using OpenCV

This project demonstrates real-time face detection using OpenCV and the Haar Cascade Classifier. The application captures video from the webcam, detects faces, and highlights them with red rectangles.

## Features

- Real-time face detection from the webcam.
- Uses the `haarcascade_frontalface_default.xml` classifier to detect faces.
- Simple and easy-to-understand Python code using OpenCV.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- A webcam for real-time face detection

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/uditbhatia26/Face-Detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Face-Detection
    ```

3. Install the required Python libraries:

    ```bash
    pip install opencv-python
    ```

4. Ensure the `haarcascade_frontalface_default.xml` file is in the project directory. You can download it from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) if it's missing.

## How to Run

1. Run the `face_detection.py` script:

    ```bash
    python face_detection.py
    ```

2. The webcam will open, and the application will detect faces, drawing red rectangles around them in real-time.

3. Press the `Esc` key to exit the program.
