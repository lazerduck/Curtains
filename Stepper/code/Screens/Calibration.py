from ScreenBase import ScreenBase
import CurtainState


class Calibration(ScreenBase):
    def __init__(self) -> None:
        self.state = CurtainState.CurtainState()
        pass

    def start(self):
        pass