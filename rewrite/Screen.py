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
    selectedLine = 1

    def __init__(self):
    # Raspberry Pi pin configuration:
        RST = None     # on the PiOLED this pin isnt used
    # Note the following are only used with SPI:
        self.disp = Adafruit_SSD1306.SSD1306_128_32(RST)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('1', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
        padding = -2
        self.top = padding
        self.bottom = self.height-padding
        self.x = 0
        self.font = ImageFont.load_default()
        self.drawText()
        print("Screen started")

    def __del__(self):
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

    def drawText(self):
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)

        lines = self.getLines()
        offset = 0
        
        for line in lines:
            if(line.selected):
                self.draw.rectangle((self.x, self.top + offset,self.width,self.top + (2*offset)), outline=0, fill=255)
            self.draw.text((self.x, self.top + offset), line.text, font=self.font, fill=255 if line.selected else 0)

        # Display image.
        self.disp.image(self.image)
        self.disp.display()
        threading.Timer(0.1, self.drawText).start()

    def getLines(self):
        return [
            {"text": self.line1, "selected": self.selectedLine == 1},
            {"text": self.line2, "selected": self.selectedLine == 2},
            {"text": self.line3, "selected": self.selectedLine == 3},
            {"text": self.line4, "selected": self.selectedLine == 4}]
