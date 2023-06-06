import RPi.GPIO as GPIO
import time
import rotaryDriver

GPIO.setmode(GPIO.BOARD)

print("Starting")

driver = rotaryDriver.rotaryDriver(19,21,23)

while(True):
    #driver.pollRotary()
    time.sleep(0.01)
    #print(driver.pos)