import cv2
import numpy as np
import helpers as hl

#load image from a file
image = cv2.imread('sample.jpg')

# Get screen dimensions
screen_width, screen_height = hl.get_screen_dimensions()

# Resize the image
resized_image = hl.resize_image(image, screen_width, screen_height)

#display image in a window
#cv2.imshow("Loaded Image", resized_image)
#cv2.waitKey(0) #wait untill a key is pressed
#cv2.destroyAllWindows()

#convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#reduce noise with gaussian blur filter 
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#edge detection using canny
edges = cv2.Canny(blurred_image, 50, 150)

# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#detect faces in image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))

#draw rectangle around faces
for(x, y, w, h) in faces:
    cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Detected Faces", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()