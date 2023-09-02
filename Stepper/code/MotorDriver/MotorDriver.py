from RPi import GPIO
import time

class MotorDriver:
    def __init__(self, step_pin, dir_pin, mode_pin, step_type, fullstep_delay):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        self.mode_pin = mode_pin
        self.fullstep_delay = fullstep_delay
        self.step_type = step_type
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(mode_pin, GPIO.OUT)
        self.resolution = {'Full':(0, 0, 0),
                    'Half':(1, 0, 0),
                    '1/4':(0, 1, 0),
                    '1/8':(1, 1, 0),
                    '1/16':(0, 0, 1),
                    '1/32':(1, 0, 1)}
        self.microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
        self.updateStepAndDelay()

    def updateStepAndDelay(self):
        self.delay = self.fullstep_delay/self.microsteps[self.step_type]
        GPIO.output(self.mode_pin, self.resolution[self.step_type])

    def setStepType(self, step_type):
        self.step_type = step_type
        self.updateStepAndDelay()

    def setFullstepDelay(self, fullstep_delay):
        self.fullstep_delay = fullstep_delay
        self.updateStepAndDelay()

    def step(self, steps, clockwise):
        print("Stepping " + str(steps) + " steps " + ("clockwise" if clockwise else "anticlockwise"))
        GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(self.delay)