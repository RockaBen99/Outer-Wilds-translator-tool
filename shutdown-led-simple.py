#!/usr/bin/env python3
from gpiozero import Button, LED
from signal import pause
import os, sys

offGPIO = int(sys.argv[1]) if len(sys.argv) >= 2 else 3
holdTime = int(sys.argv[2]) if len(sys.argv) >= 3 else 6
ledGPIO = int(sys.argv[3]) if len(sys.argv) >= 4 else 17

def when_pressed():
    # start blinking with 1/2 second rate
    ledR.blink(on_time=0.5, off_time=0.5)

def when_released():
    # be sure to turn the LEDs off if we release early
    ledR.off()

def shutdown():
    os.system("sudo poweroff")

ledR = LED(ledGPIO,)
powerButton = Button(offGPIO, hold_time=holdTime)
powerButton.when_held = shutdown
powerButton.when_pressed = when_pressed
powerButton.when_released = when_released
pause()
