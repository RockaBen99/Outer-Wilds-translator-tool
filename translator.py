import cv2
import pytesseract
#from translate import Translator
import deepl
import os

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

# Reading image
img = cv2.imread('photo.jpg')
# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Detect text from image
text = pytesseract.image_to_string(img)
print(text)

# Return each detected character and their bounding boxes
#boxes = pytesseract.image_to_boxes(img)
#print(boxes)

# Show the output
#cv2.imshow("Output", img)
#cv2.waitKey(0)



# OLD Translate text
#translator = Translator(to_lang='fr')
#translation = translator.translate("I am called Benedict")
#print(translation)

# Translate text
translator = deepl.Translator("b9ff2aae-ca1f-e192-56ae-a8c7faa94924:fx")
result = translator.translate_text(text, target_lang="EN-GB")
print("\n\n\n\n\n\n\n\n"+str(result))