#!/usr/bin/python
import os
# import RPi.GPIO as GPIO
from datetime import datetime

gameLoop = True

def player():
    print("I'm the player")

def drawScrn():
    print("Drawing the screen")
    player()

def main():
    drawScrn()

if gameLoop == False:
    print("Game loop hasn't been enabled!")

if gameLoop == True:
    main()