import cv2
import pytesseract
import deepl

# Tell pytesseract where tesseract is
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

def translateImage():
# Read image
    img = cv2.imread('photo.jpg')
# Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detect text from image
    text = pytesseract.image_to_string(img)

# Translate text
    translator = deepl.Translator("b9ff2aae-ca1f-e192-56ae-a8c7faa94924:fx")
    result = translator.translate_text(text, target_lang="EN-GB")
    return result

translated = translateImage()