from CurtainState import CurtainState
from MotorController import MotorController
from RotaryDriver.RotaryDriver import RotaryDriver

motorController = MotorController(11, 13, 15, 16, 18, 22) # Need to check the actual pins
state = CurtainState()
RotaryDriver = RotaryDriver(29, 31, 33) # Need to check the actual pins

def loop():
    applyLightSensor()
    stepMotor()
    state.setTargetPosition(RotaryDriver.pos)

def applyLightSensor():
    if state.isLightSensorEnabled:
        if state.shouldOpenIfLight() or state.mustOpen():
            state.setOpen()
        elif state.shouldCloseIfNight() or state.mustClose():
            state.setClosed()

def stepMotor():
    if state.targetPosition > state.position and state.canClose():
        motorController.setDirection(1)
        motorController.step(state.speed)
        state.position += 1
    elif state.targetPosition < state.position and state.canOpen():
        motorController.setDirection(0)
        motorController.step(state.speed)
        state.position -= 1

while True:
    loop()