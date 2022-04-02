import cv2
import imutils

img = cv2.imread("photo.jpg")
#cv2.imwrite("test.jpg", img)

rotated = imutils.rotate(img,90)
cv2.imwrite("rotated.jpg", rotated)
print("done")

def translateImage(image_path):
# Read image
    img = cv2.imread(image_path)
# Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = imutils.rotate_bound(img, angle=-90)

    cv2.imwrite("test.jpg", img)

translateImage("photo.jpg")