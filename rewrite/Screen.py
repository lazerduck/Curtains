import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import threading

import subprocess

class Screen:
    line1 = "line1"
    line2 = "line2"
    line3 = "line3"
    line4 = "line4"
    selectedLine = -1

    def __init__(self):
    # Raspberry Pi pin configuration:
        RST = None     # on the PiOLED this pin isnt used
    # Note the following are only used with SPI:
        DC = 23
        SPI_PORT = 0
        SPI_DEVICE = 0
        disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        disp.begin()
        disp.clear()
        disp.display()
        self.width = disp.width
        self.height = disp.height
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
        padding = -2
        self.top = padding
        self.bottom = self.height-padding
        self.x = 0
        self.font = ImageFont.load_default()

    def __del__(self):
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

    def drawText(self):
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

        # Write two lines of text.
        self.draw.text((self.x, self.top),       self.line1,  font=self.font, fill=255)
        self.draw.text((self.x, self.top+8),       self.line2,  font=self.font, fill=255)
        self.draw.text((self.x, self.top+16),       self.line3,  font=self.font, fill=255)
        self.draw.text((self.x, self.top+24),       self.line4,  font=self.font, fill=255)

        # Display image.
        self.disp.image(self.image)
        self.disp.display()
        threading.Timer(0.1, self.drawText).start()
