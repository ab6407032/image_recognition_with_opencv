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
