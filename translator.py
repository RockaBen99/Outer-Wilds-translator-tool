##!/usr/bin/env python3
import os
import sys
import signal
import pygame
import cv2
import pytesseract
import deepl

from displayhatmini import DisplayHATMini

from gpiozero import Button
# Define buttons
buttonA = Button(5)
buttonB = Button(6)
buttonX = Button(16)
buttonY = Button(24)

# Constants
PHOTO_PATH = 'photo.jpg'

def takePhoto(photo_path):
    #os.system('libcamera-jpeg -n -o '+photo_path) # OS version >= 11:Bullseye
    os.system('raspistill -o '+ photo_path) # OS <= 10:Buster
    img = pygame.image.load(photo_path)
    img = pygame.transform.rotate(img, 90)
    img = pygame.transform.scale(img, (display_hat.HEIGHT, int(2592//(1944/display_hat.HEIGHT))))
    mode = "showPhoto"
    return img, mode

img, mode = takePhoto(PHOTO_PATH)

# Tell pytesseract where tesseract is
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

def translateImage(image_path):
# Read image
    img = cv2.imread(image_path)
# Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Detect text from image
    text = pytesseract.image_to_string(img)

# Translate text
    translator = deepl.Translator("b9ff2aae-ca1f-e192-56ae-a8c7faa94924:fx")
    result = translator.translate_text(text, target_lang="EN-GB")
    mode = "showTranslated"
    return result, mode






print("""Display HAT Mini: Basic Pygame Demo""")


def _exit(sig, frame):
    global running
    running = False
    print("\nExiting!...\n")


def update_display():
    display_hat.st7789.set_window()
    # Grab the pygame screen as a bytes object
    pixelbytes = pygame.transform.rotate(screen, 180).convert(16, 0).get_buffer()
    # Lazy (slow) byteswap:
    pixelbytes = bytearray(pixelbytes)
    pixelbytes[0::2], pixelbytes[1::2] = pixelbytes[1::2], pixelbytes[0::2]
    # Bypass the ST7789 PIL image RGB888->RGB565 conversion
    for i in range(0, len(pixelbytes), 4096):
        display_hat.st7789.data(pixelbytes[i:i + 4096])


display_hat = DisplayHATMini(None)

os.putenv('SDL_VIDEODRIVER', 'dummy')
pygame.display.init()  # Need to init for .convert() to work
screen = pygame.Surface((display_hat.WIDTH, display_hat.HEIGHT))

signal.signal(signal.SIGINT, _exit)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

    # Clear the screen
    screen.fill((0, 0, 0))

    box_w = display_hat.WIDTH
    box_h = display_hat.HEIGHT

    if buttonX.is_pressed:
        img, mode = takePhoto(PHOTO_PATH)
    elif buttonY.is_pressed:
        translated, mode = translateImage()
    
    if mode == 'showPhoto':
        screen.blit(img, (0,0))
    elif mode == 'showTranslated':
        pass # Text output goes here

    update_display()


pygame.quit()
sys.exit(0)