class MotorController:
    def __init__(self, stepPin, dirPin, enablePin) -> None:
        self.stepPin = stepPin
        self.dirPin = dirPin
        self.enablePin = enablePin