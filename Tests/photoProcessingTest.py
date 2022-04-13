import cv2
import imutils
import pytesseract
import deepl

img = cv2.imread("photo.jpg")
#cv2.imwrite("test.jpg", img)

rotated = imutils.rotate(img,90)
cv2.imwrite("rotated.jpg", rotated)
print("done")

def processImage(image_path):
# Read image
    img = cv2.imread(image_path)
# Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = imutils.rotate_bound(img, angle=-90)

    cv2.imwrite("test.jpg", img)

processImage("photo.jpg")

# Tell pytesseract where tesseract is
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

def translateImage(image_path):
# Read image
    img = cv2.imread(image_path)
# Convert to RGB

    img = imutils.rotate_bound(img, angle=-90)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detect text from image
    text = pytesseract.image_to_string(img)
    print(text + '---------------')
# Translate text
    translator = deepl.Translator("b9ff2aae-ca1f-e192-56ae-a8c7faa94924:fx")
    result = translator.translate_text(text, target_lang="EN-GB")
    print(result)
    mode = "showTranslated"
    return result, mode

translateImage('photo.jpg')