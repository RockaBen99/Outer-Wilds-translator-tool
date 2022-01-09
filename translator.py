import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# Reading image
img = cv2.imread('Screenshot.png')
# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Detect text from image
text = pytesseract.image_to_string(img)
print(text)

# Return each detected character and their bounding boxes
boxes = pytesseract.image_to_boxes(img)
print(boxes)


# Show the output
cv2.imshow("Output", img)
cv2.waitKey(0)