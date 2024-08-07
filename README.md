# image_recognition_with_opencv
This repository contains a simple image recognition system using OpenCV for facial detection. The system uses Haar Cascades for detecting faces in an image. 

## Prerequisites

- Python 3.6 or higher
- OpenCV 4.x
- Numpy 2.0.0

## Installation

To install the necessary packages, you can use the provided `requirements.txt` file. Run the following command:

```bash
pip install -r requirements.txt
```

## Files Description

- `face_detection.py`: The main script that loads an image, processes it, and detects faces using Haar Cascades.
- `helpers.py`: Contains helper functions used in the main script.
- `haarcascade_frontalface_default.xml`: Haar Cascade file for face detection.
- `sample.jpg`: A sample image to test the face detection.
- `requirements.txt`: Contains the list of required packages.

## Usage

1. Place the image you want to use for face detection in the same directory as the scripts or provide the path to the image.
2. Run the `face_detection.py` script:

```bash
python face_detection.py --image sample.jpg
```

Replace `sample.jpg` with the path to your image file if different.

## face_detection.py

This script performs the following steps:
1. Loads the image.
2. Converts the image to grayscale.
3. Loads the Haar Cascade file for face detection.
4. Detects faces in the image.
5. Draws rectangles around detected faces.
6. Displays the processed image with detected faces.

### Example Code

```python
import cv2
import argparse

def detect_faces(image_path, cascade_path):
    # Load the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the Haar Cascade file
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Face detection using Haar cascades.")
    parser.add_argument("--image", required=True, help="Path to the input image.")
    parser.add_argument("--cascade", default="haarcascade_frontalface_default.xml", help="Path to the Haar cascade file.")
    args = parser.parse_args()
    
    detect_faces(args.image, args.cascade)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV library
- Haar Cascades for face detection provided by OpenCV
