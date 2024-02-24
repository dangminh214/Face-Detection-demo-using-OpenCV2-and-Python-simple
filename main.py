import cv2
image = cv2.imread('example_nasa_pilots.jpg')
image_resized = cv2.resize(image, (1000,800))
# create a face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# turn original image to gray
gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

# face detection and recognize
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# draw face detection
for (x, y, w, h) in faces:
    cv2.rectangle(image_resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

# show the result
cv2.imshow('Detected Faces Result', image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()