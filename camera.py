import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

ret, frame = cap.read()

i = 0
while i < 5:
    i += 1
    ret, frame = cap.read()

cv2.imwrite('image.jpg', frame)

cap.release()
cv2.destroyAllWindows()
