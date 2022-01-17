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
buttonA = Button(5)
buttonB = Button(6)
buttonX = Button(16)
buttonY = Button(24)

img = pygame.image.load('photo.jpg')

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

def takePhoto():
    os.system("libcamera-jpeg -n -o photo.jpg")
    img = pygame.image.load('photo.jpg')
    img = pygame.transform.rotate(img, 90)
    img = pygame.transform.scale(img, (display_hat.HEIGHT, int(2592//(1944/display_hat.HEIGHT))))
    mode = "photo"
    return img

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
        img = takePhoto()
    screen.blit(img, (0,0))

    update_display()


pygame.quit()
sys.exit(0)