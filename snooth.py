#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13d
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

#Set output log level
logging.basicConfig(level=logging.DEBUG)

epd = epd2in13d.EPD()
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear(0xFF)      # clear the display

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in13d.EPD_HEIGHT, epd2in13d.EPD_WIDTH), 255)
    HRedImage = Image.new('1', (epd2in13d.EPD_HEIGHT, epd2in13d.EPD_WIDTH), 255)
    
    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('/opt/vc/src/hello_pi/hello_font/Vera.ttf', 20) # Create our font, passing in the font file and font size
    
    draw.text((15, 35), string, font = font, fill = 0)

    #epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
    epd.display(epd.getbuffer(HBlackImage))

    print("Sleep for 2 secs.")
    time.sleep(2)
    print("clearing.")
    epd.Clear(0xFF)      # clear the display

    print("clearning")
    time.sleep(2)
    epd.Clear(0xFF)      # clear the display


printToDisplay("Hello, World!")



