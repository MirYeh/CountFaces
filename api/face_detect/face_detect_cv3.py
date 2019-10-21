import os

import cv2


def run(image_path, show_image=False):
    # Get user supplied values
    base_path_index = __file__.rfind(os.sep)
    base_path = __file__[:base_path_index + 1]
    cascade_path = f'{base_path}haarcascade_frontalface_default.xml'

    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(cascade_path)

    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if show_image:
        cv2.imshow("Faces found", image)
        cv2.waitKey(0)

    return len(faces)
