import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

while True:
    x = input("Enter pin number: ")
    y = input("Enter state: ")
    GPIO.setup(int(x), GPIO.OUT)
    GPIO.output(int(x), int(y))

# for x in range(1, 20):
#     try:
#         print(x)
#         GPIO.setup(x, GPIO.OUT)
#         GPIO.output(x, 0)
#         time.sleep(2)
#         #GPIO.output(x, 0)
#     except:
#         print("exception")

#GPIO.cleanup()
    